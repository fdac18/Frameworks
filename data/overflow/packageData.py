import datetime
import pprint

from pymongo import MongoClient


neededtags = [
    'reactjs',
    'angularjs',
    'vue.js',
    'vuejs2',
    'ember.js',
    'jquery',
    'backbone.js'
]

client = MongoClient('da1')
sodata = client.fdac18stackoverflow
postcol = sodata.posts

for tag in neededtags:
    anfile = open(tag + '.json', 'w+')
    pipeline = [
        {
            "$match": {
                "Tags": tag,
                "CreationDate": {
                    "$gte": datetime.datetime(2015, 1, 1, 0, 0, 0)
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "$concat": [
                      {"$substr": [{"$year": "$CreationDate"}, 0, 4]},
                        "-",
                      {"$substr": [{"$month": "$CreationDate"}, 0, 4]},
                        "-",
                      {"$substr": [{"$dayOfMonth": "$CreationDate"}, 0, 4]}
                    ]
                },
                "c": {"$sum": 1}
            }
        }
    ]
    anfile.write(str(list(postcol.aggregate(pipeline))))
    anfile.close()
