import sys
import requests
import xml.etree.ElementTree as ET

from common.tc_session import TC_Session
from secret import Secret

# set the policy to male ps_extract work


def set_policy(session_token, serveradress):
    url = f"{serveradress}/tc/services/Core-2007-01-Session?wsdl"
    headers = {'Content-Type': 'text/xml',
               'SOAPAction': 'setObjectPropertyPolicy', 'Cookie': session_token}
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ses="http://teamcenter.com/Schemas/Core/2007-01/Session">
   <soapenv:Header/>
   <soapenv:Body>
      <ses:SetObjectPropertyPolicyInput policyName="DEFAULT"/>
   </soapenv:Body>
</soapenv:Envelope>"""
    response = requests.post(url, data=body, headers=headers, verify=False)

    if response.status_code == 200:
        print('Command set_policy successful.')
        print(response.content)
    else:
        print('Command set_policy failed.')
        sys.exit('Command operation failed with HTTP Code ' +
                 str(response.status_code))


# get item from item_id -> need for the top level revision input
def get_item_from_id(session_token, item_id, revision_no, serveradress):
    # f"{serveradress}/tc/services/Core-2007-01-DataManagement?wsdl"
    url = f"{serveradress}/tc/services/Core-2007-01-DataManagement?wsdl"
    headers = {'Content-Type': 'text/xml',
               'SOAPAction': 'getItemFromId', 'Cookie': session_token}
    body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dat="http://teamcenter.com/Schemas/Core/2007-01/DataManagement">
   <soapenv:Header/>
   <soapenv:Body>
      <dat:GetItemFromIdInput nRev="1">
         <!--Zero or more repetitions:-->
         <dat:infos itemId="{item_id}">
            <!--Zero or more repetitions:-->
            <dat:revIds>{revision_no}</dat:revIds>
         </dat:infos>
         <dat:pref>
            <!--Zero or more repetitions:-->
            <dat:prefs relationTypeName="">
               <!--Zero or more repetitions:-->
               <dat:objectTypeNames></dat:objectTypeNames>
            </dat:prefs>
         </dat:pref>
      </dat:GetItemFromIdInput>
   </soapenv:Body>
</soapenv:Envelope>"""

    response = requests.post(url, data=body, headers=headers, verify=False)
    root = ET.fromstring(response.content)

    revision_uid = []

    for objectproperties in root.iter('{http://teamcenter.com/Schemas/Soa/2006-03/Base}dataObjects'):
        print("TAG " + str(objectproperties.tag),
              "ATTR" + str(objectproperties.attrib))
        if any("Revision" in s for s in objectproperties.attrib.values()):
            revision_uid.append(objectproperties.attrib["objectID"])
        else:
            pass

    if response.status_code == 200:
        print("Command get_item_from_id successful")
        return revision_uid
    else:
        print('Command get_item_from_id failed.')
        sys.exit('Command get_item_from_id failed with HTTP Code ' +
                 str(response.status_code))


# get properties of specific revision giving uid
def get_properties(session_token, revision_uid, serveradress):
    url = f"{serveradress}/tc/services/Core-2006-03-DataManagement?wsdl"
    headers = {'Content-Type': 'text/xml',
               'SOAPAction': 'getProperties', 'Cookie': session_token}
    body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dat="http://teamcenter.com/Schemas/Core/2006-03/DataManagement" xmlns:base="http://teamcenter.com/Schemas/Soa/2006-03/Base">
   <soapenv:Header/>
   <soapenv:Body>
      <dat:GetPropertiesInput>
         <!--Zero or more repetitions:-->
         <dat:objects uid="{revision_uid}">
            <!--Zero or more repetitions:-->
         </dat:objects>
         <!--Zero or more repetitions:-->
         <dat:attributes>?</dat:attributes>
      </dat:GetPropertiesInput>
   </soapenv:Body>
