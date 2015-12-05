import dfile
import status




def save_entire_state():
    f = open('state', 'w')
    s = str(state)
    f.write(s)

def open_state():
    f = open('state', 'r').read()
    state = eval(f)
    return state
    
drive_list = dfile.get_drive_list()
#dfile.print_all(drives)

state1 = status.make_staus(drive_list)
state2 = open_state()
print (state1 == state2)
#status.print_pretty(state)