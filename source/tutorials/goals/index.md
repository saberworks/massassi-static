---
title: 
author: 
email: 
description: >

date: 
original: goals.html
category: 
---

Author:Objectives Tutorial  
What they are, how they work and how to use them  
By [Antony Espindola](mailto:Ant@Horrible.Demon.co.uk)

-----

There are currently other tutorials around for Objectives (which are
also called "Goals") at the moment, but they seem to introduce too many
concepts in the COG language at once and this can be a bit confusing for
the novice programmers amongst us, therefore I have done this tutorial
to explain more about how Objectives are defined in JK/MotS, how they
work and give you a few tips on creating your own.

*I'm pretty new to this - how do I add Objectives to my level?*

First off, let's talk about what exactly Objectives are. When you play a
Single-Player JK/MotS level, you will (normally) have a few Objectives
that you must complete to end the level - be it picking up a certain
object, killing a "Dark Jedi" or similar character, entering a certain
area or even simply spotting a certain item in a room. The Objectives
are designed to give you a *purpose* to the level, rather than just
going round and killing all the enemies and finding keys to open doors
(otherwise we'd all be playing Quake, right? ;-)

This doesn't mean that you can't end the level without completing all
the Objectives- you will need to either setup you level so that you can
only enter the end sector (say by keeping a door locked until a certain
Objective is completed), or you will need to check that all the
Objectives have been completed in your end-level COG.

So when we create our levels, the first thing we need to do is let our
level know that we actually **have** Objectives in it\! This is done
through the COGSTRINGS.UNI file which holds things like lines of text,
the name of your level and the introduction text you see as the level
loads, but then you should be familiar with this file by now\!

The Objectives are entered into the COGSTRINGS.UNI file in the following
format:

The first number (in quotes) defines the Objective's number and level it
it used in. It always starts "GOAL\_" and then has a 5-digit number. You
multiply the number of your level by one thousand and then add the
number of the Objective in that level, but don't forget that the
Objectives start at Zero and not One\! For example, Objective 4 of Level
6 would be specified as:

The next number (always a zero) is not used. The next line of text is
what appears in the "Objectives" screen in the game. This text shouldn't
be too long- the loading screen's text should explain the overall
purpose of the level. Keep the text short, but not too vague otherwise
the player might get stuck. Something like *"Get some Ammo"* is rather
dull and doesn't really help whereas *"Find an alternative route into
the Ammunition Room"* would be a much better way of saying the same
thing.

*Great\! I've typed in the Objectives but nothing appears\! What am I
doing wrong?*

Now you have defined your Objectives, you need to add them into the
game. This is done through COGs which can be kept very simple or made
incredibly complicated - it all depends on your ability which can easily
grow if you experiment, learn and practise. There are no easy routes to
learning how to write COGs, but with a little programming knowledge
(like how an "IF...ELSE..." statement works) and by looking at other
people's COGs (I recommend you look through the ones by LucasArts that
come with the game as these are well commented so you can tell what they
are doing) and the use of the [JK
Specs](http://www.jedinights.com/massassi/specs/jkspecs.htm) to find out
what they do, you should have no trouble understanding it.

Now we have defined our Objective in the COGSTRINGS.UNI file, we need to
make them appear in our game - this requires a command inside a COG. To
show the Objectives, we use the SetGoalFlags() command:

The first line simple gets the "handle" for the Player and assigns it to
the *player* variable (but then you knew that\!) The second line makes
the Objective appear in the list.

Let's take a look at the SetGoalFlags() command in more detail to show
how it works as this is the important bit when working with Objectives.

The first parameter, *player*, is the handle for the current player. We
got that in the line above. The second parameter (zero in this case) is
the number of the goal that we want to show; our zero equates to the
first Objective we defined. The second number (1 in this case) is the
flag value:

By **not** setting the Goal flags, the Objective will not appear in our
Objectives list. If you want to have all your goals appear at the start,
add a SetGoalFlags line for each of your Objectives and set the flag for
each of them to 1.

Another way to work with Objectives is to "hide" some of them until
other Objectives are completed. This helps to keep some of the plot a
mystery and won't give away any secrets or twists in your Level's story
until the Player needs to know about them. To do this, simply don't add
the required lines in your Startup COG, but do them elsewhere...

To make an Objective appear when we complete another Objective, we
simply have to put the line which "shows" our Objective into the same
COG as that which "completes" the previous Objective. I'll show you how
to do this in a moment, but first let's see how you code to "complete"
and Objective:

Looks familiar? That's because we just set the Goal flag to 2 to make it
"completed"\! This shows you just how easy it can be to program COGs
yourself\!

*Ok, I understand how to define, show and complete an Objective, but how
do I work this into my level's COGs?*

You simply need to add a COG that will be triggered when the player does
something that would complete an Objective. For example, if one of our
Objectives was to *"Gain access to the Security Tower"* then we would
set up a COG that triggers when the player enters that sector. Showing
you how you write a COG to trigger like this is beyond the scope of
*this* tutorial and I'm sure it's been written far better elsewhere\! So
let's say we have a COG that triggers when we enter a sector, and we can
just edit it and add our "Objective Completed" lines to it:

So you can see how easy it is to complete and show your Objectives.
There are also conditions that can be triggered in a COG for things like
when an item or surface is damaged, an object is sighted or when you
walk into a certain sector - more information is available in other
tutorials but I wanted to keep this one simple and explain about
Objectives and not how to write COGs\!

The tricky part to Objectives is thinking of inventive ways to use them-
not just picking up items or opening doors, but by solving puzzles in
the level or checking for certain conditions. As you get better and
better with your COGs, you will be able to create more interesting and
complicated ones which will help to make your level stand out.

*Good luck\!*
