import yaml
from pprint import pprint
#dict1 = {'key1':'IOS', 'key2': 'NXOS', 'key3':'IOS-XE', 'key4': 'IOS_XR'}
#print(yaml.dump(dict1))

yamlinstring = """
a: 1
b: 
  c: 3
  d: 4
  e:
    - name: 'Prod'
      id: 100
    - name: 'Dev'
      id: 200 
  f:
    - '10.1.1.1/24'
    - '10.2.1.1/24' 
"""
#print(yaml.dump(yaml.safe_load(yamlinstring), default_flow_style = False))
#print(type(yaml.dump(yaml.safe_load(yamlinstring), default_flow_style = True)))

#print('-------------------------------------------------------------')

#print(yaml.dump(yaml.safe_load(yamlinstring), default_flow_style = True))

#print(yaml.dump(yaml.safe_load(yamlinstring)))

pprint(yaml.safe_load(yamlinstring))