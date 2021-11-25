from flask import Blueprint, Response
from modules import test_request

test_request_blueprint = Blueprint('test_req', __name__)

@test_request_blueprint.route("/", methods=["GET"])
def test_req():
    response = test_request.test_request()
    
    return Response(response, mimetype='text/xml')
