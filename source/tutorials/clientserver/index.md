---
title: Cleaving
author: Obsidian
email: dragons_bane@hotmail.com
description: >
    Learn how to make client/server cogs, special types of cogs that produce a minimum of lag in multiplayer.
date: 1999-12-12
original: clientserver.html
category: jk
---

By Obsidian
 

This tutorial is most definitely not meant for the beginning coggers. 
It deals with some advanced stuff, meant to keep the lag down during
Multiplayer games.  You should know how to use triggers well, as c/s
cogs depend on them heavily.

Why client/server cogs you ask?  The reason is very simple:  JK/MotS is
laggy enough as it is, there is no need to add any more lag then
necessary because a door or a window was not 'optimized' for MP games. 
A good way to think of it is to think of an actual network (at school,
work, or even a LAN in your home).  I'll use a school network as an
example.  Lets say you sit at a computer in the library and feel like
surfing the net, so you double click on the Netscape icon.  Now, 1 of 2
things could happen.  Lets say all the files and programs are on the
file server (i.e. all the cogs are run off of the host's computer) and
the computer your at needs to access and run Netscape from the server. 
Every action you make in Netscape (whether you are even connected to the
internet or not) is sent over the network and back.  It doesn't take a
guineas to figure out that that will create an awful lot of lag on the
network.  Same is true with cogs.  If you have to access a cog that is
on the host computer only, each time it is used it will create an
abundance of lag.  Now, lets say that school installs Netscape onto the
computer you are sitting at.  You fire up Netscape, and it pops up
almost immediately due to the fact that your computer didn't have to
receive it over the network from the server, and you go chugging along
browsing your pages.  The server sends you the minimal amount of
information needed to view the page and its contents, and Netscape
deciphers it locally and displays it.  This is very true with c/s cogs. 
You walk up to a c/s door and try to open it.  It fires off a trigger
telling the server that this door is going to open, and if the server
ok's it, it will fire off another trigger telling ALL the clients to
open that door locally.

There are inherent dangers when using c/s cogs though.  One of the
predominant issues is syncing the thing/s (in our case a door).  For
example, little Joey is playing on a JK game that little Billy is
hosting.  Billy opens a c/s door, and the network packet heading to
Joey, that contains the trigger telling his door to open, gets dropped. 
Now, we end up with Billy having an open door and Joey having a closed
door.  Because Billy's door doesn't give a rip what Joey's door is
doing, Billy is able to walk through his open door.  Meanwhile, it
appears to Joey that Billy just walked through a door (or it may appear
that Billy is place walking into the door, which would cause horrendous
syncing problems with the players as well as the doors), and is unable
to follow because his door is closed.  Or, Billy turns around and starts
to shoot Joey.  To Billy, the projectiles hit Joey.  To Joey the
projectiles hit his door, which isn't open, and does no damage.  This
could lead into rampit accusations of cheating, and possibly a boot or
two.   You could, however, use a system of triggers to keep all the
doors synced on all machines, but that would use a lot of triggers, and
defeat the purpose of using c/s cogs all together, and that would just
be silly.

"But Obsidian, What good are c/s cogs then if they can mess up like
that?\!"

The answer is simple young grasshopper.. You need to use some
innovation, a little luck, and a lot of skill.  Think of a way that is
bandwidth effective, yet still has a low chance of messing up under
normal to moderately heavy usage.  For example, don't code an idiot
proof door that will resist messing up if constantly used over and over
and over on multiple clients.  It will take a lot of time, bandwidth,
and the results will not be worth the extra bandwidth expended to keep
it idiot proof.  The best, though, would be idiot proof AND bandwidth
effective.

Another danger with c/s programs/cogs/whatever is the ease in which they
can be hacked.  Diablo and Interstate '76 come to mind.  Whenever
information is used on the client side only (i.e. the server keeps its
paws off of it until the client sends it) there is a tremendous
possibility of hacking.  That is also why massively multiplayer games,
such as Utlima Online and EverQuest, give the server absolute rule over
everything.  Character information, item information, and world
information are all saved on the server to prevent client side hacking
of characters and items.  However, as seen with UO Extreme, even this
method is not hacker proof.  Hacking is not a concern you will need to
deal with when writing a c/s cog, because the information we're going to
handle on the client side isn't even worth trying to hack.

Below are the simple cogs i made to demonstrate Client/Server coding.

If you are bright enough, you will see that my cogs actually create
about 2x as much lag as necessary.  The client cog (when activated) will
send a trigger to the server cog.  Upon the receiving of the trigger,
the server cog will broadcast another trigger to all the clients telling
them to move the thing to the other frame.  I very well could have made
the client cog broadcast the trigger that moves the thing to the other
frame, which would reduce the lag it makes by about 1/2, but this way
gives you a spot to sort of 'moderate' what is going on.  You could
cancel the thing moving, check to see if a certain player activated his
thing, check to see if the player who activated the thing had a key (or
other item required) to move the thing, all kinds of stuff which would
otherwise be a pain in the ass to do within the door cog itself,  and
that may very well require you to send more then one trigger.. which
would defeat the whole short cut idea and be an awful lot more messy.

As an example, lets say you restructure an entire door cog to c/s to cut
out the middle server cog.  Then your level editor comes to you and says
"on second thought, I want to use this door cog insted".  If you hadn't
done the entire c/s operation in the door cog, all you would need to do
is slap some triggers into the new door cog and shuffle the code around
a bit to activate the door by triggers.. as opposed to having to either
a) restructure the new door cog so it will be a stand-alone c/s cog, or
b) shoot the level editor and use the door cog you spent hours
restructuring.

