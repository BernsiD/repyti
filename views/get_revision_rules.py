from flask import Blueprint, Response
from modules import get_revision_rules

get_revision_rules_blueprint = Blueprint('get_revision_rules', __name__)

@get_revision_rules_blueprint.route("/", methods=["GET"])
def get_revision_rules_view():
    response = get_revision_rules.execute_as_obj()
    
    return Response(response, mimetype='text/xml')


get_revision_rules_blueprint.route("/xml", methods=["GET"])
def get_revision_rules_view():
    response = get_revision_rules.execute_as_xml()
    
    return Response(response, mimetype='text/xml')
