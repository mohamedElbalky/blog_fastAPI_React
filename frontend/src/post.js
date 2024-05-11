/* eslint-disable jsx-a11y/alt-text */

import React, {useState, useEffect} from "react";

import './post.css';


const BASE_URL = 'http://localhost:8000/';

function Post({post}) {
    const [imageUrl, setImageUrl] = useState('');

    useEffect(() => {
        setImageUrl(BASE_URL + post.image);
    }, [])


    const handleDelete = e => {
        e?.preventDefault();

        const requestOptions = {
            method: 'DELETE'
        }
        fetch(BASE_URL + 'posts/' + post.id, requestOptions)
        .then(response => {
            if (response.ok) {
                window.location.reload()
            }
            throw response
        })
        .catch(error => {
            console.log(error)
            // alert(error)
        })

    }



    return (
        <div className="post">
            <img className="post_image" src={imageUrl} />
            <div className="post_info">
                <div className="post_title">{post.title}</div>
                <div className="post_creator">by: <a href=".">{post.creator}</a></div>
                <div className="post_content">{post.content}</div>
                <div className="post_timestamp">{post.timestamp}</div>
                <div className="post_delete">
                    <button onClick={handleDelete}>Delete post</button>
                </div>
            </div>
        </div>
    )




}


export default Post;