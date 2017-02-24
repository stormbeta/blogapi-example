#!/usr/bin/env python3

import os
import flask
import sqlite3
from flask import request
import json


class BlogAPI:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.log = self.app.logger

        self.app.config.update(dict(
            DATABASE=os.path.join(self.app.root_path, 'blog.db'),
            PORT=8080,
        ))

        self.context = self.app.app_context().g
        self.app.add_url_rule("/post", view_func=self.add_post, methods=['POST'])
        self.app.add_url_rule("/posts", view_func=self.get_posts(), methods=['GET'])

    def get_posts(self):
        c = self.get_db().cursor()
        return json.dumps({list(c.execute("SELECT * FROM posts"))}), 200

    def add_post(self):
        c = self.get_db().cursor()
        data = json.loads(request.data)  # TODO: How does flask populate this?
        c.execute("INSERT INTO posts (post_id, title, body) VALUES (?, ?, ?)",
                  (data["post_id"], data["title"], data["body"]))
        self.log.info("Created post '" + data["title"] + "'")
        return '', 201

    def get_db(self):
        if not hasattr(self.context, 'blog_db'):
            self.context.blog_db = sqlite3.connect(self.app.config['DATABASE'])
        return self.context.blog_db


if __name__ == '__main__':
    api = BlogAPI()
    api.app.run(port=8080)
