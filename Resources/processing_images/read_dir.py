from os import listdir, chdir, walk
from os.path import isfile, join



chdir("/Volumes/1TBHDD/code/")


onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]

print(onlyfiles)

f = []
for (dirpath, dirnames, filenames) in walk('.'):
    f.extend(filenames)
    f.extend(dirnames)

print(f)