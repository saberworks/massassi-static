---
title: Camera Tutorial
author: Booto
email: booto@geocities.com
description: >
    Learn how to create cameras in Jedi Knight. They function much like
    (but not exactly) the ones in MotS.
date: 1998-04-07
category: jk
---

Author: Booto
  
**Note:** This tutorial covers each and every section of the Cog.
Understanding Cogs is an important skill editors need. If you, however,
do not wish to go that far into the details, please feel free to skip
down to the part that actually shows you [how to implement
cameras](#implement) into your level. I would suggest going through the
[elevator](/tutorials/elevators/) and [door
tutorials](/tutorials/doors), as they discuss very simple cogs. From
there, you will be able to understand all the parts of this one.  
  
Okay, I got an e-mail asking how to do cameras in levels, and I decided
to go through:

  - How to edit the camera cog for custom ones
  - Implement them in levels

This is the cog:  
  

> 
> 
>     # Jedi Knight Cog Script
>     #
>     # C3_CAMERAFF.COG
>     #
>     # This script will briefly show the effect of using the
>     # forcefield console to the player...
>     #
>     # [YB]
>     #
>     # (C) 1997 LucasArts Entertainment Co. All Rights Reserved
>     
>     flags=0x240
>     
>     symbols
>     
>     thing       console                          desc=console
>     thing       camera                           desc=camera_ghost
>     flex        delay=1.5                        desc=delay
>     
>     int         old_camera                       local
>     int         player                           local
>     int         active=0                         local
>     
>     message     activated
>     message     timer
>     
>     end
>     
>     # ===================================================================
>     
>     code
>     
>     activated:
>        if(active) Return;
>        active = 1;
>     
>        player = GetSourceRef();
>     
>        if(player == GetLocalPlayerThing())
>        {
>           SetActorFlags(player, 0xa00000);
>           old_camera = GetCurrentCamera();
>           SetCurrentCamera(0);
>           SetCameraFocus(0, camera);
>        }
>     
>        SetTimer(delay);
>     
>        Return;
>     
>     timer:
>        ClearActorFlags(player, 0xa00000);
>        SetCameraFocus(0, player);
>        SetCurrentCamera(old_camera);
>        active = 0;
>     
>        Return;
>     
>     end

I'll take you through it section by section:

> 
> 
>     # Jedi Knight Cog Script
>     #
>     # C3_CAMERAFF.COG
>     #
>     # This script will briefly show the effect of using the
>     # forcefield console to the player...
>     #
>     # [YB]
>     #
>     # (C) 1997 LucasArts Entertainment Co. All Rights Reserved
>     
>     flags=0x240

This is the header - everything after the \# character is ignored. the
flags=0x240 means that it is a local cog. Generally do not put this line
in your cogs if you do not know what it does  
  
Okay, that was easy. On to the next bit:

> 
> 
>     symbols
>     
>     thing       console                          desc=console
>     thing       camera                           desc=camera_ghost
>     flex        delay=1.5                        desc=delay
>     
>     int         old_camera                       local
>     int         player                           local
>     int         active=0                         local
>     
>     message     activated
>     message     timer
>     
>     end

This simply sets up all local object references and variables. The first
line is 'symbols.' This is needed at the start of the object and
variable declaration section.  
  
The next line tells what kind of variable it is. "Thing" is thing, "int"
is integer, and "message" means "call on some code in the cog when this
happens."  
  
I don't know what "desc = (x)" means - don't use it (not necessary).  
  
"Local" means that this is defined later in the code - it doesn't need a
value passed from the .jkl file.  
  
You use "end" after all symbols (objects, variables) are defined.  
  
Okay...got that?  
On to the code...  

> 
> 
>     code
>     
>     activated:
>        if(active) Return;
>        active = 1;
>     
>        player = GetSourceRef();
>     
>        if(player == GetLocalPlayerThing())
>        {
>           SetActorFlags(player, 0xa00000);
>           old_camera = GetCurrentCamera();
>           SetCurrentCamera(0);
>           SetCameraFocus(0, camera);
>        }
>     
>        SetTimer(delay);
>     
>        Return;
>     
>     timer:
>        ClearActorFlags(player, 0xa00000);
>        SetCameraFocus(0, player);
>        SetCurrentCamera(old_camera);
>        active = 0;
>     
>        Return;
>     
>     end

The 'code' bit is needed at the start of the code (like 'symbols' sort
of). "Activated" is one of the named messages in the symbols section.
Since this is attached to a thing, when a player tries to activate that
thing (usually a console in this case) this code is called.  

> 
> 
>     if(active) Return;
>        active = 1;

This bit checks to see if the code is already active. If so, it returns
to the game. If not, it sets active to true (1) and continues.  

> 
> 
>     player = GetSourceRef();
>     
>        if(player == GetLocalPlayerThing())
>        {
>           SetActorFlags(player, 0xa00000);
>           old_camera = GetCurrentCamera();
>           SetCurrentCamera(0);
>           SetCameraFocus(0, camera);
>        }
>     
>        SetTimer(delay);
>     
>        Return;

This puts the the activating player in the object handler "player."  
  
It then sees if the local player is the activating player. If so, it
sets the actor flags of the player to 0xa00000. It then records what
camera it has with:  

> 
> 
> ``` 
>       SetCurrentCamera(0);
>       SetCameraFocus(0, camera);
> ```

It sets the camera in the new thing's position (usually a ghost thing).
It then sets the timer to the delay length to the previously said amount
in the .jkl. It then returns to the game ( until 'timer' is called).  

> 
> 
>     timer:
>        ClearActorFlags(player, 0xa00000);
>        SetCameraFocus(0, player);
>        SetCurrentCamera(old_camera);
>        active = 0;
>     
>        Return;
>     
>     end

When timer is called (after 'delay' has passed), It clears the 0xa00000
actorflag. It then retrieves the old camera and sets the camera to
inactive(0). The code then returns to the game, and then the 'end'
keyword shows that it is the end of the code.  
  
You could change this so that it cycled through multiple camera
positions before returning.  
  
<span id="implement">**Implement the COG**</span>  
Okay that's the how to change it a bit, now on to how to implement them
(I will only show how to implement the original).  
  
Copy the code from here:  

> 
> 
>     # Jedi Knight Cog Script
>     #
>     # C3_CAMERAFF.COG
>     #
>     # This script will briefly show the effect of using the
>     # forcefield console to the player...
>     #
>     # [YB]
>     #
>     # (C) 1997 LucasArts Entertainment Co. All Rights Reserved
>     
>     flags=0x240
>     
>     symbols
>     
>     thing       console                          desc=console
>     thing       camera                           desc=camera_ghost
>     flex        delay=1.5                        desc=delay
>     
>     int         old_camera                       local
>     int         player                           local
>     int         active=0                         local
>     
>     message     activated
>     message     timer
>     
>     end
>     
>     # ==================================================================
>     
>     code
>     
>     activated:
>        if(active) Return;
>        active = 1;
>     
>        player = GetSourceRef();
>     
>        if(player == GetLocalPlayerThing())
>        {
>           SetActorFlags(player, 0xa00000);
>           old_camera = GetCurrentCamera();
>           SetCurrentCamera(0);
>           SetCameraFocus(0, camera);
>        }
>     
>        SetTimer(delay);
>     
>        Return;
>     
>     timer:
>        ClearActorFlags(player, 0xa00000);
>        SetCameraFocus(0, player);
>        SetCurrentCamera(old_camera);
>        active = 0;
>     
>        Return;
>     
>     end

TO HERE.  
  
Paste it into a new file (in notepad or MS-DOS edit) and save it as
camera.cog. Make sure to save it as "text only" or it won't work
right.  
  
Now save that file in your projects directory. Open up Jed and go to the
tools menu and click on "placed cogs."  
  
Now go to "add cog." On the bar on the left there are two things -
"project directory" and "res2.gob."  
  
Click on "project directory." The camera.cog should be there, so add
that cog.  
  
Now there are 3 things you can pass insert into the cog:  
  

> 
> 
> |                    |                                                                        |
> | ------------------ | ---------------------------------------------------------------------- |
> | **console(thing)** | the THING that, when activated, will start the camera                  |
> | **camera(thing)**  | the THING that is the camera                                           |
> | **delay(integer)** | the INTEGER that tells the camera how long it stays on the camera view |
> 

The console, surprisingly, is usually a console thing. Just put in the
thing number. Camera is usually a ghost thing. Just add a new thing of
type ghost. The hard bit is getting the pitch, yaw, and roll just right.
These 3 things are what actually align the camera's view. Don't make
delay too long (5 max) or the player will be a trapped there, unable to
move.  
  
That's it\! Pretty easy, huh?  
  
Happy Editing,  
  
Booto
