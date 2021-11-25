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



def get_revision_rules(session_token, serveradress):
    url = f"{serveradress}/tc/services/Cad-2007-01-StructureManagement?wsdl"
    headers = {'Content-Type': 'text/xml',
               'SOAPAction': 'getRevisionRules', 'Cookie': session_token}
    body = """<x:Envelope
    xmlns:x="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:str="http://teamcenter.com/Schemas/Cad/2007-01/StructureManagement">
    <x:Header/>
    <x:Body>
        <str:GetRevisionRulesInput></str:GetRevisionRulesInput>
    </x:Body>
</x:Envelope>"""
    response = requests.post(url, data=body, headers=headers, verify=False)

    if response.status_code == 200:
        print('Request was successful.')
        # print(response.content)
        return response.content
    else:
        print('Request failed.')
        sys.exit('Command operation failed with HTTP Code ' +
                 str(response.status_code))





def test_request():
    tc_session = TC_Session(Secret.TC_LOGIN, Secret.TC_PASSWORD)  #Enter username password here
    tc_session.login()
    set_policy(tc_session.session_token, tc_session.serveradress)

    resp = get_revision_rules(tc_session.session_token, tc_session.serveradress)

    tc_session.logout()
 
    return resp


if __name__ == "__main__":
    main()
