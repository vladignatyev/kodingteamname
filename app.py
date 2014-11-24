# -*- coding: utf-8 -*-
import os
import random
import nltk
nltk.data.path.append('./nltk_data/')

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


words = nltk.corpus.words.words()
random.shuffle(words)
app.config['words'] = words[:1000]


_names = pynamegen.Names(pynamegen.EN_ALPHABET)
app.config['names'] = _names.generator(use_enchant=False, use_words=True, words=app.config['words'])

app.register_blueprint(pages)

if __name__ == '__main__':
    app.config.update(DEBUG=True)
    app.debug = True
    app.run()