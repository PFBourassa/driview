#  Status is the fundamental unit of driveiew.

#  status = {
#  'Hard Drive A' : [CSC, Wigs, Etc],
#  'Hard Drive B' : [Childrens home of easton]
#  }
import dfile

def make_staus(drive_list):
    #drive_list = dfile.get_drive_list()
    state = {}
    for drive in drive_list:
        projects = dfile.get_projects(drive)
        state[drive] = projects
    return state

def print_pretty(state):
    for drive in state:
        print drive
        for project in state[drive] :
            print project

def save_entire_state():
    f = open('state', 'w')
    s = str(state)
    f.write(s)

def open_state():
    f = open('state', 'r').read()
    state = eval(f)
    return state
    
def compare_to_state(new_drive, state):
    for drive in state:
        if (new_drive == drive):
            print "Found: %s" % new_drive
            if (dfile.get_projects(new_drive) == dfile.get_projects(drive)):
                print "projects match"
        
        
"""
test_status = {
    'Hard Drive A':
        [
            CSC, 
            Wigs, 
            CareNow
        ],
    'Hard Drive B':
        [
            Childrens Home,
            Older Adults,
            State Theater,
            Allentown Art Museum
        ]
}

status = {}


def grab_drive(drive):
    return status[drive]

def list_projects(d):
    drive = grab_drive(d)
    project_list = []
    for p in d:
        project.append(p)
    return project_list

def add_drive(drive):
    status[drive] = []

def remove drive(drive):
    #mark drive as "removed"

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
"""