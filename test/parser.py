import xml.etree.ElementTree as ET
tree = ET.parse('source.xml')
root = tree.getroot()

#root = ET.fromstring(response)

#for objectproperties in root.iter('{http://teamcenter.com/Schemas/Soa/2006-03/Base}properties'):

# for child in root[1][0]:
#     print(child.tag, child.attrib)


dic_collection = []
for dataObj in root.iter('{http://teamcenter.com/Schemas/Soa/2006-03/Base}dataObjects'):
    child_dic = {}
    for child in dataObj:
        #print(child.tag, #     print(child.tag, child.attrib))
        child_dic[child.attrib['name']] = child.attrib['uiValue']
    dic_collection.append(child_dic)
    

for d in dic_collection:
    print(d)        


