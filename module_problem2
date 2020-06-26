import sys
import os

dir=sys.argv[1]
file_list=os.listdir(dir)
print(file_list)

ext_dict={}

for file in file_list:
    if(len(file.split('.'))>1):
        ext=file.split('.')[1]
        ext_dict[ext] = ext_dict.get(ext, 0) + 1

for ext,count in ext_dict.items():
    print(ext, count)
