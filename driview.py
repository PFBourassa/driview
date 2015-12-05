import dfile
import status





    
drive_list = dfile.get_drive_list()
#dfile.print_all(drives)

state = status.open_state()
for drive in drive_list:
    status.compare_to_state(drive, state)