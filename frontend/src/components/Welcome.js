import React from 'react';
import { Jumbotron, Button } from 'react-bootstrap';

const Welcome = () => {
  return (
    <div className="jumbotron">
      <h1 className="display-4">Images Gallery</h1>
      <p className="lead">
        {' '}
        This is a simple application that retrieves images from the Unsplash
        API.
      </p>

      <p>In order to use it please enter e asearch term.</p>
      <p className="lead">
        <a
          className="btn btn-primary btn-lg"
          href="https://unsplash.com"
          role="button"
          target="_blank"
          rel="noreferrer"
        >
          Learn more
        </a>
      </p>
    </div>
  );
};

export default Welcome;
