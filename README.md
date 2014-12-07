Driview
=======

Summary
-------
Files and projects move around, and computers are much better bookkeepers than any human. I propose a peice of software that will automatically search hard drives as they are available, and maintain a list of where project media is located. This program will make no changes to the content, or organization of the drives, it will simply present it’s findings in a human-readable format.

Interface
---------
This should be dead simple. 
It can run in the background at all times without taking away CPU resources.

When a drive is plugged in to a computer with this program running,
the software will automatically search through the folders until it finds “ProjectMedia,” 
it will then take the names of all the folders inside that folder eg.
“AllentownArtMuseum,” or 
“MS” 
and assume that (at least some of) the video files 
for that project are located on that drive.

This requires the human action of creating a folder named “ProjectMedia” on each drive, and each new drive that we buy. 
It also requires the human action of putting all projectmedia, in that folder, and naming it correctly.

All of the information collected by this method will be shown to the user through a browser.
This could be hosted on server space,  or put into a Trello board. 

Limitations
-----------
Driview cannot make changes to the hard drives. This is intentional.
It means that driview cannot mistakenly make exrta copies,
or accidently delete valueable material.
Other programs are much better suited to do these tasks.

Driview cannot see inside FCPX Libraries (yet!)
This means that driview cannot tell users whether FCP knows where the footage is.
This means that if project media lives inside a FCP library, but not in the /ProjectMedia folder, it will be invisible to driview, and may appear to be missing.
