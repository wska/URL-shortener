#!/usr/bin/env python
python3 init.py
gunicorn -w 4 urlshortener:app