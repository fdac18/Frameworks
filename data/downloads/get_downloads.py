import requests, datetime, copy, json, sys

registry = "https://api.npmjs.org/downloads/range"
data = None
end_date = datetime.datetime.today()

if len(sys.argv) > 1:
  pkgs = sys.argv[1:]
else:
  pkgs = ["jquery", "react", "angular", "vue", "backbone", "ember-source"]

for pkg in pkgs:
  start_date = datetime.datetime(2015, 1, 10)
  while True:
    days = (end_date - start_date).days
    if days <= 0:
      break
    days = days if days < 365 else 365
    temp_date = start_date + datetime.timedelta(days=days)

    begin = start_date.strftime("%Y-%m-%d")
    end = temp_date.strftime("%Y-%m-%d")
    req = requests.get("{0}/{1}:{2}/{3}".format(registry, begin, end, pkg))
    if req.status_code == 200:
      temp_data = json.loads(req.text)
    else:
      print("Error, exited with request code %d" % req.status_code)
      exit

    if data is None:
      data = temp_data
    else:
      data['end'] = temp_data['end']
      data['downloads'].extend(temp_data['downloads'])

    start_date = temp_date

  with open("%s.json" % pkg, "w+") as f:
    json.dump(data, f)
  data = None

