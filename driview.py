import testStatus
import status
#import os
#from sys import platform as _platform

v_path = "./Volumes"


#if _platform == "linux" or _platform == "linux2":
#    v_path = "/home/../../media/parker"
#elif _platform == "darwin":
#    v_path = "/home/../../Volumes"
#elif _platform == "win32":
#    v_path = "/home/../../Volumes"# Windows...

pm = ["Project Media", "ProjectMedia", "PROJECT MEDIA"]







def print_all(drives):
    for drive in drives:
            print "\n"
            print drive
            print_projects(drive)

def print_projects(drive):
    projects = get_projects(drive)
    for project in projects:
        print project
        size = get_size("%s/%s/Project Media/%s" % (v_path, drive, project))
        print "%s bytes" % size

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            return total_size

#drives = get_drives(v_path)
#print_all(drives)

x = status.status()
x.build(v_path)
x.write()
#testStatus.test(drives)
