import json
from flask import jsonify, Blueprint, json
from flask.globals import request
from flask.templating import render_template
from modules import extract_item_properties


extract_item_blueprint = Blueprint('extract', __name__)

#route for the browser 
@extract_item_blueprint.route('/', methods=["GET", "POST"])
def new_item():
    item_dict = {}
    if request.method == 'POST':
        item_id = request.form['item_id']
        rev_id = request.form['rev_id']

        item_dict = extract_item_properties.extract_item_properties(
            item_id, rev_id)

    return render_template('item_extraction.html', item_dict=item_dict)

#route for the REST Application
@extract_item_blueprint.route("/rest", methods=["POST"])
def extract_item_rest():
    datadict = request.get_json()
    item_id = datadict['item_id']
    rev_id = datadict['rev_id']
    outputlist = extract_item_properties.extract_item_properties(
        item_id, rev_id)
    retJson = outputlist
    return jsonify(retJson)
