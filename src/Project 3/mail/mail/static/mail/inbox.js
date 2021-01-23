const API_URL = 'http://localhost:8000'
const INBOX_COLUMNS = ['sender', 'body', 'timestamp'] 
 
// TODO: remove empty tbody
document.addEventListener('DOMContentLoaded', function() {
    // use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);
    
    // by default, load the inbox
    load_mailbox('inbox');
});

function compose_email() {
    // show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#single-email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    document.querySelector('#compose-reply-view').style.display = 'none';
  
    // clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';

    const element = document.getElementsByClassName('btn btn-primary')[0];
    element.addEventListener('click', () => {
        const form_data = document.querySelector('#compose-form');
        const data = get_form_data(form_data);
        send_mail(data);
    });
}

const compose_reply_email = (data => {
    // show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    //document.querySelector('#single-email-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#compose-reply-view').style.display = 'block';
    // clear out composition fields
    document.querySelector('#compose-reply-recipients').value = display_recipients(data['recipients']);
    document.querySelector('#compose-reply-subject').value = `Re: ${data['subject']}`;
    document.querySelector('#compose-reply-body').value = '';

    const element = document.getElementsByClassName('btn btn-primary')[1];
    element.addEventListener('click', () => {
        const form_element = document.querySelector('#compose-reply-form');
        const form_data = get_form_data(form_element);
        send_mail(form_data);
    });
})

function load_mailbox(mailbox) {
    // show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#single-email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#compose-reply-view').style.display = 'none';

    // show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
    // initialise table
    const t_element = document.createElement('table');
    t_element.setAttribute('class', 'table table-dark');
    document.querySelector('#emails-view').append(t_element);

    const tb_element = document.createElement('tbody');
    t_element.appendChild(tb_element);

    if (mailbox === 'inbox') {
        var promise = fetch_data(API_URL + '/emails/inbox');
    } else if (mailbox === 'sent') {
        var promise = fetch_data(API_URL + '/emails/sent');
    } else if (mailbox === 'archive') {
        var promise = fetch_data(API_URL + '/emails/archive');
    }

    promise.then(data => {
        var emails = data;
        emails.forEach(email => {
                if (mailbox === 'sent' && email['archived'] === true) {
                    return;
                }

                const tb_element = document.createElement('tbody');
                tb_element.setAttribute('id', email['id']);
                if (email['read'])                
                    tb_element.setAttribute('class', 'read');

                t_element.appendChild(tb_element);
                // view an email
                tb_element.addEventListener('click', () => {
                    if (!(email['read'])) {
                        mark_read(email['id']);
                    }
                    show_email(email);
                });
                
            INBOX_COLUMNS.forEach(inbox_column => {
                const td_element = document.createElement('td');
                if (inbox_column === 'sender') {
                    td_element.innerHTML = `<span><i class="fas fa-archive"></i></span> ${email[inbox_column]}`;
                    if (mailbox === 'archive') {
                        td_element.innerHTML = `<span><i class="fas fa-archive archived"></i></span> ${email[inbox_column]}`;
                    }
                    if (mailbox === 'sent') {
                        td_element.innerHTML = `<span><i class="fas fa-archive"></i></span> To: ${email[inbox_column]}`;
                    }
                }

                if (inbox_column === 'body') {
                    if (email[inbox_column].length >= 50) {
                        td_element.innerHTML = `${email[inbox_column].slice(0,80)}...`;
                    } else {
                        td_element.innerHTML = email[inbox_column];
                    }
                }
                
                if (inbox_column === 'timestamp') {
                    td_element.innerHTML = email[inbox_column];
                }
                tb_element.appendChild(td_element);
            })
        })

        // make icons clickable
        const icons = document.querySelectorAll('.fas');
        icons.forEach(icon => {
            icon.addEventListener('click', (event) => {
                event.stopPropagation();
                const id = icon.closest('tbody').id;
                if (icon.classList.contains('archived')) {
                    mark_archive_status(id, false);
                    icon.setAttribute('class', 'fas fa-archive');
                } else {
                    mark_archive_status(id, true);
                    icon.setAttribute('class', 'fas fa-archive archived');
                }
            })
        })
    }) 
    
}

const get_form_data = (element) => {
    const form_element = element;
    const recipients = form_element[1].value;
    const subject = form_element[2].value;
    const body = form_element[3].value;
    const data = {
        'recipients': recipients,
        'subject': subject,
        'body': body
    }
    return data
};

const send_mail = data => {
    fetch(API_URL + '/emails', {
        method: 'POST',
        body: JSON.stringify({
            recipients: data['subject'],
            subject: data['subject'],
            body: data['body']
            })
        })

    .then(response => response.json())
    .catch(error => {
        console.log('error: ', error)
    })
};

const show_email = data => {
    console.log(data)
    document.querySelector('#emails-view').style.display = 'none';
    empty_element('#single-email-view');
    document.querySelector('#single-email-view').style.display = 'block';

    const container_element = document.createElement('div');
    container_element.setAttribute('class', 'container');
    document.querySelector('#single-email-view').append(container_element);

    // container 1 
    const subject_container_element = document.createElement('div');
    subject_container_element.setAttribute('class', 'subject-container');

    subject_container_element.innerHTML = `<p><b>From:</b> ${data['sender']}</p>
                                            <p><b>To:</b> ${display_recipients(data['recipients'])}</p>
                                            <p><b>Subject: </b>${data['subject']}</p>
                                            <p><b>Timestamp: </b>${data['timestamp']}</p>
                                            <button class="btn btn-sm btn-outline-primary" id="reply">Reply</button>
                                            <hr>`;

    container_element.append(subject_container_element);

    const reply_btn = document.querySelector('#reply');
    reply_btn.addEventListener('click', () => {
        compose_reply_email(data);
    })
    
    const user = document.querySelector('h2').innerHTML
    if (data['recipients'].length === 1 && user in data['recipients']) {
        document.querySelectorAll('p')[1].innerHTML = '<p><b>To:</b> me</p>';
    }

    // container 2
    const body_container_element = document.createElement('div');
    body_container_element.setAttribute('class', 'body-container');
    container_element.append(body_container_element);
    body_container_element.innerHTML = data['body'];
    container_element.appendChild(body_container_element); }

const fetch_data = async (api_url) => {
    const response = await fetch(api_url);
    const data = await response.json();
    return data;
}

// TODO: async?
const mark_read = async (id) => {
    fetch(`${API_URL}/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
      .then(response => response.json())
      .then(result => {
        console.log('Success:', result);
      })
      .catch(error => {
        console.error('Error:', error);
      });
}

const mark_archive_status = async (id, status) => {
    fetch(`${API_URL}/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: status
        })
      })
      .then(response => response.json())
      .then(result => {
        console.log('Success:', result);
      })
      .catch(error => {
        console.error('Error:', error);
      });
}

const empty_element = (attribute_value) => {
    document.querySelector(attribute_value).innerHTML = '';
}

const display_recipients = (recipients) => {
    let output = '';
    recipients.forEach(recipient => {

        output += `${recipient}, `;
    })
    return output.slice(0, output.length-2);
}