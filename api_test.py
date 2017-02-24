import flask
import unittest
import tempfile
import json
import os
import app as blog


class BlogAPITest(unittest.TestCase):
    def setUp(self):
        self.blog = blog
        self.db, self.blog.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = self.blog.app.test_client()
        with self.blog.app.app_context():
            with self.blog.app.open_resource("init.sql", mode='r') as f:
                self.blog.get_db().cursor().executescript(f.read())

    def tearDown(self):
        os.close(self.db)

    def test_empty(self):
        resp = self.app.get('/posts')  # type: flask.Response
        assert resp.status_code == 200
        assert json.loads(resp.data) == []

    def test_add(self):
        resp = self.app.post('/post', data=json.dumps(dict(
            post_id="1",
            title="Hello world!",
            body="lorem ipsum"
        )))  # type: flask.Response
        assert resp.status_code == 201
        data = self.app.get('/posts').data
        result = json.loads(data)
        assert result == [{"post_id": "1", "title": "Hello world!", "body": "lorem ipsum"}]


if __name__ == '__main__':
    unittest.main()
