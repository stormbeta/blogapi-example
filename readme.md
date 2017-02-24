#Blog Post API Example Project

[![Build Status](https://travis-ci.org/stormbeta/blogapi-example.svg?branch=master)](https://travis-ci.org/stormbeta/blogapi-example)

Minimalist API example with Flask

##Requirements:

* Development
    * Python 3.6
    * Docker 1.10+

* Deployment
    * TODO

## Getting started

TODO: Port python setup wrapper script to something I can open source

### Virtualenv setup

```bash
virtualenv .virtualenv --python=python3.6
source .virtualenv/bin/activate
pip install -r requirements.txt
```

### Run tests

`python app_test.py`

### Docker run (local)

Run app on localhost:8080
`docker-compose build --pull && docker-compose run --rm blogapi`

##Notes:

I chose to use Python because I wanted to learn more about its ecosystem,
and until now I'd only used it for simple tiny scripts and automation. I
also have more confidence in Python working "out of the box" on other machines
than ecosystems with greater instability such as node.js.

Originally I wanted to use OpenAPI Spec (aka Swagger) to automatically define the API, but
ran into snags with some of the supporting frameworks and decided to just use plain Flask.
I've left the spec file in place though for reference, and in a real project I'd want to use
it to validate the API.
