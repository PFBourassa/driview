status = {}

def update_status(old,new):
    for hard_drive in new:
        if old[hard_drive]:
            old[hard_drive] = hard_drive #Add a new hard drive
            #Create a new Trello list
        if old[hard_drive] != hard_drive:
            old[hard_drive] = hard_drive #Update the old status

