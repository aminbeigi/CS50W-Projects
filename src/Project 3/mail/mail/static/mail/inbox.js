const API_URL = 'http://localhost:8000'
const INBOX_CONTENTS = ['sender', 'body', 'timestamp']

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
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    if (mailbox === 'inbox') {
        const t_element = document.createElement('table');
        t_element.setAttribute('class', 'table table-sm table-dark');
        document.querySelector('#emails-view').append(t_element);

        const tb_element = document.createElement('tbody');
        t_element.appendChild(tb_element);

        const tr_element = document.createElement('tr');
        tb_element.appendChild(tr_element);

        const promise = fetch_data(API_URL + '/emails/inbox');
        promise.then(data => {
            if (data !== undefined) {
                data.forEach(email => {
                    for (col = 0; col < 3; ++col) {
                        const td_element = document.createElement('td');
                        td_element.innerHTML = email[INBOX_CONTENTS[col]];
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

const get_data2 = (api_url) => {
    return fetch(API_URL + '/emails/inbox')
        .then(response => response.json())  
        .then(data => {
            return data;
        })
        .catch((error) => {
            console.error("Fetch error: ", error);
        });
}

const fetch_data = async (api_url) => {
    const response = await fetch(api_url);
    const data = await response.json();
    return data;
}