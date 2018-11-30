import requests, re, json, sys
from dateutil import parser
import datetime

issues_api = "https://api.github.com/repos/{owner}/{repo}/commits?since=2015-01-10T00:00:00"

owners = ['facebook', 'angular', 'vuejs', 'jashkenas', 'emberjs', 'jquery']
repos = ['react', 'angular', 'vue', 'backbone', 'ember.js', 'jquery']

if len(sys.argv) is not 3:
  exit()

user = sys.argv[1]
token = sys.argv[2]

def api_helper(url):
  req = requests.get(url, auth=(user, token))
  next_link = req.links['next']['url'] if 'next' in req.links else None
  return req, next_link


for i in range(len(owners)):
  commits = {}
  
  d = datetime.date(2015, 1, 10)
  while True:
    s = d.strftime("%Y-%m-%d")
    commits[s] = 0
    if d.year == 2018 and d.month == 11 and d.day == 30:
      break
    d = d + datetime.timedelta(days=1)
    print(s)

  url = issues_api.format(owner=owners[i], repo=repos[i])
  req, next_link = api_helper(url)

  while req.status_code is not 403 or next_link is not None:
    temp_commits = json.loads(req.text)
    for temp_commit in temp_commits:
      date = parser.parse(temp_commit['commit']['author']['date']).strftime("%Y-%m-%d")
      if date not in commits:
          commits[date] = 1
      else:
          commits[date] += 1

    if next_link is not None:
      req, next_link = api_helper(next_link)
    else:
      break

  j = []
  for (date, count) in commits.items():
    j.append({
      'c': count,
      'd': date
    })
  j = sorted(j, key=lambda x: datetime.datetime.strptime(x['d'], '%Y-%m-%d').timestamp())
  with open("%s_commits.json" % repos[i], "w+") as f:
    json.dump(j, f)