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
Changing MotS Player Actions  

-----

Author: [MastaJedi](mailto:hill@golden.net), [Jedi Knight Role Playing
Group](http://www.jedilegacy.net/SWRPG/)  
  

In *Mysteries of the Sith*, any COG can analyze, define, disable, enable
or otherwise manipulate the messages that are sent by the user, from
peripherals like the keyboard and mouse, to the game. For example, a cog
that is set up this way can determine when the player is moving, firing,
when an item is used, when the camera mode is switched - even when the
autosave function is used, and disable these messages or modify their
outcome. This ability must be activated like so:

> 
> 
>     SetActionCog(GetSelfCog(), 0x7fffffff);

and also present in this cog must be the message:

> 
> 
>     message playeraction

All player actions are now passed to this message as a combination of
parameters. Using the verb:

> 
> 
>     GetParam(flex);

in the playeraction message will return values which can be interpreted
into all the possible actions the user can make from his/her control
devices. Basic modification of the outcomes of these actions take place
as a ReturnEx() statement, where ReturnEx(0.0) disables actions from
being interpreted by the game, and ReturnEx(1.0) permits actions to be
passed through to the game. To disable parameter passing to the
playeraction message, one must run the following:

> 
> 
>     SetActionCog(GetSelfCog(), 0);

(GetSelfCog() can also be substituted with the integer (-1) to
equivalent effect.)

In the following examples, understand that parameter(0) having a value
of 0.0 is the parameter that is passed when the Jump key is
pressed/activated. In all cases, assume that

> 
> 
>     SetActionCog(GetSelfCog(),0x7fffffff)

has been executed, enabling parameters passing to the playeraction
message.

<span class="underline"></span>

**Example 1**

> 
> 
>     ...
>     Playeraction:
>     Return;
>     ...

**Resolution:** All actions will pass through unaffected.

<span class="underline"></span>

**Example 2**

> 
> 
>     ...
>     Playeraction:
>     if(GetParam(0) == 0.0)
>      ReturnEx(0.0);
>     else
>      ReturnEx(1.0);
>     Return;
>     ...

**Resolution:** The if statement checks see if what the user just did
was to press the jump key - because all actions are passed through this
cog, this statement checks all actions that are executed. If the action
that was executed IS jump, then the ReturnEx(0.0) statement DISALLOWS
the jump action to be passed on to the game; the player will not jump.
The else condition carrying the ReturnEx(1.0) statement ensures that any
OTHER action that is executed is passed through to the game unhindered.

If the ReturnEx() statements were reversed - that is to say the first
(in the if condition) was (1.0) and the and the second (in the else
condition) was (0.0), then only the Jump action would be expressed and
all other actions would be BLOCKED. Essentially the only thing the user
could make the player do was jump and that's all.

So, we see that using if statements, we can selectively block and let
pass any action sent by the user to the game. If we take this a step
further, we can block the outcome of an action and re-define it so some
other outcome is observed. The following are examples of this:

<span class="underline"></span>

Example 3

> 
> 
>     ...
>     Playeraction:
>     
>      if(GetParam(0) == 0.0)
>      { ;
>       Print("The Jump key was pressed, but it makes us crouch!");
>       SetParam(0, 1.0);
>      }
>      ReturnEx(1.0);
>      Return;
>     ...

**Resolution:** Any time the jump key is pressed, the if statement kicks
in and prints "The Jump key was pressed, but it makes us crouch\!", then
SetParam(0, 1.0) changes the jump action to a crouch action - so the
player will crouch instead of jumping when the jump key is pressed.

<span class="underline">**Example 4**</span>

> 
> 
>     ...
>     Playeraction:
>      ReturnEx(0.0);
>      print("You can't do anything till I say so!");
>      Return;
>     ...

**Resolution:** All actions are blocked - the user can't make the player
do anything, and to add insult to injury, "You can't do anything till I
say so\!" will be printed any time an action is attempted. :-)

The following is a list of all known actions and their parameters that
can be passed to the game from the user. Keep in mind that many if not
all actions have more than one parameter to describe the action.

Playeraction Parameter List with Definitions

> 
> 
>     Action   Param(0) (1)    (2)
>     
>     Jump    0.0 ---    1.0 in air
>             0.0 when landed
>     
>     Crouch    1.0 ---    2.0 in crouch
>             0.0 when standing
>     
>     Use/Nudge   2.0 ---    1.0 always
>     
>     Fire (Primary/Second)  3.0 ---    0.0 = primary fire
>             1.0 = secondary fire
>     
>     Strafe (left/right)   4.0 ---    VALUE = VELOCITY (instant.) (unknown units)
>             + value = right
>             - value = left
>             value = 0.0 when stopped
>             maximum = 2.0  (defined in walkplayer template?)
>     
>     Turn (left/right)   5.0 ---    VALUE = RATE (instant.) (deg/s ?)
>             + value = left
>             - value = right
>             value = 0.0 when stopped
>             keyboard maximum = about |180.37| deg/s
>             mouse maximum = thousands :-)
>     
>     Forward/Backward  6.0 ---    VALUE = VELOCITY (instant.) (unknown units)
>             + value = fwd 
>             - value = bwd 
>             maximum = 4.0 (defined in walkplayer template?) 
>             minimum = -2.0  
>             value is halved when "slow" is enabled 
>     
>     Select Weapon   7.0 0.0    13.0 = lightsaber / fist 
>             14.0 = bryar pistol / DL-44 
>             15.0 = st rifle / scope rifle 
>             16.0 = detonator / flash bomb 
>             17.0 = bowcaster / (para bowcaster) 
>             18.0 = repeater / (para repeater) 
>             19.0 = rail gun / seeker rail 
>             20.0 = sequencer / manual seq. 
>             21.0 = concussion rifle / (para concussion) 
>             22.0 = carbon gun / (para carbon) 
>     
>         1.0     1.0 = select next weapon
>             -1.0 = select previous weapon
>     
>     Pitch    8.0 VALUE = RATE (deg/s ?)  VALUE = DEGREE
>         +value = up    +value = up
>         -value = down    -value = down
>         (mouse value is multiple  0.0 = straight ahead of 40)
>     
>     ??    9.0
>     
>     Select Inventory -bracket  10.0 1.0 = default / "on"  1.0 = store next inventory bin for activation
>             -1.0 = store previous bin for activation 
>     
>     Select Skill -bracket  11.0 1.0 = default / "on"  1.0 = store next skill bin for activation 
>             -1.0 = store previous skill bin for activation  
>     
>     Use Selected Inventory  12.0 1.0 = item key pressed  VALUE = BIN OF SELECTED or HOTKEY INVENTORY 
>     Use Inventory (hotkey)  2.0 = item key subsequently held 
>         0.0 = item key released 
>     
>     Use Selected Skill   13.0 1.0 = skill key pressed  VALUE = BIN OF SELECTED or HOTKEY SKILL 
>     Use Skill (hotkey)   2.0 = skill key subsequently held 
>         0.0 = skill key released 
>     
>     Misc Activation   14.0 0.0    0.0 = cycle camera 
>             1.0 = ??? 
>             2.0 = quicksave 
>         (+/- 1.0 = big/small) --->  3.0 = screensize 
>             4.0 = next brightness level 
>             5.0 = ??? 
>             6.0 = take screenshot

On a final note, understand that only one playeraction message can be
run at a time by ANY cog. Any new instances of the
`SetActionCog(-1, 0x7fffffff)` verb will direct user actions to the new
cog instance, while remaining instances are disabled or ignored.

Happy Cogging\!
