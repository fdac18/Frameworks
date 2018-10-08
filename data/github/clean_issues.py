import json, os

repos = ['react', 'angular', 'vue', 'backbone', 'ember.js', 'jquery']
fields = ['url', 'comments_url', 'title', 'created_at', 'updated_at', 'body']

for repo in repos:
  with open('%s_issues_dirty.json' % repo, 'r') as dirty:
    issues = json.loads(dirty.read())
    for issue in issues:
      for field in list(issue.keys()):
        if field not in fields:
          del issue[field]
  with open('%s_issues_clean.json' % repo, 'w+') as clean:
    json.dump(issues, clean)
  os.remove('%s_issues_dirty.json' % repo)