import os
import testStatus
#v_path = "/home/../../Volumes"


def get_drive_list(v_path):
    drives = os.listdir(v_path)
    drive_list = []
    print drives
    for drive in drives:
        print "checking drive %s" % drive
        if (os.path.isdir("%s/%s/Project Media" % (v_path, drive))):
            drive_list.append(drive)
    return drive_list

def get_projects(v_path, drive):
    if drive != "Macintosh HD":
        if drive != "Project Media 2":
            projects = os.listdir("%s/%s/Project Media" % (v_path, drive))
        if drive == "Project Media 2":
            projects = os.listdir("%s/%s" % (v_path, drive))
        projects.remove(".DS_Store")
        return projects

def print_all(v_path, drive_list):
    for drive in drive_list:
            print "\n"
            print drive
            print_projects(v_path, drive)

def print_projects(v_path, drive):
    projects = get_projects(v_path, drive)
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


