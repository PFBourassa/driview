import dfile
import status


drive_list = dfile.get_drive_list()
#dfile.print_all(drives)

state = status.make_staus(drive_list)
status.print_pretty(state)