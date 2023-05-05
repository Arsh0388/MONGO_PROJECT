from pymongo import MongoClient
import sys

port = int(sys.argv[1])
client = MongoClient('localhost', port)

db = client["A4dbNorm"]
collections = db["recordings"]

pipeline = [
    { "$group": { "_id": { "$arrayElemAt": ["$songwriter_ids", 0] }, "total_length": { "$sum": "$length" }} },
    {"$project": { "_id": 1, "total_length": 1, "songwriter_id": "$_id" } }
]
result = collections.aggregate(pipeline)

for document in result:
    print(document)