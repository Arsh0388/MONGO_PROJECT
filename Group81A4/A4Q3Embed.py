from pymongo import MongoClient
import sys

port = int(sys.argv[1])
client = MongoClient('localhost', port)

db = client["A4dbEmbed"]
collections = db["SongwritersRecordings"]

pipeline = [
    {"$unwind": "$recordings"},
    { "$group": { "_id": { "$arrayElemAt": ["$songwriter_ids", 0] }, "sum_of_recordings": { "$sum": "$recordings.length" } } }
]

result = db.recordings.aggregate(pipeline)

for document in result:
    print(document)
