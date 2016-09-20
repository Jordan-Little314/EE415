#System Crawler to familiarize with how mobile file heierarchy works
#This is mainly just a warmup to understand python and mobile devices
import os, operator, sys

#Walks through and prints out all files and directories
#rootDir = '/run/user/1000/gvfs/afc:host=db0a6e7a33ffe3790ce2e744f772f098aadcbd19'
#for dirName, subdirList, fileList in os.walk(rootDir):
#    print('Found directory: %s' % dirName)
#    for fname in fileList:
#Walks
#        print('\t%s' % fname)#

f = open('iPhoneSysStats.txt', 'w')

dirpath = '/run/user/1000/gvfs/afc:host=db0a6e7a33ffe3790ce2e744f772f098aadcbd19'

all_files = (filename for basedir, dirs, files in os.walk(dirpath) for filename in files)
files_and_sizes = ((path, os.path.getsize(path)) for path in all_files)
sorted_files_with_size = sorted(files_and_sizes, key = operator.itemgetter(1))

#print(sorted_files_with_size)
orig_stdout = sys.stdout
sys.stdout = f

totalBytes = 0

for x,y in sorted_files_with_size:
    print(x + "\t" + str(y))
    totalBytes += y
print ("\n\n\nTotal bytes: " + str(totalBytes))
sys.stdout = orig_stdout
f.close()
