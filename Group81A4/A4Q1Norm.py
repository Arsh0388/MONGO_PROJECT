from pymongo import MongoClient
import sys

port = int(sys.argv[1])
client = MongoClient('localhost', port)

db = client["A4dbNorm"]
songwriter = db["songwriters"]
recordings = db["recordings"]

pipeline = db.songwriters.find(
{"recordings": {"$exists": "True", "$not": {"$size": 0}}},
{"_id": 1, "songwriter_id": 1, "name": 1, "num_recordings": {"$size": "$recordings"}}
)


### task 2

pipeline = db.SongwritersRecordings.find(
{"recordings": {"$exists": "True", "$not": {"$size": 0}}},
{"_id": 1, "songwriter_id": 1, "name": 1, "num_recordings": {"$size": "$recordings"}}
)


#####

print(pipeline)


# db.songwriters.find( { "recordings": { $exists: true, $not: { $size: 0 } } }, { "_id": 0, "songwriter_id": 1, "name": 1, "num_recordings": { $size: "$recordings" } })
