
def get_revision_uid(soa_request, part_id:str, rev:str) -> str:
    """ Returns item revision uid by part id and revision """
    revision_uid = ''
    response_getItemFromId = soa_request.get_item_from_id(part_id, rev)
    try:
        revision_uid = response_getItemFromId['output'][0]['itemRevOutput'][0]['itemRevision']['uid']
    except Exception as e:
        print('Failed get revision UID:', e)
    return revision_uid

def get_item_uid(soa_request, part_id:str, rev:str) -> str:
    """ Returns item uid by part id and revision """
    item_uid = ''
    response_getItemFromId = soa_request.get_item_from_id(part_id, rev)
    try:
        item_uid = response_getItemFromId['output'][0]['item']['uid']
    except Exception as e:
        print('Failed get item UID:', e)
    return item_uid
    