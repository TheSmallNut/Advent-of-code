import os
import sys
import json

path = os.path.join(sys.path[0], 'input.txt')
test = open(path)
content = test.read()
test.close()
content_lines = content.splitlines()

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('lights.json', 'w') as outfile:
    json.dump(data, outfile)
