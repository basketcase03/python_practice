import sys
import os

dir=sys.argv[1]
def get_files(dir,num):
    file_list=os.listdir(dir)
    for file in file_list:
        try:
            new_files=os.listdir(dir+"\\"+file)
            print('|','-'*2*num,file)
            get_files(dir+"\\"+file,num+2)
        except:
            print('|','-'*2*num,file)

get_files(dir,1)
        
