import pymongo
from random import randint

def connectToMongo():
    url = "mongodb://localhost:27017"
    client = pymongo.MongoClient(url)
    return client


def createData(db):
    fnames = ['dilip','sai','ravi','swathi','arun','prasad','harish','ramesh','sureedu','manju','nithin']
    lname = ['A','B','C','D','E']
    streets = ["Homestead Drive","Ann Street","Taylor Street","Summit Avenue","Cedar Avenue","Street West","Primrose Lane","Buttonwood Drive","Cedar Street","Westminster Drive","Arch Street"]
    city = ["Haldia","visakhapatnam","Bhatpara","Aurangabad","srikakulam","Panihati","Sambhal","vijayawada","Jhansi","Bhatpara","Katihar"]
    state = ["andhra pradesh","tamilnadu","madhya pradesh","uttarkhand","punjab","telengana"]
    zip = ["560012","530013","500014","470015","440016","410017"]
    rewards = ['red','green','amber','gold','platinum','star']
    for x in range(1,501):
        baker={
		'user_id' : x,
		'first_name' : fnames[randint(0,len(fnames)-1)],
		'last_name' : lname[randint(0,len(lname)-1)],
		'emailid' :  fnames[randint(0,len(fnames)-1)]+lname[randint(0,len(lname)-1)]+'@abc.com',
		'backing_level' : randint(0,20),
		'Address' : {
		'street_name': str(randint(0,100))+" "+streets[randint(0,len(streets)-1)],
		'city' : city[randint(0,len(city)-1)],
		'state' : state[randint(0,len(state)-1)],
		'zip' : zip[randint(0,len(zip)-1)]		
		},
		'rewards' : rewards[:randint(1,len(rewards)-1)]
                }
        db.bakers.insert_one(baker)
              
if __name__ == '__main__':

    client = connectToMongo()
    db=client.business
    #createData(db)
