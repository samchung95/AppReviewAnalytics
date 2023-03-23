import pandas as pd
import json

f = open('results_ranked.json')
data = json.load(f)

columns = [
    "category",
    "negative",
    "positive",
    "neutral"
]

category_list = []
negative_list = []
positive_list = []
neutral_list = []

for _d in data:
    for cat,value in _d.items():
        category_list.append(cat)
        negative_list.append(value.get("negative",0))
        positive_list.append(value.get("positive",0))
        neutral_list.append(value.get("neutral",0))
d = {
    "category":category_list,
    "negative":negative_list,
    "positive":positive_list,
    "neutral":neutral_list
}

df = pd.DataFrame(data=d)

print(df.head())
