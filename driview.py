import os
v_path = "/home/../../Volumes"

def get_drives(v_path):
    drives = os.listdir(v_path)
    drives.remove("Macintosh HD")
    return drives

def get_projects(drive):
    if drive != "Macintosh HD":
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