import json

# Use file handling to read file 
with open('rbac.json', encoding='utf-8') as f:
    data = json.load(f)
    # print(type(data))
for resource in data['resources']:
        #print(json.dumps(resource, indent=2))
    del(resource['singularName'])
with open('new-rbac.json', 'w') as nf:
    json.dump(data, nf)
