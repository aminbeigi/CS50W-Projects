import React from 'react'
import { Card } from 'react-bootstrap';

export const Post = ({id, title, body, user, timestamp, onDeletePost}) => {
    const deleteData = () => {
        fetch('http://localhost:8000' + '/posts' + `/${id}`, {
            method: 'DELETE',
        })
            .then(response => response.json())
            .then(response => {
                console.log(response);
                onDeletePost();
            })
            .catch((error) => {
                console.error('Error:', error);
            });  
    }
    
    const returnDeletePostBtn = () => {
        if (onDeletePost) {
            return (
                    <button onClick={() => deleteData(id)} type="button" class="btn btn-danger">Delete</button>
                )
            }
        }

    return (
        <section>
            <Card>
                <Card.Body>
                    <Card.Title>{title}</Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">by {user}</Card.Subtitle>
                    <Card.Text>{body}</Card.Text>
                    <Card.Subtitle className="mb-2 text-muted">{timestamp}</Card.Subtitle>
                    {returnDeletePostBtn()}
               </Card.Body>
            </Card>
        </section>
    )
}

Post.defaultProps = {
    key: null,
    title: "No title",
    body: "No body",
    user: "No user",
    timestamp: "No timestamp",
    deletePost: false
}