import dfile

def make_status():
    drive_list = dfile.get_drive_list()
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
    for new_drive in new:
        fnd = "f"
        print "Checking for %s..." % new_drive
        for old_drive in old:
            print "Comparing to %s" % old_drive
            if (new_drive == old_drive):
                fnd = "t"
        if (fnd == "t"):
            print "\n Found: %s \n" % new_drive
            compare_to_state(new_drive, old)
        else:
            print "\n New Drive detected: %s " % new_drive
            var = raw_input("Add drive to databse?")
            if (var == "y"):
                trial = old
                add_drive_to_state(new_drive, trial)
                print_pretty(trial)
                ask = raw_input("Is this okay?")
                if (ask =="y"):
                    save_entire_state(trial)
                else:
                    old_state = open_state()

def compare_to_state(new_drive, old_state):
    if (dfile.make_project_dict(new_drive) == old_state[new_drive]):
        print "projects match"
    else:
        print """#################################
WOAH! LOOKOUT, SOMETHING IS WORNG
#################################"""
        var = raw_input("should we let this go?")
        
def add_drive_to_state(drive, state):
    current_state = make_status()
    #print current_state[drive]
    #print "\n"
    #print_pretty(state)
    state[drive] = current_state[drive]
    #print_pretty(state)