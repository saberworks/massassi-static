---
title: Traps
author: Rishka
email: mkoger@i-55.com
description: >
    Learn the interworkings of a template trap cog. If you are interested in
    learning COG, this is a tutorial you must read.
date: 1998-03-30
original: tmptraps.htm
category: jk
---

Author: Rishka

Well, this is my first tutorial, so you'll have to bear with me. =)
Today, we're going to cover how to create and implement traps in Jedi
Knight. As an example, we'll create a trap which can fire any template,
is activated by a switch, and only fires when you enter a specified
sector. The first thing we'll do is take a look at the cog.  
  
OK, open up Notepad or your word processor of choice and start a new
document entitled "multi\_trap.cog". The following indented code needs
to be added to the document.  

```
    # ========================================================================================
    # Jedi Knight Cog Script
    #
    # multi_trap.cog
    #
    # Multiplayer trap(s) that can be deactivated by switch.
    #
    #
    # [Rishka]
    #
    # (C) 1998 The Massassi Temple. All Rights Reserved     
    # ========================================================================================
```

This is merely the header. Everything following the '\#' is ignored by
Jedi Knight. You can use this to describe the cog, name the author, and
tell who has the "rights" for the cog.  
  
```
    symbols  
```
  
This is the start of the symbols section.This is needed at the start of
the object and variable declarations.  
  
```
    message activated  
    message entered  
```
  
This defines two functions - "Activated" is called whenever the player
activates an item or switch. "Entered" is called whenever a player
enters a sector defined in the cog.  
  
```
    surface switch                  desc=switch
    sector  shootSector linkid=1        desc=shootSector
```

Here we have two variables. The first is the switch that will activate
the trap. The second is the sector that, when a player enters it, will
start the trap shooting. The linkid in the second line is used to
further determine which sector was entered. (Useful when you have more
than one sector to be used in a trap)

```
    template    projectile=+raildet
```

This is the projectile to be used for the trap. Because there isn't a
local keyword following the line, this variable is customizable in JED.

```
    thing       ghost1                  nolink,desc=ghost1
    thing       ghost2                  nolink,desc=ghost2
    thing       ghost3                  nolink,desc=ghost3
    thing       ghost4                  nolink,desc=ghost4
```

This defines four things, which will be the launch points for our trap.
They are customizable using JED.

```
    int     rounds=5
```

The number of rounds fired when the trap sector is entered.

```
    float       rate=0.33
    float       autoAimXFOV=90
    float       autoAimZFOV=180
```

The rate of fire between the four turrets and the two field of views
(FOV) used. The X FOV is the left-to-right area that the turrets use,
and the Z FOV is the up-down area for the shooters to use.

```
    int     firing=0                local
    int     cur_round=0             local
    int     activated=0             local
```

Three more variables. These variables are "local", i.e. they are defined
later on in the cog, and not customizable in JED. The first variable
determines whether the turrets are firing or not. The second determines
the current round. The last one is used to determine whether or not the
switch has been activated.

```
    sound       fireSound=turret-1.wav  local
    sound       on_snd=set_hi2.wav      local
    sound       off_snd=lgclick1.wav        local
```

The three sounds used for the trap.

```
    end
```

You use "end" after all symbols (objects, variables) are defined. This
tells Jedi Knight that the symbol definition is done.

```
    # ========================================================================================
    
    code
```

This tells Jedi Knight that the code section is starting...

```
    activate:
```

The "activated" function - only runs if the player activates a switch or
item.

```
    if (activated == 0)
```

If the switch has not been activated... (activated = 0)

```
    {
    SetWallCel(switch, 1);
```

This line changes the surfaces texture. Certain .mats have more than one
texture (for example, switches) Here, we change the .mat to it's second
texture. (0 is the first)

```
    activated = 1;
```

We set activated to 1, signifying that the switch has been activated.

```
    PlaySoundPos(on_snd, SurfaceCenter(switch), 1.0, 5.0, 10.0, 0);
```

Here, we play the "on" sound... The different variables are as follows:

<div class="tutorial-table no-headers" markdown=1>

|                            |  |
|----------------------------|----------------------------|
| on_snd                     | is the sound to be played.  |
| SurfaceCenter(switch)      | is a command that determines the exact center of a surface (switch)  |
| the third parameter (1.0)  | - the volume of the sound to be heard.  
| the fourth parameter (5.0) | - the minimum distance for the sound to be heard.  |
| the fifth parameter (10.0) | - the maximum distance for the sound to be heard  |
| the sixth parameter (0)    | - flags (not sure what different flags can be used here) |

</div>

```
    }
    else
```

If the switch HAS already been activated....

```
    activated = 0;
```

and set the "activated" variable back to 0 (i.e. the switch is off)

```
    dummy = PlaySoundPos(off_snd, SurfaceCenter(switch), 1.0, 5.0, 10.0, 0);
```

We also play the "off" sound, using the PlaySoundPos command

```
    }
    Return;
```

This signifies the end of the "activated" function....

```
    entered:
```

The "entered" function - runs if the player enters a sector defined in
the cog

```
    if (GetSenderID() == 1)
```

This line determines whether the sector entered is the same as the
sector with the linked 1.

```
    {
    if(firing == 1) Return;
```

If the "firing" variable equals 1, end the function...

```
    if(activated != 1) Return;
```

Also, if the switch hasn't been activated, end the function.

