# -*- coding: utf-8 -*-
# Gevent monkey patch to support coroutine
from gevent import monkey
monkey.patch_all()
from base64 import b64encode
from config import (DEBUG, PORT)
from flask import Flask
from gevent.wsgi import WSGIServer
from uuid import uuid4


app = Flask(__name__, static_folder='public')
app.secret_key = b64encode(uuid4().hex)
app.debug = DEBUG


from api import api
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def index():
    a = 'a.b'
    print int(a)
    return ''


if DEBUG:
    # run with reloader
    from werkzeug.serving import run_with_reloader
    from lib.log_handler import mailer
    app.logger.addHandler(mailer)

    @run_with_reloader
    def run_server():
        http_server = WSGIServer(('0.0.0.0', PORT), app)
        http_server.serve_forever()
else:

    from lib.log_handler import mailer
    app.logger.addHandler(mailer)

    http_server = WSGIServer(('localhost', PORT), app)
    http_server.serve_forever()
