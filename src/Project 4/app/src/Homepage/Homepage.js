import { useState, useEffect } from 'react';
import '../index.css';

import 'bootstrap/dist/css/bootstrap.min.css';

import {Container} from 'react-bootstrap';
import * as serviceWorker from '../serviceWorker';

import { NavBar } from '../shared/components/NavBar/NavBar'
import { CreateNewPost } from '../shared/components/CreateNewPost/CreateNewPost'
import { Post } from '../shared/components/Post/Post'

export const Homepage = () => {
    const postIncrement = 3;

    const [state, setState] = useState({
        data: [],
        loading: false,
        currentPostCount: 0
        }
    )

    const handleScroll = () => {
        const atBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight
        if (atBottom) {
            console.log("we at bottom boys");
        }
    }

    const fetchData = () => {
        fetch('http://localhost:8000' + '/posts')
           .then(response => response.json())
           .then(response => setState({data: response, loading: false}))
           .catch(() => console.log(`Can't access ${'http://localhost:8000' + '/posts'} response.`))       
    }

    useEffect(() => {
        console.log("The component is now mounted!");
        document.addEventListener('scroll', handleScroll);
        fetchData();
        return () => {
            window.removeEventListener('scroll', handleScroll);
        }
    }, []);

        return (
            <div>
                <NavBar currentPage="home"/>
                <Container>
                    <br></br>
                    <CreateNewPost onCreatePost={fetchData}/>
                    <br></br>
                    <h1>All Posts</h1>
                    {state.loading
                        ? "loading..."
                        : <div>
                            {state.data.map(post => {
                                return (
                                    <div key={post.id}>
                                        { post.user === 'George' 
                                            // TODO: add edit post feature PUT request
                                            ? <Post id={post.id} title={post.title} body={post.body} user={post.user} timestamp={post.timestamp} onDeletePost={fetchData} />
                                            : <Post id={post.id} title={post.title} body={post.body} user={post.user} timestamp={post.timestamp} />
                                        } 
                                    </div>
                                )
                            })}
                        </div>
                    }
                </Container>
            </div>
        )
    }

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();