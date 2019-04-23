from flask import Flask, request, render_template, redirect
from sqlite3 import OperationalError
import string
import sqlite3
from baseconversion import base10, base62
from urllib.parse import urlparse



app = Flask(__name__)
hostAddress = 'http://localhost:5000/'


# App method for GET and POST
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
                return render_template('home.html', shortenedUrl=hostAddress+str(base62(databaseEntry[0])))

            res = cursor.execute('INSERT INTO URL (URL) VALUES (?)', [url])
            encoded_string = base62(res.lastrowid)
            
            
        return render_template('home.html', shortenedUrl=hostAddress + encoded_string)
    else:
        return render_template('home.html')


# App method URL redirects
@app.route('/<shortenedUrl>')
def redirect_url(shortenedUrl):

    urlIndex = base10(shortenedUrl)
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

