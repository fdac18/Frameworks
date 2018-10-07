import os, sys, requests, json, time
from bs4 import BeautifulSoup

def patch(j):
  unfilled = 0
  filled = 0
  errors = 0
  for pkg in j:
    if pkg.get('versions') is None:
      unfilled += 1
      time.sleep(1)
      r = requests.get("https://www.npmjs.com/advisories/" + str(pkg['id']) + "/versions")
      while r.status_code == 429:
        time.sleep(60)
        r = requests.get("https://www.npmjs.com/advisories/" + str(pkg['id']) + "/versions")
      t = r.text
      soup = BeautifulSoup(t, "html.parser")
      text = soup.get_text()
      ver = text[text.find('{"affected":'):text.find(',"events"')]

      try:
        versions = json.loads(ver)
      except ValueError:
        versions = None
        errors += 1

      if versions is not None:
        pkg['versions'] = versions
    else:
      filled += 1
  print('{0} out of {1} advisories were attempted to be patched in and {2} of those failed. {3} were already filled.'.format(unfilled, unfilled+filled, errors, filled))
  return j

if __name__ == "__main__":
  if os.path.exists(sys.argv[1]):
    with open(sys.argv[1], encoding="utf-8") as f, open('patched_advisories.json', 'w+', encoding="utf-8") as p:
      j = json.load(f)
      patched = patch(j)
      json.dump(patched, p, ensure_ascii=False)
