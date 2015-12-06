import state
import dfile
import e



def main_ui():
    state.compare_states()
    import e
    if (e.errors != []):
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
    if (var == "print old"):
        old_state = state.open_state()
        state.print_pretty(old_state)
    if (var == "print new"):
        state.print_pretty(state.current_state)
    if (var == "current"):
        state.show_attached()
    if (var == "errors"):
        for error in state.errors:
            print error
            print state.errors[error]
            print "\n"
    if (var == "add"):
        pass

def error_stuff():
    #print "LOOP"
    e.print_all
    for error in e.errors:
        edrive = error["Drive"]
        print error
        if (error["Problem"] == "Unknown_drive"):
            print "\n New Drive detected: %s " % edrive
            vart = raw_input("Add drive to databse?")
            if (vart == "y"):
                state.add_drive_to_state(error["Drive"], state.old_state)
                state.current_state = state.current_state
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
        if "size_mismatch" in e.errors[0]:
            cdrive = error
            ans = raw_input("Use current drive data?")
            if (ans == "y"):
                print "Adding drive %s to state" % cdrive
                state.add_drive_to_state(cdrive, state.old_state)
                #state.print_pretty(state.current_state)
                state.save_entire_state(state.current_state)
                state.open_state()
                print "state.errors"
                print state.errors
                del state.errors[cdrive]
            
        main_ui()