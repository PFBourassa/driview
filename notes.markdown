Status
======
Status is the fundamental unit of driveiew.

    status = {
    'Hard Drive A' : [CSC, Wigs, Etc],
    'Hard Drive B' : [Childrens home of easton]
    }

This will create a single master list, that can always be referenced.
Should driview always check against Trello.
The newest info should always trump older info.

Other Metadata
--------------
Each project should have other metedata associated with it, but I'm not sure where to keep it.

* Time last modified
* Time last seen
* Size
* Other instances
* Part of FCPX? (later on)
* Where last seen
* Where last modified


Another dictionary full of metadata would be possible, and it would require that no names be the same.

Maybe more of a series of dictionaries, one for each each project, and the "status" just references them all.

They would be kept in a text document somewhere on each machine.
And also on the status card on trello.
When a machine is updating to Trello, it will read as much possible, and replace what it just learned with the old.

Cron Help
=========
<http://www.unixgeeks.org/security/newbie/unix/cron-1.html>
<http://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800>
<http://www.scrounge.org/linux/cron.html>

Error Handling
==============
Driview will e-mail users when things go seriorsly wrong.
Hopefully, these problems will not be caused by driview, 
because it has no write/delete priveleges.

Email when:

* A folder is expected, but is not found.
* A folder is empty, but used to be full.
* A computer goes missing for a while.

Write a Trello comment when:

* A new drive is added
* A new folder is added
* A folder is expected, but mising, and has another copy
* An empty folder is found
* A second instance of a folder is found
* The contents of a folder have changed

Code Organization
=================
Installation consists of creating a cron job to run the python script.

status.py
---------
Responsible for updating the status of whatever drives are plugged in.
takes 'new' and 'old' as arguments.

drive.py
--------
Responsible for drive-specific tasks.

Each drive needs:
* Name
* Size
* Unused
* Last seen time
* Last seen location

Each Project needs:
* Name
* 

Trello Integration
==================

Interface
---------






Each hard drive will have a list.
Each Project will have a card.
If a project "lives" on more than one drive, that will be reflected.
Labels will represent the computer where the project was last seen.

Organization
------------
Trello will be the only centralized element, and the only peice that talks to any other peice.

A special card will be called "status" and will hold the current status in plain text.
This will be the status quo against which all new updates will be compared.

Because editing this will cause problems, only driview will have editing permissions for the board, but everyone else will have view permissions.

New info will always trump the status quo.

Logging
=======
Where will the logs be kept exactly?

TODO
====
Re-write not_pm()
exporter
