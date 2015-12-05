import dfile
import status





    
drive_list = dfile.get_drive_list()
#dfile.print_all(drives)

old_state = status.open_state()
current_state = status.make_status(drive_list)

for drive in drive_list:
    status.compare_to_state(drive, old_state)
#status.print_pretty(old_state)

#print current_state
#for project in current_state["Hard Drive U"]:
#    print project
#    print(dfile.get_size("Hard Drive U", project))