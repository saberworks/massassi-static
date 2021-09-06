---
title: 
author: 
email: 
description: >

date: 
original: index.shtml
category: 
---

Author:[![Printable Version](/images/printable.gif)](tutorial_print.shtml)
Simple Elevator  

-----

Author: [JM](mailto:deyjaL@aol.com)  
  

This tutorial will show you how to use my generic elevator script. It is
not a scripting tutorial in itself, it is a script implementation
tutorial\! It should be noted that lifts can be created using entities,
but scripting gives you much more control. THIS script won't give you
much more control, but it's a good start\!

  - **Tools needed:**  
    GTKRadiant 1.2.8 or above
    Jedi Outcast
    My script - [JMGeneric/elevator01](jmelev.zip)

Now, how to use the script...

Create the following entities:

  - Your elevator, a func\_static. Must have an origin brush, I suggest
    making the origin brush 16\*16\*16.
  - Two ref\_tags. These are the up and down positions, similar to
    frames in JED. The elevator's origin brush will center itself on
    these positions.
  - Two func\_usables for each switch that controls this elevator. One
    textured with a switch off texture. The other given the spawnflag
    'start off', and textured with a switch on texture. They should be
    in exactly the same position.
  - A trigger\_multiple with a wait value of at least 2 and the
    spawnflag 'use button'.
  - A target\_scriptrunner with a count value of -1

Give your elevator entity a unique script\_targetname value.  
Give your buttons a unique targetname value. BOTH FUNC\_USABLES SHOULD
HAVE THE SAME TARGETNAME\!  
Give each ref\_tags unique targetnames.  
Select your trigger, then select your target\_scriptrunner, then press
ctrl+k  
Deselect all, and select your elevator.  
Insert the key 'PARM2' with the targetname of the up ref\_tag as it's
value.  
Insert the key 'PARM3' with the targetname of the down ref\_tag as it's
value.  
Insert the key 'PARM4' with the targetname of the button as it's
value.  
Insert the key 'PARM6' with a float value in milliseconds. This is how
long it will stay at the top. The trigger\_multiple should have a wait
value equal to this divided by 1000, plus 2. That is, (PARM6/1000)+2.  
Deselect all.  
Select your target\_scriptrunner.  
Insert the key 'usescript' with the value 'JMGeneric/elevator01'. Do not
include the extension, or scripts/  
Insert the key 'PARM1' with the script\_targetname of the elevator as
it's value.  
Insert the key 'PARM4' with the targetname of the button as it's
value.  

Your elevator will move to the top when the player presses the use
button while inside the trigger. Place the trigger right in front of the
button\! To create more buttons, just duplicate the func\_usables and
the trigger. All buttons switch states when the elevator moves.

**DO NOT** use spacebar to duplicate elevators\! This will clear the
spawnflags for BOTH elevators\! You have to build each one, and each
button for each one, from scratch.

**DO** use unique names for everything\! I suggest a naming scheme
similiar to the one in the demo map. It uses 'elev\_01\_up',
'elev\_01\_button', etc. This script has slightly more overhead then a
script made specifically for your elevator, but the difference is
negligible. This script is based off of the kejim\_post/tower script
which controls the small elevator that takes you up to the switch that
turns the gun on.

Cheers,  
JM
