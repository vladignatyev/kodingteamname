# -*- coding: utf-8 -*-

from flask import redirect, Blueprint, render_template, current_app, send_from_directory,request, abort, redirect, url_for, make_response, Response, jsonify
import pynamegen


pages = Blueprint('pages', __name__)

@pages.route('/')
def home():
    variants = []
    for i in range(0,10):
        variants += [[word.title() for word in current_app.config['names'].next().split(u' ')]]

    return render_template('index.html', variants=variants)

@pages.route('/names/', methods=['GET'])
def generate():
    num_words = int(request.args['num_words'])
    max_symbols = int(request.args.get('minmax_words', 6))
    true_random = request.args.get('true_random', 'off') == 'on'
    use_numbers = request.args.get('use_numbers', 'off') == 'on'

    if use_numbers:
        _names = pynamegen.Names().generator(num_words=num_words, max_symbols=max_symbols, use_enchant=not true_random)
    else:
        _names = current_app.config['names']


    variants = []
    for i in range(0,20):
        variants += [[word.title() for word in _names.next().split(' ')]]

    return render_template('generate.html', variants=variants)
