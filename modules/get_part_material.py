from common.tc_session import TC_Session
from common.soa_requests import SOA_Request
from common.utils import get_revision_uid
from secret import Secret


def execute_as_json(item_id, revision):
    tc_session = TC_Session(Secret.TC_HOST, Secret.TC_LOGIN, Secret.TC_PASSWORD)
    tc_session.login()
    transport = tc_session.get_transport()
    soa_request = SOA_Request(Secret.TC_HOST, transport)

    # Check name of relation type with material. It could be different.
    relation_type_name = 'SPB5_IzgotovlenoIz'  

    # Get data
    revision_uid = get_revision_uid(soa_request, item_id, revision)
    response = soa_request.expand_grm_relations_for_primary(revision_uid, relation_type_name)

    tc_session.logout()

    return str(response)


def execute_as_obj(item_id, revision):
    tc_session = TC_Session(Secret.TC_HOST, Secret.TC_LOGIN, Secret.TC_PASSWORD)
    tc_session.login()
    transport = tc_session.get_transport()
    soa_request = SOA_Request(Secret.TC_HOST, transport)

    # Check name of relation type with material. It could be different.
    relation_type_name = 'SPB5_IzgotovlenoIz'  

    # Get data
    revision_uid = get_revision_uid(soa_request, item_id, revision)
    response = soa_request.expand_grm_relations_for_primary(revision_uid, relation_type_name)

    tc_session.logout()

    # preparing data
    dic_collection = []
    if 'ServiceData' in response:
        service_data = response['ServiceData']
        if 'dataObjects' in service_data:
            for data_object in service_data['dataObjects']:
                if data_object['type'] == 'SPB5_MaterialMMRevision':  # Check your material object type
                    object_dic = {
                        'uid': data_object['uid'],
                        'objectID': data_object['objectID'],
                        'type': data_object['type'],
                    }
                    if 'properties' in data_object:
                        properties = data_object['properties']
                        for property in properties:
                            object_dic[property['name']] = property['uiValue']
                    dic_collection.append(object_dic)
    return dic_collection