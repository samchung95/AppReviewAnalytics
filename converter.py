import json
from pprint import pprint

category_map = {
    "Functionality":
    set(["Functionality",
     "App functionality",
     "Technical issue",
     "Authentication",
     "Product information",
     "Technical performance",
     "Bug",
     "Features",
     "Setup process",
     "Downloading problem",
     "Auto-redeem",
     "Order placement",
     "Receipt printing feature"]),

    "User Experience":
    set(["User Experience",
     "Ease of use",
     "Navigation",
     "Overall experience",
     "User interface",
     "App design/usability",
     "Shopping features",
     "Connectivity",
     "Online sales",
     "Lucky draw app",
     "Feature request",
     "Lucky draw",
     "Simplicity",
     "Speed"]),

    "Usability":
    set(["Usability",
     "Website navigation",
     "Purchasing",
     "Convenience",
     "Shopping",
     "Ease of purchase",
     "Online ordering",
     "Store layout",
     "Inventory management"]),

    "Customer Support":
    set(["Customer support",
     "Customer service"]),

    "Technical issue":
    set(["Technical Issues",
     "Authentication",
     "Technical difficulty"]),

    "Online shopping":
    set(["Online shopping",
     "E-commerce",
     "Online purchase",
     "Delivery",
     "Shopping experience",
     "Grocery shopping",
     "Delivery service",
     "Online purchases"]),

    "Product/Service Quality":
    set(["Product/service quality",
     "Product",
     "Reliability",
     "Content",
     "Purpose",
     "Product selection",
     "Product display",
     "Value proposition",
     "Inventory management"]),

    "Promotions":
    set(["Promotions",
     "Promotion",
     "Rewards"]),

    "Value for Money":
    set(["Value for money",
     "Payment",
     "Value",
     "Payment process",
     "Benefits",
     "Price",
     "Purchase history feature",
     "Redemption"]),

    "Miscellaneous":
    set(["Expectations",
     "Pain point",
     "Marketing",
     "Options",
     "Technology",
     "Registration process",
     "Privacy concerns",
     "Comparison to NTUC app",
     "Positive point",
     "Suggestions for improvement"])
}

f = open('results.json')
data = json.load(f)

for cat,s in category_map.items():
    _t = set()
    for item in s:
        _t.add(item.lower().replace(' ',''))

    category_map[cat] = _t
    
print(category_map)

for cat,s in category_map.items():
    print('usability' in s)

new_data = []
for _review in data:
    category = _review["category"]
    sentiment = _review["sentiment"]
    review = _review["review"]
    stars = _review["stars"]

    sub_category = category
    main_category = 'Others'
    for cat,s in category_map.items():
        print(sub_category.lower().replace(' ',''), sub_category.lower().replace(' ','') in category_map[cat])
        if sub_category.lower().replace(' ','') in s:
            main_category = cat
    
    _t = {'sub_category':sub_category, 'main_category': main_category}
    _review.update(_t)
    new_data.append(_review)
    

with open('results_raw_new.json',mode='w') as file:
    json.dump(new_data, file)