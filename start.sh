#!/usr/bin/env python
python3 init.py
gunicorn3 -w 4 -b 127.0.0.1:5000 urlshortener:app