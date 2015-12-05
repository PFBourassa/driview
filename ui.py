import state
import dfile

def main_ui():
    old_state = state.open_state()
    current_state = state.make_status()
    state.compare_states(old_state, current_state)
    var = raw_input("What do you want to do?: ")
    if (var == "scan"):
        current_state = state.make_status()
        state.compare_states(old_state, current_state)
    if (var == "save"):
        confirm = raw_input("Are you sure, this will overwrite the old state?")
        if (confirm == "y"):
            print "ok"
            current_state = state.make_status()
            state.save_entire_state(current_state)
        if (confirm == "n"):
            print "ok"
    if (var == "print"):
        old_state = state.open_state()
        state.print_pretty(old_state)