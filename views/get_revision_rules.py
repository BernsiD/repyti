from flask import Blueprint, Response
from flask.templating import render_template
from modules import get_revision_rules

get_revision_rules_blueprint = Blueprint('get_revision_rules', __name__)

@get_revision_rules_blueprint.route("/", methods=["GET"])
def get_revision_rules_view():
    response_dics = get_revision_rules.execute_as_obj()
    return render_template('revision_rules.html', rule_dics=response_dics)

@get_revision_rules_blueprint.route("/json", methods=["GET"])
def get_revision_rules_json_view():
    response = get_revision_rules.execute_as_json()
    return Response(response, mimetype='text/json')
