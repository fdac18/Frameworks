import json

repos = ['react', 'angular', 'vue', 'backbone', 'ember.js', 'jquery']
fields = ['comments_url', 'data', 'date']

for repo in repos:
  with open('%s_issues.json' % repo, 'r') as dirty:
    issues = json.loads(dirty.read())
    for issue in issues:
      issue['data'] = '%s %s' % (issue['title'], issue['body'])
      issue['date'] = issue['created_at']
      for field in list(issue.keys()):
        if field not in fields:
          del issue[field]

  with open('%s_docs.json' % repo, 'w+') as docs:
    json.dump(issues, docs)