Again, I feel It would be of more benefit to display the cogs I did and
give detailed comments, as opposed to walking you through a step-by-step
process which can get awfully confusing and tedious (too bad level
tutorial authors don't have this luxury ;) )  
(note: included cogs (in zip) are not commented)

First the server cog (which is close to nothing because I didn't need to
do anything besides redirect the client trigger)  My comments are
(obviously) after the comment slashes (//) .

```
# Jedi Knight Cog Script  
# server_mthing.cog  
#  
# Server cog for the Cleint/Server tutorial.  
#  
# -Obsidian 12-3-99

symbols

message trigger

end

# ..........

code

Trigger:

If(GetSourceRef() == 98) SendTrigger(-1, 99, 0, 0, 0, 0);  // If this is the trigger sent by a client cog, send another trigger to all client                                                                                                      
                                                                cogs telling them to move their thing to the other frame.  
return;

end
```

Now the client cog, which is a bit heftier then the one-command-wonder
server cog.

```
# Jedi Knight Cog Script  
# client_mthing.cog  
#  
# Moves a thing from frame 0 to 1 and vice versa when activated. Created for the C/S Tutorial.  
#  
# -Obsidian 12-3-99

flags=0x240    // Thee most important line in this entire cog.  It tells the cog to run locally on each clients machine, and to not sync  
                    itself with the other client cogs. (0x200 local, 0x40 no sync)  
symbols

int  player  local  // Probably the only redundant line in this cog, because player is never used.  A habit i guess.
                            If you did need to use the player variable, you can assign it to GetLocalPlayerThing()
                            (even though this is a MP cog) because the flags above set this cog to local.  Print() also works
                            like it should (i.e. doesn't display on the host's side, like non local cogs do if Print is used.)

thing  MoveThing  mask=0x405 // The thing we're moving.  The mask allows it to call the activated: message when activated.
flex  Speed=5  nolink  // How fast were moving the thing

int  frame   local

message startup  
message activated  
message trigger  
 

end

# ==========

code

Startup:

player = GetLocalPlayerThing();  // Redundant, but shows that GetLocalPlayerThing can be used instead of GetSourceRef or  
                                        GetSenderRef

return;

# ..........

Activated:

If(IsThingMoving(movething)) return;  // ALWAYS do checks that you can do locally first before sending the first trigger.  If the thing  
                                            can't even be moved for some reason, you don't want to be firing off triggers and have it  
                                            find out it won't be able to move until the very end.  This is a good way to reduce lag.

SendTrigger(-1, 98, 0, 0, 0, 0);  // If the thing isn't moving, then send the first trigger to the server cog, which it will relay to the other  
                                            client cogs.  
return;

# ..........

Trigger:

If(GetSourceRef() == 99) Call MThing;  // If this is the trigger from our server cog (giving the OK to move the thing) call the message  
                                            that will send the thing on its way.  
return;

# ..........

MThing:    // The message that will move the thing after all the triggers have been swapped and everything is given the OK

frame = GetCurFrame(movething);  // Find out which frame the thing is at so it gets sent to the other frame.

if(frame == 0) MoveToFrame(movething, 1, speed);  
If(frame == 1) MoveToFrame(movething, 0, speed);

return;

end  
```

Now, to maybe clear up a little confusion, the above cogs will move the
SAME object on all players' machines, making it appear as if it is done
globally, only with a fraction of the lag.  I think i heard somewhere
that a trigger is only a few bytes in size, and when considering only 2
triggers (1 if you didn't activate the thing) were sent to/from you,
with a grand total of a few bytes of information being sent over the
network. Client/server cogs are a work from the heavens.. if done
properly.  Glass would also benefit greatly from a c/s makeover.  
The only thing i really see that cannot be effectively converted to c/s
are elevators, and more generally anything that is designed to move
players.  These types of c/s cogs can create nasty player syncing
problems, because the player won't be in the same spot on all machines,
and that spells disaster.   So there are some cogs that need to stay
global for syncing reasons.. But barring those, the sky's the limit
=).
