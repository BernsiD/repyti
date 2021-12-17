from common.tc_session import TC_Session
from common.soa_requests import SOA_Request
from secret import Secret


def extract_item_properties(item_id, rev_id):
    tc_session = TC_Session(Secret.TC_HOST, Secret.TC_LOGIN, Secret.TC_PASSWORD)
    tc_session.login()
    transport = tc_session.get_transport()  # transoprt containts session and use it in all following soa requests
    soa_request = SOA_Request(Secret.TC_HOST, transport)
    
    # set policy
    soa_request.set_policy("DEFAULT")

    # get uid
    response_getItemFromId = soa_request.get_item_from_id(item_id, rev_id)
    try:
        revision_uid = response_getItemFromId['output'][0]['itemRevOutput'][0]['itemRevision']['uid']
        print("Das ist die UID der Revision:", revision_uid)
    except Exception as e:
        print('Failed to get UID:', e)
        return {}

    # get properties
    response_getProperties = soa_request.get_properties(revision_uid)
    prop_dict = {}
    for property in response_getProperties['dataObjects'][0]['properties']:
        prop_dict[property['name']] = property['uiValue']

    # get classification uid
    response_findClassificationObjects = soa_request.find_classification_objects(revision_uid)
    classification_uid = None
    class_dict =  {}
    try:
        classification_uid = response_findClassificationObjects['icos'][0]['value'][0]['uid']
        print("Das ist die UID der Classification:", classification_uid)
    except Exception as e:
        print('Failed to get Classificaton UID:', e)
        

    # get classification object info
    if classification_uid:
        response_getClassificationObjectInfo = soa_request.get_classification_object_info(classification_uid)
        for attr in response_getClassificationObjectInfo['classificationObjectInfo'][0]['value']['attrValuesMap']:
            try:
                # check or chooce other peace of information you need to extract
                class_dict[attr['key']] = attr['value']['values'][0]['attrValue']
            except:
                pass

    # collect all data
    mapping_dict = {**prop_dict, **class_dict}
    return mapping_dict

