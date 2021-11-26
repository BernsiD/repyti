import xml.etree.ElementTree as ET
tree = ET.parse('source.xml')
root = tree.getroot()

print(len(root))