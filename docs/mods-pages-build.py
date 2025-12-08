import os, sys
import json

datafile='mods-pages-build.json'
with open(datafile, mode='r') as f:
    payload=json.load(f)

result=''
result+=''
result+='# applied mods / datapacks\n'
result+='\n'
result+='## mods\n'
result+='\n'
result+='| Icon | Name | Descr |\n'
result+='| ---- | ---- | ----- |\n'
for line in payload['mods']:
    result+='| <img src="{}" style="height: 3em;" /> | {} | {} |\n'.format(
        line['icon'],
        line['name'],
        line['description'],
    )
result+='\n'
result+='## datapacks\n'
result+='\n'
result+='| Name | Descr |\n'
result+='| ---- | ----- |\n'
for line in payload['datapack']:
    result+='| {} | {} |\n'.format(
        line['name'],
        line['description'],
    )
result+='\n'
result+=''
print(result)
