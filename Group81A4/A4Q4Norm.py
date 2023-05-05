from pymongo import MongoClient
import datetime
import sys
port = int(sys.argv[1])
client = MongoClient('localhost', port)


db = client["A4dbNorm"]
songwriter = db["songwriters"]
recordings = db["recordings"]

query_result = recordings.aggregate([
    { "$lookup": { 
        "from": "songwriters", 
        "localField": "songwriter_id", 
        "foreignField": "songwriter_ids", 
        "as": "songwriter" 
    } },
    { "$match": { "issue_date": { "$gt": datetime.datetime(1950, 1, 1, 0, 0, 0, 0) } }},
    { "$project": { 
        "_id": 1, 
        "name": { "$arrayElemAt": ["$songwriter.name", 0] }, 
        "r_name": "$name", 
        "r_issue_date": "$issue_date" 
    } }
])

for every_detail in query_result:
    print(every_detail)
