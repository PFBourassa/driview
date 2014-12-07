import fnmatch
import os
import getpass
                
def findHardDrives():
    home = os.environ['HOME']
    os.chdir(home)
    user = getpass.getuser()
    for dirName, subdirlist, flist in os.walk('./../../media/parker'):
        return subdirlist

def findProjectMedia(drive):
    for root, dirs, files in os.walk(drive):
        for file in fnmatch.filter(dirs,'ProjectMedia'):
            pm = os.path.join(root, file)
            return pm
            
def listProjects(drive):
    pm = findProjectMedia(drive)
    return os.listdir(pm)
            
#print listProjects(findProjectMedia("./Hard drive A"))
print findHardDrives()