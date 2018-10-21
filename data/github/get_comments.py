import requests, json, sys, time, datetime

comments_api = "https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments"

owners = ['facebook', 'angular', 'vuejs', 'jashkenas', 'emberjs']
repos = ['react', 'angular', 'vue', 'backbone', 'ember.js']

if len(sys.argv) is not 3:
  exit()

user = sys.argv[1]
token = sys.argv[2]

def api_helper(url):
  req = requests.get(url, auth=(user, token))
  while req.status_code == 403:
    print("sleeping at", str(datetime.datetime.now()))
    time.sleep(65 * 60)
    print("waking up at ", str(datetime.datetime.now()))
    req = requests.get(url, auth=(user, token))
  next_link = req.links['next']['url'] if 'next' in req.links else None
  return req, next_link

for i in range(len(owners)):
  comments = []
  
  with open("%s_issues_clean.json" % repos[i], "r") as js:
    issues = json.loads(js.read())
    for issue in issues:
      url = comments_api.format(owner=owners[i], repo=repos[i], number=issue['num'])
      req, next_link = api_helper(url)
      while req.status_code is not 403 or next_link is not None:
        temp_comments = json.loads(req.text)
        comments.extend(temp_comments)
        if next_link is not None:
          req, next_link = api_helper(next_link)
        else:
          break

    with open("%s_comments_dirty.json" % repos[i], "w+") as f:
      json.dump(comments, f)