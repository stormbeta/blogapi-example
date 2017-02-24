#!/usr/bin/env python3

import os
import flask

class BlogAPI:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.log = self.app.logger

        self.app.config.update(dict(
            DATABASE=os.path.join(self.app.root_path, 'blog.db'),
            PORT=8080,
        ))

        @self.app.route("/post", methods=['POST'])
        def add_post():
            return "POST"

        @self.app.route("/posts", methods=['GET'])
        def get_posts():
            return "GET"


if __name__ == '__main__':
    api = BlogAPI()
    api.app.run(port=8080)
