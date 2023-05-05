from pymongo import MongoClient
import sys
import json
from bson import ObjectId, json_util

def main():
    if len(sys.argv) > 1 :
        port = int(sys.argv[1])
        client = MongoClient('localhost', port)
        db = client["A4dbEmbed"]
        songwriters = db['songwriters']
        recordings = db['recordings']
        with open('songwriters.json', 'r') as f:
            song_writer_input = json_util.loads(f.read())
            for doc in song_writer_input:
                doc['_id'] = ObjectId()
            songwriters.insert_many(song_writer_input)
        with open('recordings.json', 'r') as f:
            recordings_input = json_util.loads(f.read())
            for doc in recordings_input:
                doc['_id'] = ObjectId()
            recordings.insert_many(recordings_input)
        songwriter_recordings = db['SongwritersRecordings']
        input_reader_embeded = songwriters.aggregate([{"$lookup" : { "from": "recordings", "localField" : "recordings", "foreignField": "recording_id", "as": "recordings"}}])
        songwriter_recordings.insert_many(input_reader_embeded)
main()