# -*- coding: utf-8 -*-
import os
import random

from werkzeug.routing import BaseConverter
import redis

import flask
from flask import session, render_template
from flask.ext.compress import Compress

from blueprints.pages import pages
from blueprints.links import links


app = flask.Flask(__name__)
Compress(app)  # enabling gzip compression

app.secret_key = 'Al_osoa-ds)*D_0-12iS_DOASsaSd{OQbwqkdbWODOIHXZ)C -)S_)AD*a- AS_D A_SD AS_D A_SD quw-d19w1-34a;skh'
app.config.update(HTTP_PREFIX='http://')

redis_url = os.environ.get('REDISCLOUD_URL', None)
if not redis_url:
    r = redis.StrictRedis(host='localhost', port=6379)
else:
    import urlparse

    url = urlparse.urlparse(redis_url)
    r = redis.Redis(host=url.hostname, port=url.port, password=url.password)

app.config['REDIS'] = r
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html', popular_items=[]), 404

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
app.register_blueprint(links)

if __name__ == '__main__':
    app.config.update(DEBUG=True)
    app.debug = True
    app.run()