import fnmatch
import os

matches = []
for root, dirs, files in os.walk('./Hard drive A'):
    for file in fnmatch.filter(dirs, 'ProjectMedia'):
        pm = os.path.join(root, file)
        for r, d, f in os.walk(pm):
            if d  != []:
                print "\n"
                
def findHardDrives():
    for dirName, subdirlist, flist in os.walk('./../../../../media'):
        return subdirlist
    
def findProjectMedia(drive):
    for root, dirs, files in os.walk(drive):
        for file in fnmatch.filter(dirs,'ProjectMedia'):
            pm = os.path.join(root, file)
            return pm
            
def listProjects(pm):
    for r, d, f in os.walk(pm):
        if d != []:
            print d
    
print "findHardDrive returned:"
print findHardDrives()
print "\n"
print findProjectMedia("./Hard drive A")
print listProjects(findProjectMedia("./Hard drive A"))