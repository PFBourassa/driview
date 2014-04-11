import fnmatch
import os

matches = []
for root, dirs, files in os.walk('./Hard drive A'):
    for file in fnmatch.filter(dirs, 'ProjectMedia'):
        #print dirs
        pm = os.path.join(root, file)
        for r, d, f in os.walk(pm):
            if d  != []:
                print d
        #print file
        #for folder in dirs:
        #matches.append(folder)
        #print folder
    
#matches = os.walk('ProjectMedia')
      
#print "I found these matches: "
#print matches