# URL-shortener
A project that acts as a URL shortener

# Implementation specifications:
TODO
While Flask is an excellent libary to quickly get a HTTP API up and running, the default development server is synchronous, and thus not suitable for production.
There are plenty of WSGI server options to choose from that can handle Flask applications. For this project, I have chosen to use Green Unicorn WSGI HTTP Server, or just "gunicorn".

```
pip3 install gunicorn
pip3 install Flask
```

gunicorn3 (Green Unicorn WSGI HTTP Server)



# Starting the server
To start the server, one calls the gunicorn3 module with parameter specifications.


Say we want to start the server using 4 workers to use the localhost IP address with port 5000:

```
gunicorn3 -w 4 -b 127.0.0.1:5000 main:app
```
The server then starts with 4 synchronous workers. 