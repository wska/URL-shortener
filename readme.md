# URL-shortener
A small URL shortener using Python, Flask, gunicorn, Sqlite3 and a bit of Boostrap. 

# Implementation specifications:
The URL shortener was developed using Python 3.6, Flask 1.0.2 & gunicorn 19.9.0, and Sqlite3, which is included by default in Python3.
The URL shortening algorithm is done by using base 62 encoding (covered by the regular expression [a-zA-Z0-9]).
Flask was used to develop the RESTful HTTP web server and the endpoints for the URL Shortener. I choose to use Sqlite3 and a database implementation, which allows the state of the application to persist even after being shut down.
While Flask is an excellent library to quickly get a HTTP server up and running, the default development server is not meant for production deployment. However,
there are plenty of WSGI server options to choose from that can handle Flask applications out of the box. For this project, I have chosen to use Green Unicorn WSGI HTTP Server, or just "gunicorn".


# Instructions

The required modules can be installed using the packet manager for Python3, pip3. I would advise to first create a virtual environment in order to isolate the application. Python3 has a virtual environment as part of its dev-package: venv.

The modules required can be acquired by performing:

```
pip3 install gunicorn
pip3 install Flask
```

or you can use the provided requirements.txt file using:

```
pip3 install -r requirements.txt
```



To start the server, one can either use the shell script provided or the instructions below it.
Using the shell script:
```
sh start.sh
```

The shell script executes two commands. The first one calls the init.py file which creates the database(if not present) and adds the required schema.
```
python3 init.py
```
Afterwards, it calls the gunicorn module to launch the flask application in the main app file, which is urlshortener.py. The additional parameter is the number of workers that processes incoming HTTP requests. Typically you want to use a workers equivalent to the number of cores in the CPU.
```
gunicorn -w 4 urlshortener:app
```
The server then starts with 4 synchronous workers, on the default gunicorn listening address, which is the localhost address 127.0.0.1, on port number 8000. 

Executing the file will create a database if absent. There is also a function inside of init.py for wiping the current state of the database.

# Using the application
In order to test the application, one can either visit the designated port number on the localhost IP address: http://localhost:8000/
One will be greeted by a basic HTML page that has a form that can be filled in. Once a form is submitted, it will return the content with a shortened URL that follows the http://localhost in addition to a base62 shortened url. The link can then be used to be redirected to the original URL.

One can also create a POST request, for example using the request module for python3:

```
import requests
requests.post('http://localhost:8000/', data= {'url': url})
```
Where the url variable is some arbitrary URL, will return the corresponding html object as a response.

# Testing
I created some unittests to evaluate some of the core functionality of the application. The unittest asserts the correctness of the base conversions, and also performs a number of POST requests and validates the response code of the response object. It also stress-tests the server by sending 400 requests in parallel on all available CPUs.
The unittest can be executed by running the test file:
```
python3 test.py
```


