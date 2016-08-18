#!/bin/bash
gunicorn -b 0.0.0.0:80 --worker-class=gevent -t 99999 --workers=10 --max-requests 1000 --timeout 28 app:app
