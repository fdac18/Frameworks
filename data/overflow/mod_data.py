from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("."):
    f.extend(filenames)
    for afile in filenames:
        if '.json' in afile:
            print(afile)
    break

print(f)
