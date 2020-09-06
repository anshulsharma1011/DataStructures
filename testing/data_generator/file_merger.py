from os import listdir
from os.path import isfile, join
from datetime import datetime

mypath = "D:\\DS_ALGO\\testing\\data\\"
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open('file3.txt', 'w') as outfile:
    print(datetime.now())
    outfile.write("arr=")
    outfile.write("[")
    for names in filenames:
        with open(mypath+names) as infile:
            outfile.write(infile.read())
    outfile.write("0")
    outfile.write("]")
    print(datetime.now())