"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
import random
#from models import Person

api = Blueprint('api', __name__)


@api.route('/excuse', methods=['GET'])
def getrandomexecuse():

    execuse = ("You wouldnt believe this but,", "OMG,", "Sweet baby jesus,")
    who = ("The dog", "The nanny", "My Grandma")
    action = ("ate", "ran over", "punched")
    what = ("the homework", "the laptop", "the gardner")
    when = ("yesterday", "today", "on friday")

    temporary = random.randint(0,2)
    execuse= who[temporary]+" "+action[temporary] +" "+what[temporary]+" "+when[temporary]


    return jsonify(execuse), 200