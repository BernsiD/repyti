from zeep import Client, Settings
from zeep import transports
from zeep.transports import Transport
from requests import Session
from lxml import etree


TC_HOST = 'http://ts1-msk.corp.uzga404.ru:7001/tc/services'
TC_LOGIN = 'nathadv'
TC_PASSWORD = 'Galka7777'


class Transport_decoration_free(Transport):
    def post_xml(self, address, envelope, headers):
        """Post the envelope xml element to the given address with the headers.
        In this modificaton `xml_declaration` is False to remove <?xml version='1.0' encoding='utf-8'?>
        For some reason server return empty page with status 200 with this line.
        """
        message = etree.tostring(envelope, pretty_print=False, xml_declaration=False, encoding="utf-8")
        return self.post(address, message, headers)


session = Session()
transport = Transport_decoration_free(session=session)

# login
wsdl_login = '%s/%s?wsdl' % (TC_HOST, "Core-2006-03-Session")
c_login = Client(wsdl_login, transport=transport)
r_login = c_login.service.login(username=TC_LOGIN, password=TC_PASSWORD, group="", role="", sessionDiscriminator="1i52")

# set policy
wsdl_policy = '%s/%s?wsdl' % (TC_HOST, "Core-2007-01-Session") 
c_set_policy = Client(wsdl_policy, transport=transport)
r_set_policy = c_set_policy.service.setObjectPropertyPolicy(policyName="DEFAULT")

# get item data
wsdl_get_item_data = '%s/%s?wsdl' % (TC_HOST, "Core-2007-01-DataManagement")
c_item_from_id = Client(wsdl_get_item_data, transport=transport)
r_item_from_id = c_item_from_id.service.getItemFromId(nRev=1, infos={'itemId':"4051.0000.00.005", 'revIds':"00"}, pref='')

item_rev_uid = r_item_from_id['output'][0]['itemRevOutput'][0]['itemRevision']['uid']
print('# getItemFromId')
print(r_item_from_id)

# # get item properties
# wsdl_get_properties = '%s/%s?wsdl' % (TC_HOST, "Core-2006-03-DataManagement")
# c_properties = Client(wsdl_get_properties, transport=transport)
# r_properties = c_properties.service.getProperties(objects={'uid':item_rev_uid})
# print('# getProperties, UID:', item_rev_uid)
# print(r_properties)

# # get item properties: Core-2006-03-DataManagement
# wsdl_get_properties = '%s/%s?wsdl' % (TC_HOST, "Core-2006-03-DataManagement")
# c_properties = Client(wsdl_get_properties, transport=transport)
# r_properties = c_properties.service.getProperties(objects={'uid':item_rev_uid})
# print('# getProperties, UID:', item_rev_uid)
# print(r_properties)

# # get material
# wsdl_get_material = '%s/%s?wsdl' % (TC_HOST, "MaterialManagement-2012-09-MaterialManagement") 
# c_get_material = Client(wsdl_get_material, transport=transport)
# r_get_material = c_get_material.service.getMaterialSubstanceInfo(objs={'uid':item_rev_uid})
# print(r_get_material)

# expandGRMRelations
wsdl_expandGRMRelations = '%s/%s?wsdl' % (TC_HOST, "Cad-2007-01-DataManagement") 
c_expandGRMRelations = Client(wsdl_expandGRMRelations, transport=transport)
r_expandGRMRelations = c_expandGRMRelations.service.expandGRMRelations(objects={'uid':item_rev_uid}, pref={'expItemRev':''})
print(r_expandGRMRelations)




# logout
r_logout = c_login.service.logout()





