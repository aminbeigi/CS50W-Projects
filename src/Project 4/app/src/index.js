import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom"

import 'bootstrap/dist/css/bootstrap.min.css';

import { Homepage } from './Homepage/Homepage'
import { MyPostsPage } from './MyPostsPage/MyPostsPage'

import * as serviceWorker from './serviceWorker';

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={Homepage}></Route>
            <Route exact path="/my-posts" component={MyPostsPage}></Route>
        </Switch>
    </Router>,
    document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();