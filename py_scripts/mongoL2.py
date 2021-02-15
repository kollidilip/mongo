import pymongo
from random import randint
url = "mongodb://localhost:27017"
client = pymongo.MongoClient(url)

names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

db=client.business

#createData(db)
def createData(db):
    for x in range(1, 501):
        business = {
            'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
            'rating' : randint(1, 5),
            'likes' : randint(1,350),
            'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
        }
        result=db.reviews.insert_one(business)

# create the instance of a collection
collection = db.reviews
#print(collection)

# query data
# 1- Top Rated business (query the business details which are top rated)
query1 = {'rating' : {'$eq' : 5}}
result1 = collection.find(query1).limit(5)
print("Top rated businesses")
for doc in result1:
    print (doc)
    
# 2- Top Rated business which are most liked (query the business details which aretop rated and liked the most)
query2 = {'rating' : {'$eq' : 5}}
result2 = collection.find(query2).sort("likes" ,-1).limit(5)
print("Most liked top rated business")
for doc in result2:
    print (doc)

# 3- get the business names based on the Cuisine value (Mexican)

query3 = {'cuisine' : {'$eq' : 'Mexican'}}
result3 = collection.find(query3).limit(5)
print("Business with cuisine as Mexican")
for doc in result3:
    print (doc)

# 4- get the popular business names based on the Cuisine value (Mexican)

query4 = {'cuisine' : {'$eq' : 'Mexican'}}
result4 = collection.find(query3).sort("likes" ,-1).limit(5)
print("Popular Business with cuisine as Mexican")
for doc in result4:
    print (doc)