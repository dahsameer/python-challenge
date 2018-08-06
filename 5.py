#http://www.pythonchallenge.com/pc/def/peak.html

from urllib import request
import pickle

result = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
resulttext = result.read().decode("utf-8")
filename = "banner.p"
outfile = open(filename, 'w')
for words in resulttext:
    outfile.write(words)
outfile.close()

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

for line in new_dict:
    for c,n in line:
        for i in range(n):
            print(c,end='')
    print()