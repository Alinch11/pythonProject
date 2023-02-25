import json

with open('card.json', encoding='utf8') as f:
    templates = json.load(f)

# utf8 читает кириллицу, load преобразует для python незнакомы сиснаксис н-р true в True, или null в none
# load позволяет переводить файл формата JSON в Python

print(templates)
print(type(templates))