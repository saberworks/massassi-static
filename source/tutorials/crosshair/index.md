---
title: Custom Crosshair
author: Rjmig88
email: Rjmig88@aol.com
description: >
    This tutorial teaches you how to make the proper modifications to add your own customized crosshair image..
date: 2000-07-23
category: jk
---

Author: Rjmig88

## Before you begin:  
[Download the necessary files for this tutorial.](crosshair.zip)

## Introduction:  
Well, you clicked on this link because you wanted to learn how to do
create some cool crosshairs like I have. Well, here is your chance to
learn how to do them... (sorry, I am not good at introductions...)

Instead of me just giving you the cog, we will actually open it up and
see what each part does. First we will do the cog, then the templates,
then finally get rid of the Jedi Knight default crosshair without
editing the .exe file:

## Tutorial:  
Open up the **crosshair.cog** now. Done looking? Time to explain what
each statement does.

The symbols section is the templates (you can add on more for more
crosshairs), 2 ints (the switch is just a "storage" space to see what
crosshair you currently got on the toggle, so don't change this\!, the
zoomed int is a supportive feature for different zoom functions, don't
change this\! It's just another storage place, the int dummy is another
storage space, and the temp vector is a vector storage place.

**Startup:**

```
# This will get the player on your own computer and save it as a thing number.  
*player = GetLocalPlayerThing()*;

# This will set the pulse, in the pulse, it will fire a crosshair template if 
# you are not dead, making the new crosshair appear.  
*SetPulse(0.001)*;

# this just returns the information to the server and closes the cog message.  
# not having it will skip to the next message.
*return*;
```

**Pulse:**

```
# this just checks to see if you are still living, you wouldn't want the 
# crosshair to be active when you are dead\!  
if(GetThingHealth(player) >= 1)
{  
    # These check to see if the crosshair and a regular view is on
    if(zoomed == 0) // REGULAR ZOOM  
    {
    if(switch == 0) // CROSSHAIR 1  
    {  
    # this checks to see if you are in person view.
    if(GetCurrentCamera() == 0)  
    {  
    Dummy = FireProjectile(player, crosshair0, -1, -1, '0 0 0.035', '0 0 0', 0, 0, 0, 0);
    # this creates the crosshair template
    Temp_Vector = VectorAdd(GetThingPos(Dummy), VectorScale(VectorNorm(GetThingLVec(Dummy)), 0.2));

    # this will calculate where the original Jedi Knight crosshair was so it
    # can then be adjusted so its accurate 
    SetThingPos(Dummy, Temp_Vector);

    # This will set the crosshair template to the above calculations
    }  
    # this is saying if its a outside view instead
    else  
    {  
    Dummy = FireProjectile(player, crosshair0, -1, -1, '0 0 0.087', '0 0 0', 0, 0, 0, 0);

    # same stuff as above, replace template to a ghost type template if you
    # dont want external crosshairs
    Temp_Vector = VectorAdd(GetThingPos(Dummy),
    VectorScale(VectorNorm(GetThingLVec(Dummy)), 0.2));  
    SetThingPos(Dummy, Temp_Vector);  
}  
```

Seeing a pattern in the crosshair cog now? Just add on or change as
necessary for more crosshairs. Scroll down in your copy of the cog till
you come to zoom 1, you may change the vectors and stuff for a different
zoom and send a trigger to this cog telling to zoom in, so the crosshair
will be there. Think of it as a "master" cog for crosshairs.

**killed:**

```
# makes sure that this player died  
if(player != GetSenderRef()) Return;

# this will turn off the crosshairs  
SetPulse(0);
return;  
```

**newplayer:**

```
# Turn crosshairs back on (custom, not JK's by the way)  
SetPulse(0.001);
return;  
```
  
**activated:**

```
# These lines are just supporting lines for the crosshair toggle feature.
# It will save the int switch as that value used in the pulse so it will
# be a different crosshair.  
if(switch == 0)  
{  
switch = 1;  
Print("MaDeVentor's Crosshair-2");  
}  
else if(switch == 1)  
{  
switch = 2;  
Print("MaDeVentor's Crosshair-3");  
}
```
  
**trigger:**

Just add your receiving triggers here for zoom features and have the int
zoom resigned here...  
  
Whew\! that was a LONG code, eh? Still with me? Good. Now time to see
the templates for the crosshairs and the files\! =)  
  
Open up static.jkl, you will see those templates, basically, the
template is just a small template for a sprite. A sprite is a custom mat
texture that is a 2d picture really. Open up a sprite now\! Its a file
with a .spr extension. You will see its just a storage base for a
crosshair .mat file, and has size and stuff you can mess around with.  
  
Now, the moment that you have been waiting for, disabling Jedi Knight's
crosshair\!

Open up the file **jkstrings.uni**

Now you are wondering why there is 898 messages instead of 900? Well, we
need to first block the JK crosshair messages in here...  
Locate the 2 crosshair strings.  
They are  

```
"GUI_CROSSHAIR" 0 "Enable aiming crosshair"  
"GUI_CROSSHAIR_HINT" 0 "Show the targeting crosshair?"  
```

So, how do we block them, well, we put a \# in front of them. Just like
this:

```
#"GUI_CROSSHAIR" 0 "Enable aiming crosshair"  
#"GUI_CROSSHAIR_HINT" 0 "Show the targeting crosshair?"  
```

There, oh wait, we are not done yet\! Open up that **renameme.plr**
file, ohhh, I bet we never edited these before... Well, I will walk you
through...

See that part where its crosshair 0? That's the flag for the crosshair,
1= JK crosshair on, 0= JK crosshair off. Make sure its 0. Now this file
will be a little tricky to install since it can't go into a .gob. In
your readme.txt for your mod, you will need to tell the player how to
install this file. Tell them to make a new character, then paste this
into the new folder JK created in their player folder, then have them
delete their old .plr file, and rename it to their player. This way it
will stop all but the most determined people to turn on JK's crosshair.

Oh wait, we need to put on the crosshair toggle. I already did it in the
**jkstrings.uni**, and in the items dat.

By The Way, if you want to hotkey it, but not use these files, a suggest
use for items.dat is this:  

```
crosshair  116  1  1  0x120 cog=crosshair.cog  
```
  
Please give me credit for learning how to do crosshairs, it would be
nice, but if you use any of these files, then you must give me credit,
please\! Thank you.
