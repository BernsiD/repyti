from zeep import Client
from zeep.transports import Transport
from lxml import etree
from requests import Session


class TC_Session:
    def __init__(self, serveradress, username, password): 
        self.username = username
        self.password = password
        self.serveradress = serveradress
        self.transport = Transport_decoration_free(session=Session())
        self.client = None

    def login(self):
        self.client = self.__get_client()
        resonse = self.client.service.login(username=self.username, password=self.password, group="", role="", sessionDiscriminator="1i52")

    def logout(self):
        self.client.service.logout()

    def get_transport(self):
        return self.transport

    def __get_client(self):
        service = 'Core-2006-03-Session'
        wsdl = self.__get_wsdl_url(self.serveradress, service)
        return Client(wsdl, transport=self.transport)

    @staticmethod
    def __get_wsdl_url(wsdl_host, wsdl_service):
        return '%s/%s?wsdl' % (wsdl_host, wsdl_service)


class Transport_decoration_free(Transport):
    def post_xml(self, address, envelope, headers):
        """Post the envelope xml element to the given address with the headers.
        In this modificaton `xml_declaration` is False to remove <?xml version='1.0' encoding='utf-8'?>
        For some reason server return empty page with status 200 with this line.
        """
        message = etree.tostring(envelope, pretty_print=False, xml_declaration=False, encoding="utf-8")
        return self.post(address, message, headers)