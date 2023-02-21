import json

with open('card.json', encoding='utf8') as f:
    strfile = f.read()
    templates = json.loads(strfile)

# strfile преобразование строки

print(templates)
print(type(templates))