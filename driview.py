import dfile
import state





    
drive_list = dfile.get_drive_list()



old_state = state.open_state()
current_state = state.make_status(drive_list)

state.compare_states(old_state, current_state)
#status.print_pretty(old_state)


#print current_state
#for project in current_state["Hard Drive U"]:
#    print project
#    print(dfile.get_size("Hard Drive U", project))