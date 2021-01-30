import { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import 'bootstrap/dist/css/bootstrap.min.css';

import { Button, Breadcrumb, Card, Container } from 'react-bootstrap'

const API_URL = 'http://localhost:8000';

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
        .then(response => response.json())
        .then(response => console.log(response))
        .catch(() => console.log(`Can't access ${API_URL + endpoint} response.`))
}

const CreateNewPost = () => {
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

class Index extends Component {
    state = {
        data: [],
        loading: false
    }

    componentDidMount() {
        console.log("The component is now mounted!")
        this.setState({loading: true})
        fetch(API_URL + '/posts')
            .then(response => response.json())
            .then(response => this.setState({data: response, loading: false}))
            .catch(() => console.log(`Can't access ${API_URL + '/posts'} response.`))
    }

    componentDidUpdate() {
        console.log("The component just updated")
    }

    render() {
        return (
            <div>
                <NavBar />

                <Container>
                    <br></br>
                    <CreateNewPost />
                    <br></br>
                    <h1>All Posts</h1>
                    {this.loading
                        ? "loading..."
                        : <div>
                            {this.state.data.map(post => {
                                return(
                                    <div>
                                        <Post title={post['title']} body={post['body']} user={post['user']} timestamp={post['timestamp']} />
                                    </div>
                                )
                            })}
                        </div>
                    }
                </Container>
            </div>
        )
    }
}

ReactDOM.render(
    <Index />,
    document.getElementById('root')
);