# {
#     'output': [
#         {
#             'item': {
#                 'properties': [],
#                 'uiproperties': [],
#                 'props': [],
#                 'uid': 'RKnFFPEFojgGRC',
#                 'type': 'SPB5_Det',
#                 'classUid': None,
#                 'className': 'SPB5_Det',
#                 'updateDesc': None,
#                 'objectID': None,
#                 'cParamID': None,
#                 'isHistorical': None,
#                 'isObsolete': None,
#                 'jbt_addition': None
#             },
#             'itemRevOutput': [
#                 {
#                     'itemRevision': {
#                         'properties': [],
#                         'uiproperties': [],
#                         'props': [],
#                         'uid': 'RKvFFPEFojgGRC',
#                         'type': 'SPB5_DetRevision',
#                         'classUid': None,
#                         'className': 'SPB5_DetRevision',
#                         'updateDesc': None,
#                         'objectID': None,
#                         'cParamID': None,
#                         'isHistorical': None,
#                         'isObsolete': None,
#                         'jbt_addition': None
#                     },
#                     'datasets': []
#                 }
#             ]
#         }
#     ],
#     'ServiceData': {
#         'updatedObjs': [],
#         'deletedObjs': [],
#         'createdObjs': [],
#         'childChangeObjs': [],
#         'plainObjs': [
#             {
#                 'uid': 'RKnFFPEFojgGRC'
#             },
#             {
#                 'uid': 'RKvFFPEFojgGRC'
#             }
#         ],
#         'updated': [],
#         'deleted': [],
#         'created': [],
#         'childChange': [],
#         'plain': [],
#         'dataObjects': [
#             {
#                 'properties': [
#                     {
#                         'values': [
#                             {
#                                 'value': 'SPB5_Det',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'object_type',
#                         'uiValue': 'Component',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': True
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'owning_site',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': 'Usd9Os4NojgGRC',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'owning_group',
#                         'uiValue': 'ОРиСУЖЦП.УАиСЖЦП.Дирекция ПИиУП.АО УЗГА',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': 'bKmBtzWWojgGRC',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'owning_user',
#                         'uiValue': 'Натха Дмитрий Владимирович (nathadv)',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '2021-12-09T14:32:03+03:00',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'last_mod_date',
#                         'uiValue': '09-Dec-2021 14:32',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': True
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'has_variant_module',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': ' ',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'checked_out',
#                         'uiValue': ' ',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': True
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'object_desc',
#                         'uiValue': '',
#                         'modifiable': True
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': True
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'is_vi',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '0',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'is_configuration_item',
#                         'uiValue': 'False',
#                         'modifiable': True
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '353833-Тестовая деталь',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'object_string',
#                         'uiValue': '353833-Тестовая деталь',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [],
#                         'uiValues': [],
#                         'name': 'process_stage_list',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '0',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'revision_number',
#                         'uiValue': ' ',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [],
#                         'uiValues': [],
#                         'name': 'release_status_list',
#                         'uiValue': '',
#                         'modifiable': False
#                     }
#                 ],
#                 'uiproperties': [],
#                 'props': [],
#                 'uid': 'RKnFFPEFojgGRC',
#                 'type': 'SPB5_Det',
#                 'classUid': None,
#                 'className': 'SPB5_Det',
#                 'updateDesc': None,
#                 'objectID': 'RKnFFPEFojgGRC',
#                 'cParamID': None,
#                 'isHistorical': None,
#                 'isObsolete': None,
#                 'jbt_addition': None
#             },
#             {
#                 'properties': [
#                     {
#                         'values': [
#                             {
#                                 'value': '2021-12-09T14:32:03+03:00',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'last_mod_date',
#                         'uiValue': '09-Dec-2021 14:32',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': True
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'object_desc',
#                         'uiValue': '',
#                         'modifiable': True
#                     },
#                     {
#                         'values': [],
#                         'uiValues': [],
#                         'name': 'release_status_list',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': 'Usd9Os4NojgGRC',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'owning_group',
#                         'uiValue': 'ОРиСУЖЦП.УАиСЖЦП.Дирекция ПИиУП.АО УЗГА',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': True
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'owning_site',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [],
#                         'uiValues': [],
#                         'name': 'process_stage_list',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': 'RKnFFPEFojgGRC',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'items_tag',
#                         'uiValue': '353833-Тестовая деталь',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [],
#                         'uiValues': [],
#                         'name': 'fms_tickets',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [],
#                         'uiValues': [],
#                         'name': 'view',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': 'bKmBtzWWojgGRC',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'owning_user',
#                         'uiValue': 'Натха Дмитрий Владимирович (nathadv)',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'fnd0IRDCUsed',
#                         'uiValue': '',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': 'SPB5_DetRevision',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'object_type',
#                         'uiValue': 'Component Revision',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '0',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'is_IRDC',
#                         'uiValue': 'False',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': ' ',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'checked_out',
#                         'uiValue': ' ',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '353833/00-Тестовая деталь',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'object_string',
#                         'uiValue': '353833/00-Тестовая деталь',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '0',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'revision_number',
#                         'uiValue': ' ',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '0',
#                                 'isNull': None
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'is_vi',
#                         'uiValue': 'False',
#                         'modifiable': False
#                     },
#                     {
#                         'values': [
#                             {
#                                 'value': '',
#                                 'isNull': True
#                             }
#                         ],
#                         'uiValues': [],
#                         'name': 'has_variant_module',
#                         'uiValue': '',
#                         'modifiable': False
#                     }
#                 ],
#                 'uiproperties': [],
#                 'props': [],
#                 'uid': 'RKvFFPEFojgGRC',
#                 'type': 'SPB5_DetRevision',
#                 'classUid': None,
#                 'className': 'SPB5_DetRevision',
#                 'updateDesc': None,
#                 'objectID': 'RKvFFPEFojgGRC',
#                 'cParamID': None,
#                 'isHistorical': None,
#                 'isObsolete': None,
#                 'jbt_addition': None
#             },
#             {
#                 'properties': [],
#                 'uiproperties': [],
#                 'props': [],
#                 'uid': 'Usd9Os4NojgGRC',
#                 'type': 'Group',
#                 'classUid': None,
#                 'className': 'Group',
#                 'updateDesc': None,
#                 'objectID': 'Usd9Os4NojgGRC',
#                 'cParamID': None,
#                 'isHistorical': None,
#                 'isObsolete': None,
#                 'jbt_addition': None
#             },
#             {
#                 'properties': [],
#                 'uiproperties': [],
#                 'props': [],
#                 'uid': 'bKmBtzWWojgGRC',
#                 'type': 'User',
#                 'classUid': None,
#                 'className': 'User',
#                 'updateDesc': None,
#                 'objectID': 'bKmBtzWWojgGRC',
#                 'cParamID': None,
#                 'isHistorical': None,
#                 'isObsolete': None,
#                 'jbt_addition': None
#             }
#         ],
#         'modelObjects': [],
#         'partialErrors': []
#     }
# }