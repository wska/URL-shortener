# URL-shortener
A small URL shortener as a assignment for an internship program.

# Implementation specifications:
The URL shortener was developed using Python 3.6, Flask 1.0.2 & gunicorn 19.9.0, and Sqlite3, which is included by default in Python3.
The URL shortening algorithm is done by using base 62 encoding (covered by the regular expression [a-zA-Z0-9]). 
Flask was used to develop the actual HTTP web server and the endpoints for the URL Shortener. I choose to use Sqlite3 and a database implementation, despite there not being strict requirement for the application to persist in its state after server shutdown.
While Flask is an excellent libary to quickly get a HTTP API up and running, the default development server is not meant for production deloyment. However,
there are plenty of WSGI server options to choose from that can handle Flask applications out of the box. For this project, I have chosen to use Green Unicorn WSGI HTTP Server, or just "gunicorn".


# Instructions

These required modules can be installed using the packet manager for Python3, pip3. I would advise to first create a virtual environment in order to isolate the application first. Python3 has a virtual environment as part of its dev-package: venv. 

The modules required can be aquired by performing:

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
Afterwards, it calls the gunicorn module to launch the flask application in the main app file, which is urlshortener.py. The additional parameters includes the number of workers that procecces incoming HTTP requests, and the host adress used in addition to the port number.
```
gunicorn -w 4 urlshortener:app
```
The server then starts with 4 synchronous workers, on the default gunicorn listening address, whih is the localhost address 127.0.0.1, on port number 8000.  

Executing the file init.py will wipe the content of the current database.