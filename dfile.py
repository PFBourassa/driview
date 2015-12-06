import os
import testStatus
#v_path = "/home/../../Volumes" #linux
v_path = "./../../../../Volumes" #osx

def get_drive_list():
    drives = os.listdir(v_path)
    drive_list = []
    for drive in drives:
        if (os.path.isdir("%s/%s/Project Media" % (v_path, drive))):
            drive_list.append(drive)
    return drive_list

def print_projects(drive):
    projects = get_projects(drive)
    for project in projects:
        print project
        size = get_size("%s/%s/Project Media/%s" % (v_path, drive, project))
        print "%s bytes" % size

def get_size(drive, project):
    start_path = "%s/%s/Project Media/%s" % (v_path, drive, project)
    total_size = getFolderSize(start_path)
    return total_size


def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size


def make_project_dict(drive):
    project_dict = {}
    projects = os.listdir("%s/%s/Project Media" % (v_path, drive))
    projects.remove(".DS_Store")
    for project in projects:
        if ".fcpbundle" not in project:
            project_dict[project] = get_size(drive, project)
        #print project
    return project_dict
  
"""    
def has_Project_Media(v_path, drive):
    if (os.path.isdir("%s/%s/Project Media" % (v_path, drive))):
        return True
    if (os.path.isdir("%s/%s/Project Media " % (v_path, drive))):
        return True
    if (os.path.isdir("%s/%s/Project media" % (v_path, drive))):
        return True
"""