from urllib.request import urlopen
import sys
import os

#url=sys.argv[1]
url="http://docs.python.org/tutorial/"
response=urlopen(url)

content=response.read()
try:
    file=open(os.path.basename(url),'wb')
    print(os.path.basename(url))
except:
    file=open('index.txt','wb')
    
file.write(content)
file.close()
print(os.path.basename(url))
