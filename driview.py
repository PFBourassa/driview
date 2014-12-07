import os
from sys import platform as _platform

v_path = "/home/../../Volumes"

if _platform == "linux" or _platform == "linux2":
    v_path = "/home/../../media/parker"
elif _platform == "darwin":
    v_path = "/home/../../Volumes"
elif _platform == "win32":
    v_path = "/home/../../Volumes"# Windows...

def not_pm(drive):
    if drive != "Project Media 1":
        if drive != "Project Media 2":
            if drive != "Project Media 3":
                return true
            else:
                return false
        else:
            return false
    else:
        return false

def get_drives(v_path):
    drives = os.listdir(v_path)
    if "Macintosh HD" in drives :
        drives.remove("Macintosh HD")
    return drives

def get_projects(drive):
    if drive != "Project Media 2":
        projects = os.listdir("%s/%s/Project Media" % (v_path, drive))
    if drive == "Project Media 2":
        projects = os.listdir("%s/%s" % (v_path, drive))
    projects.remove(".DS_Store")
    return projects

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

drives = get_drives(v_path)
print_all(drives)