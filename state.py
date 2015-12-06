import dfile
global errors
import os
errors = {}

global s_path
s_path = "./state.txt"

def make_state():
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
    f = open('%s' % s_path, 'w')
    s = str(state)
    f.write(s)

def open_state():
    if (os.path.exists("%s" % s_path)):
        f = open('%s' % s_path, 'r').read()
        state = eval(f)
        return state
    else:
        errors["No_state"] = s_path
    
def compare_states():
    for new_drive in current_state:
        fnd = "f"
        for old_drive in old_state:
            if (new_drive == old_drive):
                fnd = "t"
        if (fnd == "t"):
           familiar_drive(new_drive, old_state)
        else:
            errors["Unknown_drive"] = new_drive
            unkown_drive(new_drive)
     
def unkown_drive(new_drive):  
    #print "\n New Drive detected: %s " % new_drive
    var = "n"#var = raw_input("Add drive to databse?")
    if (var == "y"):
        trial = old
        add_drive_to_state(new_drive, trial)
        print_pretty(trial)
        ask = raw_input("Is this okay?")
        if (ask =="y"):
            save_entire_state(trial)
        else:
            old_state = open_state()

def familiar_drive(new_drive, old_state):
    if (dfile.make_project_dict(new_drive) == old_state[new_drive]):
        pass
        #print "projects match"
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
    
def show_attached():
    for drive in current_state:
        if drive in old_state:
            print "Drive %s found in database" % drive
        if drive not in old_state:
            print "New drive: %s found" % drive
        

global old_state

global current_state