const API_URL = 'http://localhost:8000/emails'

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
        const table_element = document.createElement('table');
        table_element.setAttribute('class', 'table table-sm table-dark');
        document.querySelector('#emails-view').append(table_element);

        const table_body_element = document.createElement('tbody');
        table_element.appendChild(table_body_element);

        const table_row_element = document.createElement('tr');
        table_body_element.appendChild(table_row_element);

        const array =  ['test', 'test2', 'test3'];

        array.forEach((i) => {
            const table_data_element = document.createElement('td');
            table_data_element.innerHTML = i;
            table_body_element.appendChild(table_data_element);
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
    fetch(API_URL, {
        method: 'POST',
        body: JSON.stringify(data
    )
      })
      .then(response => response.json())
    };

const get_data = (api_url) => {
    fetch(api_url)
        .then(reponse => response.json())  
        .then(() => {
            return data;
        })
        .catch((error) => {
            console.error("Fetch error: ", error);
        });
}