#  Status is the fundamental unit of driveiew.

#  status = {
#  'Hard Drive A' : [CSC, Wigs, Etc],
#  'Hard Drive B' : [Childrens home of easton]
#  }
import dfile

def make_status(drive_list):
    #drive_list = dfile.get_drive_list()
    state = {}
    for drive in drive_list:
        project_dict = dfile.make_project_dict(drive)
        state[drive] = project_dict
    return state

def print_pretty(state):
    for drive in state:
        print "\n"
        print drive
        print "------"
        for project in state[drive] :
            print "%s: %s" % (project, state[drive][project])

def save_entire_state(state):
    f = open('state', 'w')
    s = str(state)
    f.write(s)

def open_state():
    f = open('state', 'r').read()
    state = eval(f)
    return state
    
def compare_states(old, new):
    for drive in new:
        compare_to_state(drive, old)

def compare_to_state(new_drive, old_state):
    for drive in old_state:
        if (new_drive == drive):
            print "Found: %s" % new_drive
            if (dfile.make_project_dict(new_drive) == old_state[drive]):
                print "projects match"
            else:
                print "####*****WOAH! LOOKOUT, SOMETHING IS WORNG*****####"

    
"""
    new_proj_dict = dfile.make_project_dict(new_drive)
    #print new_proj_dict
    for project in old_state[drive]:
        print "%s: %s" % (project, old_state[drive][project])"""