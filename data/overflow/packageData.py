import datetime
import pprint

from pymongo import MongoClient


client = MongoClient('da1')
sodata = client.fdac18stackoverflow
postcol = sodata.posts

pipeline = [
  {
    "$match": {
      "Tags": "jquery",
      "CreationDate": {"$gte": datetime.datetime(2015, 1, 1, 0, 0, 0)}
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

# postcol.aggregate(pipeline)
print(pipeline)

pipeline['Tags'] = 'vuejs2'
