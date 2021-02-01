import React from 'react'
import { Breadcrumb} from 'react-bootstrap';

export const NavBar = ({currentPage}) => {
    const renderPage = () => {
        if (currentPage === 'home') {
            return (
                <Breadcrumb>
                    <Breadcrumb.Item active>Home</Breadcrumb.Item>
                    <Breadcrumb.Item href="/my-posts">My Posts</Breadcrumb.Item>
                </Breadcrumb>
            )
        }

        if (currentPage === 'myPosts') {
             return (
                <Breadcrumb>
                    <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                    <Breadcrumb.Item active>My Posts</Breadcrumb.Item>
                </Breadcrumb>
            )           
        }
    }

    return (
        <div>
            {renderPage()}
        </div>
    )
}

NavBar.defaultProps = {
    currentPage: 'home'
}