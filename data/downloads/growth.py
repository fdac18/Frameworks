import json, sys

# old_month is in the format YYYY-MM
# new_month is in the format YYYY-MM
def find_growth_between(pkg, old_month, new_month):
  with open("%s.json" % pkg, "r") as f:
    j = json.loads(f.read())
    dates = j['downloads']
    dl_rate = {}
    for date in dates:
      ymd = date['day'].split('-')
      ym = ymd[0] + '-' + ymd[1]
      if ym not in dl_rate:
        dl_rate[ym] = date['downloads']
      else:
        dl_rate[ym] += date['downloads']
    old_dl = dl_rate[old_month]
    if (old_dl == 0): old_dl = 1
    new_dl = dl_rate[new_month]
    if (new_dl == 0): new_dl = 1
    percent = ((new_dl / old_dl) - 1) * 100
    change = 'grew'
    if (percent < 0):
      change = 'declined'
    percent_str = float("{0:.2f}".format(percent))

    return percent, "{}'s download rate {} by {}% between {} and {}".format(pkg, change, percent_str, old_month, new_month), dl_rate

if __name__ == '__main__':
  pkg = sys.argv[1]
  old_month = sys.argv[2]
  new_month = sys.argv[3]
  percent, growth_str, dl_rates_by_month = find_growth_between(pkg, old_month, new_month)
  print(growth_str)