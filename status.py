#  Status is the fundamental unit of driveiew.

import os
from sys import platform as _platform

test_status = {
    "Hard Drive A":
        ["Example", "CSC", "Peanuts", "Wigs"],
    "Hard Drive B":
        ["Example","Peanuts","CSC","Wigs", "Art Museum"]
}

def get_drives(v_path):
    drives = os.listdir(v_path) #["Hard Drive A", "B"]
    if "Macintosh HD" in drives :
        drives.remove("Macintosh HD")
    return drives

def not_pm(drive):
    if drive != "Project Media 1":
        if drive != "Project Media 2":
            if drive != "Project Media 3":
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def get_projects(drive, v_path):
    if not_pm(drive):
        projects = os.listdir("%s/%s/Project Media" % (v_path, drive))
    else:
        projects = os.listdir("%s/%s" % (v_path, drive))
    if _platform == "darwin":
        projects.remove(".DS_Store")
    return projects

class status:
    """the funamental snapshot of driview"""
    content = {}
    def build(self, v_path):
        drives = get_drives(v_path)
        for drive in drives:
            self.content[drive] = []
            projects = get_projects(drive, v_path)
            for project in projects:
                self.content[drive].append(project)
    def write(self):
        for drive in self.content:
            print "\n"
            print drive
            for project in self.content[drive]:
                print project
    
    #tel['guido'] = 4127
    
def list_projects(d):
    drive = grab_drive(d)
    project_list = []
    for p in d:
        project_list.append(p)
    return project_list

def add_drive(drive):
    status[drive] = []

def update_status(old,new):
    for hard_drive in new:
        if old[hard_drive]:
            old[hard_drive] = hard_drive #Add a new hard drive
            #Create a new Trello list
        if old[hard_drive] != hard_drive:
            old[hard_drive] = hard_drive #Update the old status

def update_drive(drive, status):
    for project in listProjects(drive):
        if status[drive] == 0:
            status[drive] = drive

def print_status(status):
    for drive in status:
        print "%s: " % drive
        for project in drive:
            print "%s" % project 
            
def checkforduplicates(status):
    project_list = []
    for drive in status:
        for project in drive:
            project_list.append(project)
            
    