import requests, re, json, sys
from dateutil import parser
import datetime

repos = ['react', 'angular', 'vue', 'backbone', 'ember.js', 'jquery']

for i in range(len(repos)):
  issues = []
  with open("%s_docs.json" % repos[i], "r") as f:
    issues = json.loads(f.read())

  dates = {}

  d = datetime.date(2015, 1, 10)
  while True:
    s = d.strftime("%Y-%m-%d")
    dates[s] = 0
    if d.year == 2018 and d.month == 11 and d.day == 30:
      break
    d = d + datetime.timedelta(days=1)

  for issue in issues:
    date = parser.parse(issue['date']).strftime("%Y-%m-%d")
    if date in dates:
      dates[date] += 1
    else:
      dates[date] = 1 

  j = []
  for (date, count) in dates.items():
    j.append({
      'c': count,
      'd': date
    })
  j = sorted(j, key=lambda x: datetime.datetime.strptime(x['d'], '%Y-%m-%d').timestamp())

  with open("%s_issues_by_day.json" % repos[i], "w+") as f:
    json.dump(j, f)