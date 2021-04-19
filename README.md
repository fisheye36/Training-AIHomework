# Description

This project contains a simple microservices-based web application written in Python with Flask-RESTPlus library. It is
fully dockerized, meaning that it is possible to run independent microservices as Docker containers, as well as using
Docker Compose to start both services together, allowing them to communicate.

# Project layout

Each subdirectory houses independent Python projects, ready to be dockerized or run locally. It is advised to create one
Python virtual environment for one subproject, which is why there are also 3 different `requirements.txt` files.

`tests` subdirectory contains integration tests for the entire application. Be sure to grab a cup of coffee when running
those - it may take a huge amount of time to complete :)

# Running

## PingService

To run locally (in a virtual environment):

```shell
cd ping-service
pip install -U pip setuptools
pip install -r requirements.txt
gunicorn service:app
```

Then navigate to http://localhost:8000 to see Swagger API documentation.

To use Docker:

```shell
docker build -t ping-service .
docker run -dp 8000:8000 ping-service
```

Then navigate to the same URL.

## ReceiverService

As above, though remember to change image tag during build process (and directory).

## Tests

First, setup your environment:

```shell
cd tests
pip install -U pip setuptools
pip install -r requirements.txt
```

Then, run the tests using `pytest`:

```shell
pytest
```

# Room for improvements

Swagger documentation is partially done, and it could always be improved. Personally, I prefer
[FastApi](https://fastapi.tiangolo.com/) library for developing REST APIs in Python, since it has very good integration
with Swagger, as well as out of the box request/response data validation: JSON, query strings, required headers, cookies
etc. It does not bloat code with huge number of decorators, instead it uses Python annotations to do the heavy lifting -
I highly recommend checking the library out!
