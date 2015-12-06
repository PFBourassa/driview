import state

global projects
projects = []

def init():
    i = 0
    for drive in state.old_state:
        for p in state.old_state[drive]:
            q = {"Name": p, "Copies": 1}
            if q not in projects:
                projects.append({"Name": p, "Copies": 1})
                print p
            elif q in projects:
                print "%s is a duplicate" % p
                try:
                   id = projects.index(q)
                   q["Copies"] += 1
                   projects[id] = q
                except:
                   print "Not Found"

def do():
    for p in projects:
        pass

def print_good():
    for p in projects:
        print p
        
