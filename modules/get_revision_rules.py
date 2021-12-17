from common.tc_session import TC_Session
from common.soa_requests import SOA_Request
from secret import Secret


def execute_as_json():
    tc_session = TC_Session(Secret.TC_HOST, Secret.TC_LOGIN, Secret.TC_PASSWORD)
    tc_session.login()
    transport = tc_session.get_transport()
    soa_request = SOA_Request(Secret.TC_HOST, transport)
    response = soa_request.get_revision_rules()
    tc_session.logout()
    return str(response)


def execute_as_obj():
    tc_session = TC_Session(Secret.TC_HOST, Secret.TC_LOGIN, Secret.TC_PASSWORD)
    tc_session.login()
    transport = tc_session.get_transport()
    soa_request = SOA_Request(Secret.TC_HOST, transport)
    response = soa_request.get_revision_rules()
    tc_session.logout()

    # preparing data
    dic_collection = []
    if 'ServiceData' in response:
        service_data = response['ServiceData']
        if 'dataObjects' in service_data:
            object_count = len(service_data['dataObjects'])
            print('Revision rules found:', object_count)
            for data_object in service_data['dataObjects']:
                object_dic = {
                    'uid': data_object['uid'],
                    'objectID': data_object['objectID'],
                }
                if 'properties' in data_object:
                    properties = data_object['properties']
                    for property in properties:
                        object_dic[property['name']] = property['uiValue']
                dic_collection.append(object_dic)
    return dic_collection