from flask import jsonify, Blueprint
from flask.globals import request
from flask.templating import render_template
from modules import get_part_material


get_part_material_blueprint = Blueprint('get_part_material', __name__)

#route for the browser 
@get_part_material_blueprint.route('/', methods=["GET", "POST"])
def get_part_material_view():
    item_dict = {}
    if request.method == 'POST':
        item_id = request.form['item_id']
        rev_id = request.form['rev_id']
        dic_collection = get_part_material.execute_as_obj(item_id, rev_id)
        print('Result dic:', str(item_dict))
    return render_template('get_part_material.html', dics=dic_collection)

#route for the REST Application
@get_part_material_blueprint.route("/rest", methods=["POST"])
def extract_item_rest():
    datadict = request.get_json()
    item_id = datadict['item_id']
    rev_id = datadict['rev_id']
    outputlist = extract_item_properties.extract_item_properties(
        item_id, rev_id)
    retJson = outputlist
    return jsonify(retJson)
