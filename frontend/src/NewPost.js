import React, { useState } from "react";

import "./NemPost.css";

const BASE_URL = "http://localhost:8000/";

function NewPost() {
  const [image, setImage] = useState(null);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [creator, setCreator] = useState("");

  const handleImageUpload = (e) => {
    if (e.target.files[0]) {
      setImage(e.target.files[0]);
    }
  };

  const handleCreate = (e) => {
    e?.preventDefault();

    const formData = new FormData();
    formData.append("image", image);

    const requestOptions = {
      method: "POST",
      body: formData,
    };

    fetch(BASE_URL + "posts/image", requestOptions)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response
      })
      .then((data) => {
        console.log(data.filename);
        createPost(data.filename);
      })
      .catch((error) => {
        console.log(error);
        alert(error);
      })
      .finally(() => {
        setImage(null);
        document.getElementById("image_input").value = null;
      });
  };

  const createPost = (imageUrl) => {
    const json_string = JSON.stringify({
      image_url: imageUrl,
      title: title,
      content: content,
      creator: creator,
    });

    const requestOptions = {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
      body: json_string,
    };

    fetch(BASE_URL + "posts", requestOptions)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        window.location.reload();
        window.scrollTo(0, 0);
      })
      .catch((error) => {
        console.log(error);
        console.log("hello world!");
        // alert(error)
      });
  };

  return (
    <div className="newpost">
      <div className="newpost_el image_box">
        <label htmlFor="image_input" className="newpost_file_label">
          Upload Image
        </label>
        <input
          className="newpost_input"
          type="file"
          id="image_input"
          name="image"
          onChange={handleImageUpload}
          placeholder="upload image"
        />
      </div>

      <div className="newpost_el">
        <input
          className="newpost_input"
          id="creator_input"
          type="text"
          name="creator"
          placeholder="Creator"
          onChange={(e) => setCreator(e.target.value)}
          value={creator}
        />
      </div>

      <div className="newpost_el">
        <input
          className="newpost_input"
          id="title_input"
          placeholder="Title"
          type="text"
          name="title"
          onChange={(e) => setTitle(e.target.value)}
          value={title}
        ></input>
      </div>

      <div className="newpost_el">
        <textarea
          className="newpost_input"
          rows="10"
          id="content_input"
          placeholder="Content"
          name="content"
          onChange={(e) => setContent(e.target.value)}
          value={content}
        ></textarea>
      </div>

      <div className="newpost_el">
        <button onClick={handleCreate}>Create Post</button>
      </div>
    </div>
  );
}

export default NewPost;
