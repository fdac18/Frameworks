import json

pkgs = ["jquery", "react", "angular", "vue", "backbone", "ember-source"]

for pkg in pkgs:
  with open("%s.json" % pkg, "r") as f:
    j = json.loads(f.read())
    stripped = []
    for day in j['downloads']:
      stripped.append({
        'c': day['downloads'],
        'd': day['day']
      })
    with open("%s_downloads.json" % pkg, "w+") as ff:
      json.dump(stripped, ff)