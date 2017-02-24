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
        self.app.add_url_rule("/posts", view_func=self.get_posts, methods=['GET'])
        # self.app.teardown_appcontext_funcs.append(self.close_db)

    def get_posts(self):
        c = self.get_db().cursor()
        data = c.execute("SELECT * FROM posts")
        keys = [i[0] for i in c.description]
        mapped_result = [dict(zip(keys, values)) for values in data]
        return json.dumps(mapped_result), 200

    def add_post(self):
        db = self.get_db()
        data = json.loads(request.data)  # TODO: How does flask populate this?
        db.cursor().execute("INSERT INTO posts (post_id, title, body) VALUES (?, ?, ?)",
                  (data["post_id"], data["title"], data["body"]))
        db.commit()
        self.log.info("Created post '" + data["title"] + "'")
        return '', 201

    def get_db(self) -> sqlite3.Connection:
        if not hasattr(self.context, 'blog_db'):
            self.context.blog_db = sqlite3.connect(self.app.config['DATABASE'])
            self.context.blog_db.row_factory = sqlite3.Row
        return self.context.blog_db

    #TODO: Colled at the wrong time
    def close_db(self, error):
        if hasattr(self.context, 'blog_db'):
            self.context.blog_db.close()


if __name__ == '__main__':
    api = BlogAPI()
    api.app.run(port=8080)
