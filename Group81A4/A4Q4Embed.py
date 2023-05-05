from pymongo import MongoClient
import datetime 
import sys

port = int(sys.argv[1])
client = MongoClient('localhost', port)

db = client["A4dbEmbed"]
collections = db["SongwritersRecordings"]
query_result = collections.aggregate([
    {"$unwind": "$recordings"},
    { "$match": { "recordings.issue_date": { "$gt": datetime.datetime(1950, 1, 1, 0, 0) } } },
    { "$project": { 
        "_id": 1, 
        "name": 1,
        "r_name": "$recordings.name",  
        "r_issue_date": "$recordings.issue_date"
    }}
])

for every_detail in query_result:
    print(every_detail)
