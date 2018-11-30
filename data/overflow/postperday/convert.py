import requests, re, json, sys
from dateutil import parser
import datetime

repos = ['react', 'angular', 'backbone', 'ember', 'jquery']

for i in range(len(repos)):

  with open("%s.json" % repos[i], "r") as f:
    posts = json.loads(f.read())

    j = []
    check = {}
    for post in posts:
      d = post['_id']
      s = d.split('-')
      date = datetime.date(int(s[0]), int(s[1]), int(s[2]))
      ds = date.strftime("%Y-%m-%d")
      j.append({
        'c': post['c'],
        'd': ds
      })
      check[ds] = post['c']

    d = datetime.date(2015, 1, 10)
    while True:
      s = d.strftime("%Y-%m-%d")
      if s not in check:
        j.append({
          'c': 0,
          'd': s
        })
      if d.year == 2018 and d.month == 11 and d.day == 30:
        break
      d = d + datetime.timedelta(days=1)

    j = sorted(j, key=lambda x: datetime.datetime.strptime(x['d'], '%Y-%m-%d').timestamp())
    with open("%s_overflow.json" % repos[i], "w+") as f:
      json.dump(j, f)