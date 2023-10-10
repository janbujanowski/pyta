import json

file = open("neurox/data/BTCEUR-1h.json","rt", encoding="utf-8")
fileContent = file.read()
dataset = json.loads(fileContent)

open = []
close = []
high = []
low = []

for entry in dataset['data']:
    open.append(entry['rate_open'])
    close.append(entry['rate_close'])    
    high.append(entry['rate_high'])    
    low.append(entry['rate_low'])   