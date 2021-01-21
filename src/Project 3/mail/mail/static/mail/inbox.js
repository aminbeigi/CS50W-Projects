const API_URL = 'http://localhost:8000'
const INBOX_CATEGORIES = ['sender', 'body', 'timestamp']

document.addEventListener('DOMContentLoaded', function() {
    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);
    
    // By default, load the inbox
    load_mailbox('inbox');
});

function compose_email() {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#single-email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
  
    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';

    const element = document.getElementsByClassName('btn btn-primary')[0];
    element.addEventListener('click', () => {
        send_mail(get_form_data());
    });
}

function load_mailbox(mailbox) {
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#single-email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    if (mailbox === 'inbox') {
        const t_element = document.createElement('table');
        t_element.setAttribute('class', 'table table-sm table-dark');
        document.querySelector('#emails-view').append(t_element);

        const tb_element = document.createElement('tbody');
        t_element.appendChild(tb_element);

        const promise = fetch_data(API_URL + '/emails/inbox');
        promise.then(data => {
            if (data !== undefined) {
                data.forEach(email => {
                        const tb_element = document.createElement('tbody');
                        tb_element.setAttribute('id', email['id']);
                        t_element.appendChild(tb_element);
                        // show an email
                        tb_element.addEventListener('click', () => {
                            show_email(email);
                        });
                        
                    for (col = 0; col < 3; ++col) {
                        const category = INBOX_CATEGORIES[col]; 
                        const td_element = document.createElement('td');
                        if (category === 'sender') {
                            td_element.innerHTML = email[category];
                        }

                        if (category === 'body') {
                            if (email[category].length >= 50) {
                                td_element.innerHTML = `${email[category].slice(0,50)}...`;
                            } else {
                                td_element.innerHTML = email[category];
                            }
                        }
                        
                        if (category === 'timestamp') {
                            td_element.innerHTML = email[category];
                        }
                        tb_element.appendChild(td_element);
                    }
                })
            }
        }) 

    }
}

const get_form_data = () => {
    const form_element = document.querySelector('form'); const recipients = form_element[1].value;
       const subject = form_element[2].value;
    const body = form_element[3].value;
    const data = {
        'recipients': recipients,
        'subject': subject,
        'body': body
    }
    return data
};

const send_mail = (data) => {
    fetch(API_URL + '/emails', {
        method: 'POST',
        body: JSON.stringify(data
    )
      })
      .then(response => response.json())
    };

const show_email = data => {
    document.querySelector('#emails-view').style.display = 'none';
    // TODO: make func that empties email view
    document.querySelector('#single-email-view').remove();
    document.querySelector('#single-email-view').style.display = 'block';


    const container_element = document.createElement('div');
    container_element.setAttribute('class', 'container');
    document.querySelector('#single-email-view').append(container_element);

    const subject_container_element = document.createElement('div');
    subject_container_element.setAttribute('class', 'container');
    container_element.append(subject_container_element);
    const subject_element = document.createElement('p');
    subject_element.innerHTML = `<h3>${data['subject']}</h3>`;
    subject_container_element.appendChild(subject_element);
    
    const body_container_element = document.createElement('div');
    body_container_element.setAttribute('class', 'body-container');
    container_element.append(body_container_element);
    const body_element = document.createElement('p');
    body_element.innerHTML = data['body'];
    body_container_element.appendChild(body_element);
    
}

const fetch_data = async (api_url) => {
    const response = await fetch(api_url);
    const data = await response.json();
    return data;
}