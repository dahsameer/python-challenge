#http://www.pythonchallenge.com/pc/def/linkedlist.html
import urllib
from urllib import request
import re

baseurl="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
querystring="12345" #because the  first link given is  12345


for i in range(1,400):
    print(i," - ",querystring)
    if i == 86:
        nextstring = int(querystring)/2
        nextstring = str(nextstring)
    else:
        result = request.urlopen(baseurl+querystring)
        resulttext = result.read().decode("utf-8")
        matchpattern = re.search(r'\d+$',resulttext,re.M)
        if not matchpattern:
            print(resulttext)
            break
        nextstring = matchpattern.group()
    querystring = nextstring