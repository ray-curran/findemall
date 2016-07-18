import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory, jsonify
from flask import send_file, make_response, abort

from angular_flask.main import main

from angular_flask import app

# routing for API endpoints, generated from the models designated as API_MODELS
from angular_flask.core import api_manager
from angular_flask.models import *


session = api_manager.session

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/testing')
def basic_pages(**kwargs):
    return make_response(open('angular_flask/templates/index.html').read())


# routing for CRUD-style endpoints
# passes routing onto the angular frontend if the requested resource exists
from sqlalchemy.sql import exists

# @app.route('/api/testing')
# def testing():
#     return jsonify(**main('130 Sinaloa, Mexico City'))

@app.route('/api/testing/<spot>')
def testing(spot):
    return jsonify(**main(spot))




# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
