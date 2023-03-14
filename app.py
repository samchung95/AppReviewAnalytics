import json
from pprint import pprint

f = open('results.json')
data = json.load(f)

cats = {}
for r in data:
    cat = r['category'].lower()
    sen = r['sentiment'].lower()


    if cat not in cats:
        cats[cat]={}
        cats[cat][sen] = 1
    else:
        if sen not in cats[cat]:
            cats[cat][sen] = 1
        else:
            cats[cat][sen] += 1

def compare(x):
    if 'negative' in cats[x]:
        return cats[x]['negative']
    return 0
li = list(cats.keys())
li.sort(key=compare)
li = [{i:cats[i]} for i in li]
li.reverse()
pprint(li)

with open('results_ranked.json',mode='w') as file:
    json.dump(li, file)