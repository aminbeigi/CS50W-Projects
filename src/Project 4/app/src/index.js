import { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import 'bootstrap/dist/css/bootstrap.min.css';

import { Button, Breadcrumb, Card, Container } from 'react-bootstrap'

const APIURL = 'http://localhost:8000';

const temp = e => {
    const title = e.target[0].value
    const body = e.target[1].value
    console.log(title)
    e.target[0].value = ''
    e.target[1].value = ''
    e.preventDefault();
}
const fetchData = (endpoint) => {
    fetch(API_URL + endpoint)
        .then(respose => response.json())
        .then(response => console.log(response))
}

const Post = () => {
    return (
        <section>
            <Card>
            <Card.Header as="h5">Create new post</Card.Header>
                <Card.Body>
                    <form onSubmit={temp}>
                    <Card.Title>title: <input type="text"></input></Card.Title>
                    <Card.Text>Body: <input type="text"></input></Card.Text>
                    <Button type="submit" variant="primary" >Post</Button>
                    </form>
                </Card.Body>
            </Card>
        </section>
    )
}
const Post = ({title, body}) => {
    return (
        <section>
            <Card>
                <Card.Body>
                    <Card.Title>{title}</Card.Title>
                    <Card.Text>{body}</Card.Text>
                </Card.Body>
            </Card>
        </section>
    )
}

const NavBar = () => {
    return (
        <div>
            <Breadcrumb>
                <Breadcrumb.Item active>Home</Breadcrumb.Item>
                <Breadcrumb.Item href="#">All Posts</Breadcrumb.Item>
            </Breadcrumb>
        </div>
    )
}

class Index extends Component {
    render() {
        return (
            <div>
                <NavBar />

                <Container>
                    <br></br>
                    <CreateNewPost />
                    <br></br>
                    <h1>All Posts</h1>
                    <Post title='titlkkkkkkkkkkkke' body='body'/>
                    <Post title='title2' body='body2'/>
                    <Post title='title3' body='body3'/>
                </Container>
            </div>
        )
    }
}

ReactDOM.render(
    <Index />,
    document.getElementById('root')
);