from pymongo import MongoClient
import sys

port = int(sys.argv[1])
client = MongoClient('localhost', port)

db = client["A4dbEmbed"]
collections = db["SongwritersRecordings"]


query_result = collections.aggregate([
    {"$unwind": "$recordings"},
    {"$match": {"recordings.recording_id": {"$regex": "^70"}}},
    {"$group": {"_id": '', "average": {"$avg": "$recordings.rhythmicality"}}},
    
])

for each in query_result:
    print(each)
