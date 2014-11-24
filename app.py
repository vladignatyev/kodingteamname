# -*- coding: utf-8 -*-
import os
import random

from werkzeug.routing import BaseConverter

import flask
from flask import session, render_template
from flask.ext.compress import Compress

from blueprints.pages import pages

import pynamegen


app = flask.Flask(__name__)
Compress(app)  # enabling gzip compression

app.secret_key = 'kapsd-qjkjz xvscv[widf d[f0iya d09209 -S{PS]q ] } S}Q }S{S Q{}S Fsf]q } FS}{ F}Q{Q}W{R}(]xAFaP{OXCL:'
app.config.update(HTTP_PREFIX='http://')


_names = pynamegen.Names(pynamegen.EN_ALPHABET)
app.config['names'] = _names.generator()

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('pages/404.html', popular_items=[]), 404

def random_string():
    l = list('WA29dFb7XuTwvZYiO4L8f6slrUpkChaSDPRMI1gzoVxQjHec0yNmE3KJn5GBtq') * 16
    random.shuffle(l)
    return ''.join(l)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = random_string()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token   


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter

app.register_blueprint(pages)

if __name__ == '__main__':
    app.config.update(DEBUG=True)
    app.debug = True
    app.run()