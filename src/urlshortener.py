# William Skagerström - 23-04-2019

from flask import Flask, request, render_template, redirect
from sqlite3 import OperationalError
import string
import sqlite3
from baseconversion import base10, base62
from urllib.parse import urlparse



app = Flask(__name__)
hostAddress = 'http://localhost:8000/' # Change this to be in line with the IP/Port number that is used for the gunicorn server


# App method for index
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = str.encode(request.form.get('url'))
        if urlparse(original_url).scheme == '':
            url = 'http://' + original_url
        else:
            url = original_url

        with sqlite3.connect('links.db') as conn:
            
            cursor = conn.cursor()
            
            queryURL = cursor.execute('SELECT * FROM URL WHERE URL=?', [url]) # Checks if the URL has already been shortened
            databaseEntry = queryURL.fetchone()
            
            if databaseEntry is not None: # If not none, return the already existing shortened URL in the database

                indexToBase62 = base62(databaseEntry[0]) # Converts the entry index in the database to base 62 and uses it as the shortened URL

                return render_template('index.html', shortenedUrl=hostAddress+str(indexToBase62)) # Render template fetches the HTML file in /template


            res = cursor.execute('INSERT INTO URL (URL) VALUES (?)', [url])
            encoded_string = base62(res.lastrowid)
            
            
        return render_template('index.html', shortenedUrl=hostAddress + encoded_string)
    else:
        return render_template('index.html')


# App method URL redirects
@app.route('/<shortenedUrl>')
def redirect_url(shortenedUrl):

    urlIndex = base10(shortenedUrl) # Converts the shortened URL back to base 10 so that it may be used to index the database

    url = hostAddress 

    with sqlite3.connect('links.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute('SELECT URL FROM URL WHERE ID=?', [urlIndex])
        try:
            dataBaseEntry = res.fetchone()
            if dataBaseEntry is not None:
                url = dataBaseEntry[0]
        except Exception as e:
            print(e)
    return redirect(url)

