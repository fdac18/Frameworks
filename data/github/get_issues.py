import requests, re, json, sys

issues_api = "https://api.github.com/repos/{owner}/{repo}/issues?per_page=100&state=all"

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
  issues = []
  url = issues_api.format(owner=owners[i], repo=repos[i])
  req, next_link = api_helper(url)
  while req.status_code is not 403 or next_link is not None:
    temp_issues = json.loads(req.text)
    temp_issues[:] = [issue for issue in temp_issues if 'pull_request' not in issue]
    issues.extend(temp_issues)
    if next_link is not None:
      req, next_link = api_helper(next_link)
    else:
      break

  with open("%s_issues_dirty.json" % repos[i], "w+") as f:
    json.dump(issues, f)