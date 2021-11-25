import json
from flask import jsonify, Blueprint, json
from flask.globals import request
from flask.templating import render_template
from modules import extract_rev_effectivity


extract_effectivity_blueprint = Blueprint('extract_eff', __name__)

#route for the browser 
@extract_effectivity_blueprint.route('/', methods=["GET", "POST"])
def new_item():
    item_dict = {}
    if request.method == 'POST':
        item_id = request.form['item_id']
        rev_id = request.form['rev_id']

        item_dict = extract_rev_effectivity.extract_rev_effectivity(
            item_id, rev_id)

    return render_template('effectivity_extraction.html', item_dict=item_dict)

#route for the REST Application
@extract_effectivity_blueprint.route("/rest", methods=["POST"])
def extract_item_rest():
    datadict = request.get_json()
    item_id = datadict['item_id']
    rev_id = datadict['rev_id']
    outputlist = extract_rev_effectivity.extract_rev_effectivity(
        item_id, rev_id)
    retJson = outputlist
    return jsonify(retJson)
