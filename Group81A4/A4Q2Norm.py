from pymongo import MongoClient
import sys

port = int(sys.argv[1])
client = MongoClient('localhost', port)

db = client["A4dbNorm"]
songwriter = db["songwriters"]
recordings = db["recordings"]

query_result = db.recordings.aggregate([
    {"$match": {"recording_id": {"$regex": "^70"}}},
    {"$group": {"_id": "", "average": {"$avg": "$rhythmicality"}}}
])


for result in query_result:
    print(result)
