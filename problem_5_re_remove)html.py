from urllib.request import urlopen
import re
import sys

#url=sys.argv[1]
url="https://summerofcode.withgoogle.com/archive/2018/organizations/"
request=urlopen(url)
content=request.read()

print(content)

content=re.sub(r'<.*?>', '',content.decode('utf-8'),flags=re.S)
print(content)
