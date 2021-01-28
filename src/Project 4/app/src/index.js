import { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import 'bootstrap/dist/css/bootstrap.min.css';

import { Button, Breadcrumb } from 'react-bootstrap'

class Index extends Component {
    render() {
        return (
            <div>
                <div>
                    <Breadcrumb>
                        <Breadcrumb.Item active>Home</Breadcrumb.Item>
                        <Breadcrumb.Item href="#">All Posts</Breadcrumb.Item>
                    </Breadcrumb>
                </div>
                <div>
                    <h1>All Posts</h1>
                </div>
            </div>
        )
    }
}

ReactDOM.render(
    <Index />,
    document.getElementById('root')
);