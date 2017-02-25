#Blog Post API Example Project

[![Build Status](https://travis-ci.org/stormbeta/blogapi-example.svg?branch=master)](https://travis-ci.org/stormbeta/blogapi-example)

Minimalist API example with Flask

##Requirements:

* Python 2.7+/3.4+
* Docker 1.10+

## Getting started

### Virtualenv setup

```bash
virtualenv .virtualenv --python=python3
source .virtualenv/bin/activate
pip install -r requirements.txt
```

### Run tests

`python app_test.py`

### Running (local)

Run app on localhost:8080

`docker-compose build --pull && docker-compose run --rm blogapi`

Or run directly:

`python app.py`

### Example

```bash
$ curl -X POST -H "Content-Type: application/json" http://localhost:8080/post -d '{"post_id": "12", "title": "hello", "body": "lorem ipsum"}' -w '%{http_code}'
201
$ curl -X GET http://localhost:8080/posts
[{"body": "lorem ipsum", "post_id": "12", "title": "hello"}]
```

## Deployment

Travis automatically runs the unit tests on pushes to master

The docker container should be deployable to any docker-based infrastructure, and can be ran as a background service via compose manually:

`docker-compose run -d -p 8080:8080 blogapi`

In a real-world service, I'd want to front it with nginx for TLS/HTTPS, and
setup something like a Kubernetes cluster to deploy it into. The database
would run as a separate container with a persistent volume mount instead of
just being a local file

##Notes:

I chose to use Python because I wanted to learn more about its ecosystem,
and until now I'd only used it for simple tiny scripts and automation. I
also have more confidence in Python working "out of the box" on other machines
than ecosystems with greater instability such as node.js.

Originally I wanted to use OpenAPI Spec (aka Swagger) to automatically define the API, but
ran into snags with some of the supporting frameworks and decided to just use plain Flask.
I've left the spec file in place though for reference, and in a real project I'd want to use
it to validate the API.

TODO: Port python setup wrapper script to something I can open source
