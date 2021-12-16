from zeep import Client

class SOA_Request:
    def __init__(self, host, transport) -> None:
        self.host = host
        self.transport = transport

    def set_policy(self, policy_name):
        client = self.__get_client('Core-2007-01-Session')
        response = client.service.setObjectPropertyPolicy(policy_name)
        return response

    def get_item_from_id(self, item_id, rev_id):
        client = self.__get_client('Core-2007-01-DataManagement')
        response = client.service.getItemFromId(nRev=1, infos={'itemId':item_id, 'revIds':rev_id}, pref='')
        return response

    def get_properties(self, revision_uid):
        client = self.__get_client('Core-2006-03-DataManagement')
        response = client.service.getProperties(objects={'uid':revision_uid})
        return response

    def find_classification_objects(self, revision_uid):
        client = self.__get_client('Classification-2007-01-Classification')
        response = client.service.findClassificationObjects(wsoIds={'uid':revision_uid})
        return response

    def get_classification_object_info(self, classification_uid):
        client = self.__get_client('Classification-2011-12-Classification')
        response = client.service.getClassificationObjectInfo(icoUids=classification_uid, getOptimizedValues=1, fetchDescriptor=1, locale=1)
        return response

    def get_revision_rules(self):
        client = self.__get_client('Cad-2007-01-StructureManagement')
        response = client.service.getRevisionRules()
        return response

    def expand_grm_relations_for_primary(self, revision_uid, relation_name):
        """
        Returns relation objects by parent revision uid and relation type name
        """
        client = self.__get_client('Core-2007-06-DataManagement')
        response = client.service.expandGRMRelationsForPrimary(primaryObjects={'uid':revision_uid}, pref={'expItemRev':False, 'info':{'relationName':relation_name}}) 
        return response

    def __get_client(self, service_name: str):
        wsdl = '%s/%s?wsdl' % (self.host, service_name) 
        return Client(wsdl, transport=self.transport)
