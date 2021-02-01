import React from 'react'
import { Button, Card, Form } from 'react-bootstrap';

export const CreateNewPost = ({onCreatePost}) => {
    const postData = e => {
        const title = e.target[0].value;
        const body = e.target[1].value;
        
        const data = {
            'user': 'George',
            'title': title,
            'body': body,
        }

        fetch('http://localhost:8000' + '/posts', {
            method: 'POST',
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            if (onCreatePost) {
                onCreatePost()
            }

          })
          .catch((error) => {
            console.error('Error:', error);
          });    

        e.target[0].value = '';
        e.target[1].value = '';
        e.preventDefault();
    }

    return (
        <section>
            <Card>
            <Card.Header as="h5">Create new post</Card.Header>
                <Card.Body>
                    <Form onSubmit={postData}>
                        <Form.Group>
                            <Form.Control required size="lg" type="text" placeholder="title" />
                        </Form.Group>

                        <Form.Group controlId="exampleForm.ControlTextarea1">
                                <Form.Control required as="textarea" rows={3} placeholder="body"/>
                        </Form.Group>

                        <Button type="submit" variant="primary">Post</Button>
                    </Form>
                </Card.Body>
            </Card>
        </section>
    )
}