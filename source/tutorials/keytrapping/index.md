---
title: Player Action
author: Obsidian
email: dragons_bane@hotmail.com
description: >
    The complete tutorial to SetActionCog() and PlayerAction
date: 1999-11-17
original: player_action.html
category: jk
---

Author: Obsidian

This tutorial is meant for the more advanced cogger, interested in
unlocking one of MotS' most powerful features.  (what, you ask, there is
something better then colored lighting?\!)

PlayerAction? huh?  Why's it Gods' gift to MotS editors?  Simple:  it
allows you to use the player's existing buttons instead of having to
make new items to act as additional buttons.  Examples:  (all in MotS)
the cameras, EWeb, STRifle zooming.  Anytime you ask 'how did they do
that with my existing buttons?' the answer is undoubtedly by the use of
the SetActionCog command.  It acts very similar to 'key trapping', where
a programmer is able to intercept a key stroke before it reaches its
destination.

Now that you have been enlightened, you now need to know the full extent
of this command.  The following is the list of all the buttons i know of
that can be trapped.

* Jump Key  
* Crouch Key  
* Activate Key  
* 2nd Fire Key  
* left/Right Strafe Keys  
* Left/Right Turn Keys/Mouse  
* Forward/Backward movement Keys  
* Weapon Switching Keys  
* Up/Down Pitch Keys/Mouse  
* Inventory Menu Selection Keys  
* Force Power Selection Keys  
* Inventory Use Key  
* Force Power Use Key  
* Cycle Camera Key  
* Talk Key  
* Quick Save Key  
* Screen Size Adjustment Keys  
* Gamma Level Keys  
* Score Tally Key  
* Screen Shot Key

Get my jist? SetActionCog is **VERY** powerful (and 1 key is still at
large.  More on it later).

Well, now that you are wetting your pants (I almost did when I
discovered it and its potential) you are wondering 'How the hell do I
use it\!\!'

It is very simple actually (if you know what you are doing).

    SetActionCog(cog, flags);

This is the command used to initiate the key trapping and all its
goodness.  This is the command that tells what COG to send the trapped
key messages to, and which keys to trap.  The COG in the command refers
to the specific cog that it sends the message to.  More often then not,
you will use/find GetSelfCog() in this spot (it gets ID of the very cog
that called GetSelfCog) as it cuts down on the confusion of chasing down
which messages go to what cog.  In the FLAGS spot goes the hex flags of
the keys you wish to trap.  I will post a chart I made (awhile ago, back
in August) at the bottom of the tutorial and include it with the zip
that has all the parameters, IDs, flags, and anything else you can shake
a stick at.  To stop the trapping of keys, one mearly has to call
SetActionCog again and use -1 for the cog and 0 for the flags
(SetActionCog(-1, 0);)

    PlayerAction:

This is the message where SetActionCog sends the information it traps. 
By using its Param's, you can find out everything you need about what
button they pushed, how fast they're moving, what direction they're
moving, what weapon they selected, their head pitch, and the list goes
on.  The chart below tells all of them.

    ReturnEx(1/0);

This is another command used for the PlayerAction message.  Returning 0
means that the action the key performs WILL NOT happen.  example:

    If(GetParam(0) == 0)     // if he presses the jump key  
    {  
       Print("No Jump for You\!");  
       ReturnEx(0);    // Makes the player NOT jump, even though he pressed the jump key.  
       return;  
    }

That will Print "No Jump For you\!" to the console, and the player will
not jump.  However, by replacing the 0 with a 1 in the ReturnEx command,
it will print "No Jump for You\!" and the player will jump.

There are some commands, such as jump and crouch, that send 2 messages
to PlayerAction:.  2 of them are Jump and Crouch.  The first is sent
when they press the jump key (found out by using GetParam(2), it will be
1 if they jump), and second when they land (found out also by
GetParam(2), however it will be 0 if they are landing).  Same deal with
crouch, value of 1 is when they first crouch, value of 0 is when they
get up.

Here is the chart you've heard a bit about above.  There is a unique
case with the misc. keys (gamma, screen size, print screen, ect) where
they will all return a Param(0) of 14.  They are separated by their
Param(2), each has a different value for it.  Enough talk, more chart.  

<div class="tutorial-table" markdown=1>

|              |              |              |              |                  |                     |                                                        |
| ------------ | ------------ | ------------ | ------------ | ---------------- | ------------------- | ------------------------------------------------------ |
| **Param(0)** | **Param(1)** | **Param(2)** | **Param(3)** | **Hex Key Flag** | **Key**             | **Notes**                                              |
| 0            | n/a          | 1/0          | n/a          | 0x1              | Jump                | 1 is takeoff, 0 is landing                             |
| 1            | n/a          | 1/0          | n/a          | 0x2              | Crouch              | 1 is crouch, 0 is getting up                           |
| 2            | n/a          | n/a          | n/a          | 0x3              | Activate            |                                                        |
| 3            | n/a          | n/a          | n/a          | 0x4              | 2nd Fire            |                                                        |
| 4            | n/a          | Speed        | n/a          | 0x10             | L/R Strafe          | \- speed is left, + speed is right                     |
| 5            | n/a          | Direction    | n/a          | 0x20             | L/R Turn            | \-1 is right, +1 is left                               |
| 6            | n/a          | Speed        | n/a          | 0x40             | For/Back (movement) | \- speed is left, + speed is right                     |
| 7            | n/a          | Key Num      | n/a          | 0x80             | Weap Keys           | 13-22 (13=1, 14=2, 15=3, ect)                          |
| 8            | Speed        | Head Pitch   | n/a          | 0x100            | Head Pitch          | \+ is up, - is down                                    |
| 9            | ???          | ???          | n/a          | 0x200?           | ???                 | The key i haven't found yet                            |
| 10           | 1            | Direction    | n/a          | 0x400            | Inv Menu            | \-1 for left, +1 for right (dir). Param 1 is always 1. |
| 11           | 1            | Direction    | n/a          | 0x800            | Force Menu          | See Inv Menu                                           |
| 12           | n/a          | n/a          | n/a          | 0x1000           | Inv Use             |                                                        |
| 13           | n/a          | n/a          | n/a          | 0x2000           | Force Use           |                                                        |
| 14           | n/a          | SB           | SB           | 0x4000           | Misc Keys           | See Below table for params                             |

</div>


##Misc Key Parameters

<div class="tutorial-table" markdown=1>

|              |              |                        |
| ------------ | ------------ | ---------------------- |
| **Param(2)** | **Param(3)** | **Key**                |
| 0            | n/a          | Cycle Camera           |
| 1            | n/a          | Talk                   |
| 2            | n/a          | Quick Save             |
| 3            | \-1/+1       | Screen Size Adjustment |
| 4            | n/a          | Gamma Level            |
| 5            | n/a          | Score Tally            |
| 6            | n/a          | Screen Shot            |

</div>

That's about all there is to it.  The acute minded may realize that this
is the key to  
\*cough\*driveable vehicles\*cough\* \*Obsidian walks away whistling\*  
 
