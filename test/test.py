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
r_item_from_id = c_item_from_id.service.getItemFromId(nRev=1, infos={'itemId':"353833", 'revIds':"00"}, pref='')
#print(r_item_from_id)

# logout
r_logout = c_login.service.logout()


