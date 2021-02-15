import pymongo
url = "mongodb://sasmgdbp:F9m9w7x4d6v7@10.54.14.152:61020,10.9.143.158:61020,10.9.143.160:61020/?authMechanism=PLAIN&readPreference=primary&authSource=$external&ssl=false"
url1 = "mongodb://609586622:9848502935%40DadJan@10.54.14.152:61020,10.9.143.158:61020,10.9.143.160:61020/?authMechanism=PLAIN&readPreference=primary&authSource=$external&ssl=false"

myclient = pymongo.MongoClient(url1)
print(myclient.list_database_names())
db = myclient ['admin']
stats = db.currentOp({"secs_running": {"gte": 5}}) 
#db.command("replSetGetStatus")
#db_stats = db.command({'replSetGetStatus'  :1})
print(stats)
