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

document.addEventListener('DOMContentLoaded', () => {
    const element = document.getElementsByClassName('btn btn-primary')[0];
    element.addEventListener('click', () => {
        console.log("I've been clicked!")
    });
});

function compose_email() {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
  
    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}

const get_form_data = () => {
    const submit_btn = document.querySelectorAll('input');
    const form_element = document.querySelector('form');
    const recipients = form_element[1].value;
    const subject = form_element[2].value;
    const body = form_element[3].value;
    console.log('submit_btn');
};