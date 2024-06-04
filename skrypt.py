#json
import json

with open('file.json') as f:
    d = json.load(f)
    print(d)

# yaml
import yaml

with open("file.yaml") as stream:
    print(yaml.safe_load(stream))

# xml
import xml.etree.ElementTree as ET

tree = ET.parse('file.xml')
root = tree.getroot()
for child in root:
    print (child)