</soapenv:Envelope>"""
    prop_dict = {}
    response = requests.post(url, data=body, headers=headers, verify=False)

    root = ET.fromstring(response.content)
    for objectproperties in root.iter('{http://teamcenter.com/Schemas/Soa/2006-03/Base}properties'):
        print("TAG " + str(objectproperties.tag),
              "ATTR" + str(objectproperties.attrib))
        prop_key = None
        prop_value = None
        for item in objectproperties.attrib.items():
            if "name" in item:
                prop_key = item[1]
            elif "uiValue" in item:
                prop_value = item[1]
                prop_dict[prop_key] = prop_value
            else:
                pass

    if response.status_code == 200:
        print("Command get_properties successful")
        # print(response.content)
        return prop_dict
    else:
        print('Command get_properties failed.')
        sys.exit('Command get_properties failed with HTTP Code ' +
                 str(response.status_code))


def findClassificationObjects(session_token, revision_uid, serveradress):
    url = f"{serveradress}/tc/services/Classification-2007-01-Classification"
    headers = {'Content-Type': 'text/xml',
               'SOAPAction': 'findClassificationObjects', 'Cookie': session_token}
    body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:clas="http://teamcenter.com/Schemas/Classification/2007-01/Classification" xmlns:base="http://teamcenter.com/Schemas/Soa/2006-03/Base">
   <soapenv:Header/>
   <soapenv:Body>
      <clas:FindClassificationObjectsInput>
         <!--Zero or more repetitions:-->
         <clas:wsoIds uid="{revision_uid}">
            <base:props name="">
               <base:value modifiable="0">
                  <!--Zero or more repetitions:-->
                  <base:dbValues></base:dbValues>
                  <!--Zero or more repetitions:-->
                  <base:uiValues></base:uiValues>
                  <!--Zero or more repetitions:-->
                  <base:isNulls>0</base:isNulls>
               </base:value>
            </base:props>
         </clas:wsoIds>
      </clas:FindClassificationObjectsInput>
   </soapenv:Body>
</soapenv:Envelope>"""

    response = requests.post(url, data=body, headers=headers, verify=False)

    root = ET.fromstring(response.content)

    classification_uid = None

    for object in root.iter("{http://teamcenter.com/Schemas/Classification/2007-01/Classification}value"):
        print(object.tag, object.attrib)
        classification_uid = object.attrib["objectID"]

    if response.status_code == 200:
        print("Command findClassificationObjects successful")
        # print(response.content)
        return classification_uid
    else:
        print('Command findClassificationObjects failed.')
        sys.exit('Command findClassificationObjects failed with HTTP Code ' +
                 str(response.status_code))


def getClassificationObjectInfo(session_token, classification_uid, serveradress):
    url = f"{serveradress}/tc/services/Classification-2011-12-Classification"
    headers = {'Content-Type': 'text/xml',
               'SOAPAction': 'getClassificationObjectInfo', 'Cookie': session_token}
    body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:clas="http://teamcenter.com/Schemas/Classification/2011-12/Classification">
   <soapenv:Header/>
   <soapenv:Body>
      <clas:GetClassificationObjectInfoInput getOptimizedValues="1" fetchDescriptor="1">
         <!--Zero or more repetitions:-->
         <clas:icoUids>{classification_uid}</clas:icoUids>
      </clas:GetClassificationObjectInfoInput>
   </soapenv:Body>
</soapenv:Envelope>"""

    response = requests.post(url, data=body, headers=headers, verify=False)
    root = ET.fromstring(response.content)

    class_prop_dict = {}

    for child in root.iter("{http://teamcenter.com/Schemas/Classification/2011-12/Classification}attrValuesMap"):
        key = child.attrib['key']
        for value in child.iter("{http://teamcenter.com/Schemas/Classification/2011-12/Classification}values"):
            class_prop_dict[key] = value.attrib['attrValue']

    # print(class_prop_dict)

    class_names_dict = {}

    for child in root.iter("{http://teamcenter.com/Schemas/Classification/2011-12/Classification}attrDescMap"):
        for value in child.iter("{http://teamcenter.com/Schemas/Classification/2011-12/Classification}value"):
            class_names_dict[value.attrib['id']] = value.attrib["name"]

    # print(class_names_dict)

    merged_dict = dict(
        zip(class_names_dict.values(), class_prop_dict.values()))

    if response.status_code == 200:
        print('Command getClassificationObjectInfo successful.')
        # print(response.content)
        return merged_dict
    else:
        print('Command getClassificationObjectInfo failed.')
        sys.exit('Command getClassificationObjectInfo failed with HTTP Code ' +
                 str(response.status_code))


def extract_item_properties(item_id, rev_id):
    tc_session = TC_Session(Secret.TC_LOGIN, Secret.TC_PASSWORD)  #Enter username password here
    tc_session.login()
    set_policy(tc_session.session_token, tc_session.serveradress)
    revision_uid = get_item_from_id(
        tc_session.session_token, item_id, rev_id, tc_session.serveradress)
    print("Das ist die UID der Revision: " + revision_uid[0])
    # Hier werden die Item Properties ausgelesen
    prop_dict = get_properties(
        tc_session.session_token, revision_uid[0], tc_session.serveradress)
    classification_uid = findClassificationObjects(
        tc_session.session_token, revision_uid[0], tc_session.serveradress)
    class_dict = getClassificationObjectInfo(
        tc_session.session_token, classification_uid, tc_session.serveradress)
    tc_session.logout()
    mapping_dict = {**prop_dict, **class_dict}

    return mapping_dict


if __name__ == "__main__":
    main()
