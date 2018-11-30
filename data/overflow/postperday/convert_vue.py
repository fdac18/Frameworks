import requests, re, json, sys
from dateutil import parser
import datetime

posts1 = []
posts2 = []

with open("vue.json", "r") as f:
  posts1 = json.loads(f.read())

with open("vue2.json", "r") as f:
  posts2 = json.loads(f.read())


j = []
check = {}
for post in posts1:
  d = post['_id']
  s = d.split('-')
  date = datetime.date(int(s[0]), int(s[1]), int(s[2]))
  ds = date.strftime("%Y-%m-%d")
  if ds in check:
    check[ds] += post['c']
  else:
    check[ds] = post['c']

for post in posts2:
  d = post['_id']
  s = d.split('-')
  date = datetime.date(int(s[0]), int(s[1]), int(s[2]))
  ds = date.strftime("%Y-%m-%d")
  if ds in check:
    check[ds] += post['c']
  else:
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

for key in check:
  j.append({
    'c': check[key],
    'd': key
  })

j = sorted(j, key=lambda x: datetime.datetime.strptime(x['d'], '%Y-%m-%d').timestamp())
with open("vue_overflow.json", "w+") as f:
  json.dump(j, f)