import os
import sqlite3
from flask import request, g, Flask
import json

app = Flask(__name__)
log = app.logger

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'blog.db'),
    PORT=8080,
))

@app.route("/posts", methods=['GET'])
def get_posts():
    c = get_db().cursor()
    data = c.execute("SELECT * FROM posts")
    keys = [i[0] for i in c.description]
    mapped_result = [dict(zip(keys, values)) for values in data]
    return json.dumps(mapped_result), 200


@app.route("/post", methods=["POST"])
def add_post():
    db = get_db()
    data = json.loads(request.data)  # TODO: How does flask populate this?
    db.cursor().execute("INSERT INTO posts (post_id, title, body) VALUES (?, ?, ?)",
              (data["post_id"], data["title"], data["body"]))
    db.commit()
    log.info("Created post '" + data["title"] + "'")
    return '', 201


def get_db():  # type: sqlite3.Connection
    if not hasattr(g, 'blog_db'):
        g.blog_db = sqlite3.connect(app.config['DATABASE'])
        g.blog_db.row_factory = sqlite3.Row
    return g.blog_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'blog_db'):
        g.blog_db.close()


if __name__ == '__main__':
    app.run(port=8080)
