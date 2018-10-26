import json, os


repos = ['react', 'angular', 'vue', 'backbone', 'ember.js', 'jquery']

data = {}

for repo in repos:
  with open('%s_issues_clean.json' % repo, 'r') as clean:
    issues = json.loads(clean.read())
    for issue in issues:
      try:
        data[issue['d']].append(issue)
      except KeyError:
        data[issue['d']] = []

  with open('%s_comments_clean.json' % repo, 'r') as clean:
    comments = json.loads(clean.read())
    for comment in comments:
      try:
        data[comment['d']].append(comment)
      except KeyError:
        data[comment['d']] = []

for key in data.keys():
  time = key.split('/')
  path = '../data_by_month/%s-%s' % (time[0], time[1])
  if os.path.isdir(path) is not True:
    os.mkdir(path)
  with open(path + '/data.json', "w+") as f:
    json.dump(data[key], f)

