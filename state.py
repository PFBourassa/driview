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
    fnd = "f"
    for new_drive in new:
        fnd = "f"
        for old_drive in old:
            if (new_drive == old_drive):
                fnd = "t"
        if (fnd == "t"):
            print "Found: %s" % new_drive
            compare_to_state(new_drive, old)
        else:
            print "New Drive detected: %s " % new_drive

def compare_to_state(new_drive, old_state):
    if (dfile.make_project_dict(new_drive) == old_state[new_drive]):
        print "projects match"
    else:
        print "####*****WOAH! LOOKOUT, SOMETHING IS WORNG*****####"