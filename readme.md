#Blog Post API Example Project

Minimalist API example, demonstrates the use of the OpenAPI Spec
(formerly known as swagger) to programmatically describe the API.

##TODO:

* Figure out how to write unit tests through connexion/flask
* Implement REST endpoints
* setup.py, virtualenv, and other python project config
* Docker compose deployment (make sure to use a volume for the db file so it's persistent)
* Deployment documentation

## Docker run (local)

TODO: Replace with docker-compose.yml file
`docker build --pull . -t blogapp && docker run -p 5000:5000 --rm -it blogapp`

##Notes:

I chose to use Python because I wanted to learn more about its ecosystem,
and until now I'd only used it for simple tiny scripts and automation. I
also have more confidence in Python working "out of the box" on other machines
than ecosystems with greater instability such as node.js.

The OpenAPI spec was chosen because it provides a clean and cross-language
approach to programatically describing an API.

The connexion framework was chosen because it was the simplest way to
make use of the OpenAPI spec with Python, and includes useful extras like
a built-in endpoint for the generated API documentation.
