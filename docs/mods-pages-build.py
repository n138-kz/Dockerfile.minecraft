import json

datafile='mods-pages-build.json'
with open(datafile, mode='r') as f:
    payload=json.load(f)

print(payload)
