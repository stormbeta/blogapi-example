#Blog Post API Example Project

Minimalist API example with Flask

##TODO:

* Figure out how to write unit tests through flask
* setup.py, virtualenv, and other python project config
* Docker compose deployment (make sure to use a volume for the db file so it's persistent)
* Deployment documentation

## Run tests

`python app_test.py`

## Docker run (local)

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
