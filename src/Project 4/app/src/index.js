import { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import 'bootstrap/dist/css/bootstrap.min.css';

import { Button, Breadcrumb, Card, Container } from 'react-bootstrap';

const API_URL = 'http://localhost:8000';
const PAGE_POST_LIMIT = 5;

const postData = e => {
    const title = e.target[0].value;
    const body = e.target[1].value;
    const data = {
        'user': 'George',
        'title': title,
        'body': body,
    }
    console.log(data);
    
    fetch(API_URL + '/create-post', {
        method: 'POST',
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });    

    e.target[0].value = '';
    e.target[1].value = '';
    e.preventDefault();
}

const CreateNewPost = () => {
    return (
        <section>
            <Card>
            <Card.Header as="h5">Create new post</Card.Header>
                <Card.Body>
                    <form onSubmit={postData}>
                        <Card.Title>title: <input type="text"></input></Card.Title>
                        <Card.Text>Body: <textarea rows="4" cols="40"></textarea></Card.Text>
                        <Button type="submit" variant="primary" >Post</Button>
                    </form>
                </Card.Body>
            </Card>
        </section>
    )
}
const Post = ({title, body, user, timestamp}) => {
    return (
        <section>
            <Card>
                <Card.Body>
                    <Card.Title>{title}</Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">by {user}</Card.Subtitle>
                    <Card.Text>{body}</Card.Text>
                    <Card.Subtitle className="mb-2 text-muted">{timestamp}</Card.Subtitle>
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

const Index = () => {
    const [state, setState] = useState({
        data: [],
        loading: false,
        }
    )

    useEffect(() => {
        console.log("The component is now mounted!")
        setState({loading: true})
        fetch(API_URL + '/posts')
            .then(response => response.json())
            .then(response => setState({data: response, loading: false}))
            .catch(() => console.log(`Can't access ${API_URL + '/posts'} response.`))
    }, [])

        return (
            <div>
                <NavBar />
                <Container>
                    <br></br>
                    <CreateNewPost />
                    <br></br>
                    <h1>All Posts</h1>
                    {state.loading
                        ? "loading..."
                        : <div>
                            {state.data.map((post, i) => {
                                return(
                                    <div key={i}>
                                        <Post key={i} title={post['title']} body={post['body']} user={post['user']} timestamp={post['timestamp']} />
                                    </div>
                                )
                            })}
                        </div>
                    }
                </Container>
            </div>
        )
    }


ReactDOM.render(
    <Index />,
    document.getElementById('root')
);