from bs4 import BeautifulSoup
from helper import split_into_sentences,queryText
import json

fp = "C:\\Users\\Huai\\Documents\\GitHub\\AppReviewAnalytics\\reviews.html"
soup = BeautifulSoup((open(fp, encoding="utf-8").read()),features="html.parser")

char = 0
sentences = []
reviews = soup.find_all('div', {'class' : 'RHo1pe'})
for review in reviews:
    for comment in review.find_all('div', {'class' : 'h3YV2d'}):
        stars = len(review.find_all('span',{'class':'Z1Dz7b'}))
        sens = [(i,stars) for i in comment.text.split('.') if len(i)>0]
        sentences += [(comment.text,stars)]
        print(sens)
        char += len(comment.text)
        # print(f'-{comment.text}, stars:{str(stars)}')
    # print(reviews)
# print(len(reviews))
categories = [
'Overcrowded store',
'Limited product variety',
'Repetitious promotions',
'Redundant features',
'Inability to purchase or order products',
'Difficulty in logging in',
'Inability to redeem vouchers',
'Unresponsive or crashing back button',
'Security concerns',
'Lack of payment gateway',
'Poor search functionality',
'Limited product information',
'None']
'''\n\nCategories: {str(categories)}'''
# description = sentences[0]

s = [f'\n{(str(i+1))}: {v[0]}' for i,v in enumerate(sentences)]
test = ''.join(s[:5])
print(test)

query = f'Categorise all pain point or positive points of the review \n\n{test}\n\nreturn the answer in a list of json object with keys: "category":str,"confidence":int,"sentiment":str,"comment_index":int'
# # format = 'comment: str, stars: int, category: str, sentiment: int'
print('\n')
# print(query)

result_list = []
for sen in sentences:
    print(sen)
    query = f'Categorise all pain points or positive points of the review \n\nReview: {sen[0]}\n\nreturn the answer in a list of json object with keys: "category":str,"sentiment":str'
    result = queryText(query)

    try:
        r = json.loads(result)
        if type(r) == list:
            for i in r:
                i['review']=sen[0]
                i['stars']=sen[1]
            result_list+=r
    except Exception as e:
        print(e)

with open('results_raw.json',mode='w') as file:
    json.dump(result_list, file)






