import pymongo
from random import randint
url = "mongodb://localhost:27017"
client = pymongo.MongoClient(url)

names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

db=client.business

for x in range(1, 501):
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'likes' : randint(1,350),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }
    result=db.reviews.insert_one(business)