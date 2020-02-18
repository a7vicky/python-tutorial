import json
import yaml
import sys

#print(sys.argv[1])
file_input=sys.argv[1]

# yaml to json covertor
'''
with open(file_input, 'r') as f:
    # yaml to json conversion
    json_data=json.dumps(yaml.safe_load(f), indent=2)
print(json_data)
'''

# json to yaml convertor
with open(file_input, 'r') as f:
    # json to yaml conversion
    yaml_data=yaml.safe_dump(json.load(f))
print(yaml_data)