```
    firing = 1;
```

Set the "firing" variable to 1.

```
    cur_round = 0;
```

Set the current round to 0;

```
    while(cur_round < rounds)
```

While the current round is less than the maximum number of rounds...

```
    {
    FireProjectile(ghost1, projectile, fireSound, -1, '0 0 0', '0 0 0', 1.0, 0x60, autoAimXFOV, autoAimZFOV);
```

OK, this is the actual command used to fire the projectile... We'll
spend a little time on this one here.  
The syntax for the FireProjectile command is as follows:

**FireProjectile(thing turret, template projectile, sound fireSound, int
mode, vector fireOffset, vector aimingError, flex unknown, int flags,
flex XFOV, flex ZFOV)**  
  
The first variable is pretty much self-explanatory - it is the thing
that shoots the projectile. The second variable is the template for the
projectile to be shot.The third variable is the sound to play while the
projectile is being fired. The fourth variable is the mode (key) to play
while shooting, useful if a player is doing the shooting, but not for a
trap. The fifth parameter is the fire offset vector... this is used to
change where the projectile comes from. A fire offset vector of '0 0 1'
would fire the projectile 1 JKU (Jedi Knight Unit) higher than if you
used a fire offset vector of '0 0 0'. The sixth parameter is the aiming
error vector... if it's not equal to '0 0 0', the projectile will be off
target. The higher the numbers, the further off it will be. The seventh
parameter is unknown right now, so we won't discuss that one. =P The
eight parameter is the flags used by the FireProjectile command. I'm not
sure what all flags can be used for this command, so stick with "0x60"
unless you want to experiment. The last two parameters are the X-Axis
FOV and Z-Axis FOV. They determine the left-right and up-down range of
the turret.

```
    Sleep(rate);
```

This command causes JK to sleep for rate seconds... no commands are run
by this cog.

``` 
    FireProjectile(ghost2, projectile, fireSound, -1, '0 0 0', '0 0 0', 1.0, 0x60, autoAimXFOV, autoAimZFOV);
    Sleep(rate);
    FireProjectile(ghost3, projectile, fireSound, -1, '0 0 0', '0 0 0', 1.0, 0x60, autoAimXFOV, autoAimZFOV);
    Sleep(rate);
    FireProjectile(ghost4, projectile, fireSound, -1, '0 0 0', '0 0 0', 1.0, 0x60, autoAimXFOV, autoAimZFOV);
    Sleep(rate);
```

These are all the same as the first one; they just fire from different
turrets.

```
    cur_round = cur_round + 1;
```

Increment the current round by one, and continue until you reach the
maximum number of rounds. (rounds)

```
    }
    firing = 0;
```

Set the "firing" variable to 0.

```
    }
    
    Return;
```

This is the end of the "entered" funtion...

```
    end
```

This signifies the end of the code section, which is also the end of the
cog... That's all there is to it.. see that wasn't so hard. =uP  
  
Now, time to tackle how to implement it in JED. OK, so crank up JED now,
and start a new level (or open up an old one if you'd like). If you
haven't done so already, put the new trap cog into the project directory
of the level.  
  
Now, in JED, create a sector to put your trap in. On one of the walls
put a switch (see the switches tutorial for more information on adding
switches) to use for your trap. Now create four new things in your
sector, using the template "ghost", and place them where you want your
trap to shoot from. Make sure they are facing the right direction. (you
can change the directions by editing the *pitch, yaw, roll* variables in
the Item Editor in JED) OK, now write down (or remember) the sector
number used in the trap, the switch's surface number, and the four thing
numbers for the turrets.  
  
If you don't have your level saved in .JED format yet, you'll need to
save it now. Open up the Placed Cogs window, and add a new cog. On the
left pane, select Project Directory. In the right pane, select the new
trap cog. Click OK. Now, using the numbers you wrote down, fill in the
variables for the cog. The names of the variables are
self-explanatory...  
  
<div class="tutorial-table no-headers" markdown=1>

|             |                                                                                                                                                                                                                                                    |
| ------------| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| switch      | The surface number of the switch which you wrote down earlier                                                                                                                                                                                      |
| sector      | Enter the sector number you wrote down earlier                                                                                                                                                                                                     |
| projectile  | The template to use for the projectile to be fired. You have a wide selection of choices here, not just limited to weapon projectiles. Be creative and use rocks, shrapnel, and explosions... \*Note: not all projectiles can be used in this cog. |
| ghost*n*    | The four thing numbers for the turrets.                                                                                                                                                                                                            |
| rounds      | The number of rounds to use for the trap.                                                                                                                                                                                                          |
| rate        | The time delay between the fire from the traps. (in seconds)                                                                                                                                                                                       |
| autoAimXFOV | The left-to-right range for the turret to use. (0 to 360)                                                                                                                                                                                          |
| autoAimZFOV | The up-down range for the turret to use (0 to 180)                                                                                                                                                                                                 |

</div>
  
  
OK, that's all there is to it... really\! =uP  
Now, gob it and run it to see the results... fires too slowly? change
the rate of fire. Too narrow a field of fire? Increase the FOVs. Don't
like the projectile fired? Change that too\! Well, it's late now, so I
better end it... hope this has helps some of you beginning coggers in
your quest to understand traps.  
  
Happy Editing,  
\-Rishka

Reference: [tmptrap.cog](tmptrap.cog)
