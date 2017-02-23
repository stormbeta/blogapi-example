#Blog Post API Example Project

Minimalist API example, demonstrates the use of the OpenAPI Spec
(formerly known as swagger) to programmatically describe the API.

##TODO:

* Figure out how to write unit tests through connexion/flask
* Implement REST endpoints
* setup.py and other python project config
* Docker setup to ensure this project can be ran regardless of local python version
* Deployment documentation

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
