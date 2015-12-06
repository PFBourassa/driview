import dfile
import state
import ui


state.old_state = state.open_state()
state.current_state = state.make_state()
    
#global drive_list
#drive_list = dfile.get_drive_list()




#state.compare_states(old_state, current_state)
#status.print_pretty(old_state)
for error in state.errors:
    ui.error_stuff()
        
ui.main_ui()

#print current_state
#for project in current_state["Hard Drive U"]:
#    print project
#    print(dfile.get_size("Hard Drive U", project))