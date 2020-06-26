import sys
import os
import datetime

dir=sys.argv[1]
file_list=os.listdir()
for file in file_list:
    print(file,os.stat(file).st_size,
          datetime.datetime.fromtimestamp(os.stat(file).st_mtime))
