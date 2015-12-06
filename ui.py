import state
import dfile



def main_ui():
    state.compare_states()
    if (state.errors != {}):
        error_stuff()
    var = raw_input("What do you want to do?: ")
    if (var == "scan"):
        state.compare_states()
        state.show_attached()
    if (var == "save"):
        confirm = raw_input("Are you sure, this will overwrite the old state?")
        if (confirm == "y"):
            print "ok"
            current_state = state.make_state()
            state.save_entire_state(current_state)
        if (confirm == "n"):
            print "ok"
    if (var == "print"):
        old_state = state.open_state()
        state.print_pretty(old_state)
    if (var == "current"):
        state.show_attached()
    if (var == "add"):
        pass

def error_stuff():
    print state.errors
    for error in state.errors:
        print error
        if (str(error) == "Unknown_drive"):
            print "\n New Drive detected: %s " % state.errors[error]
            var = raw_input("Add drive to databse?")
        if (str(error) == "No_state"):
            print "Open state.py, and set a new s_path"
            ans = raw_input("Would you like to set a new s_path now?")
            if (ans == "y"):
                state.s_path = raw_input("Where?")
            if (ans == "n"):
                pass
            q = (raw_input("You can save to the current s_path. y/n"))
            if (q == "y"):
                confirm = raw_input("Are you sure, this will overwrite the old state?")
                if (confirm == "y"):
                    print "ok"
                    current_state = state.make_state()
                    state.save_entire_state(current_state)
                if (confirm == "n"):
                    print "ok"
        main_ui()