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
Single-Player JO Maps, Part 2: Force Powers  

-----

Author: [Jepman](mailto:jp_laliberte@hotmail.com)  
  

Alright, I'm going to assume you have a level or something to test your
character's new Force powers. It's not a terrible task to change Force
powers, just follow this tutorial and I will take you on an easy ride
through the wonders of Force power settings.

  - **Tools needed:**  
    GtkRadiant / JK2Radiant — Jedi Outcast map editor
    BehavEd — Jedi Outcast Icarus Script Editor
    Wordpad — Text Editor

I am also expecting that your Radiant editor and BehavEd are correctly
setup. Radiant does most of it for you, but I believe you have to go set
the paths right in the BehavEd Preferences (Prefs button).

First we're going to start by creating the Icarus script that will set
your Force powers. Create a new folder within *jedioutcast/gamedata/*.
This will allow you to load your mod up in-game through the Mods option.
In this folder you have just created, create yet another one, and this
time name it *scripts*. We need to create one more folder. Create it
within the scripts folder, and give it the name as that of your level.
For now we'll name it *project1* Once you've done this, create a new
text file in there. Call it *level\_start.txt*.

Open up
*jedioutcast/gamedata/projectfolder/scripts/project1/level\_start.txt*
in Wordpad, then copy and paste the following code into the text file:

    rem ( "script run at start of level" ); 
    rem ( "set up force powers and weapons" ); 
    
    affect ( "kyle", /*@AFFECT_TYPE*/ FLUSH ) 
    { 
    // Neutral Force 
                    set ( /*@SET_TYPES*/ "SET_FORCE_JUMP_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_PUSH_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_PULL_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_SPEED_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_SEEING_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
    // Light Force 
                    set ( /*@SET_TYPES*/ "SET_FORCE_ABSORB_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_HEAL_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_PROTECT_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_MINDTRICK_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
    // Dark Force 
                    set ( /*@SET_TYPES*/ "SET_FORCE_GRIP_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_DRAIN_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_LIGHTNING_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_FORCE_DARK_RAGE_LEVEL", /*@FORCE_LEVELS*/ "0" ); 
    // Saber Abilities 
                    set ( /*@SET_TYPES*/ "SET_SABER_THROW", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_SABER_DEFENSE", /*@FORCE_LEVELS*/ "0" ); 
                    set ( /*@SET_TYPES*/ "SET_SABER_OFFENSE", /*@FORCE_LEVELS*/ "0" ); 
    } 

If you leave the code as it is right now, your player will start with no
Force powers whatsoever. It's great for Single Player levels where your
player is not a Jedi or any sort of Force user.

For each Force power, you can set the "rank" of power you want your
player to have. So, if you wanted to have your player have a rank of 2
for Force Jump and a rank 3 for Force Push, the code would look like
this:

    set ( /*@SET_TYPES*/ "SET_FORCE_JUMP_LEVEL", /*@FORCE_LEVELS*/ "2" );
    set ( /*@SET_TYPES*/ "SET_FORCE_PUSH_LEVEL", /*@FORCE_LEVELS*/ "3" ); 

There is a maximum rank for each Force power. Without cheat codes in
Jedi Outcast, the maximum level you reach in both Single Player and
Multiplayer alike is 3. I was told with cheating you could go up to 5,
but I haven't experienced this as of yet.

Save your text file and launch BehaveEd, a tool that comes with the
latest release of Raven's Jedi Outcast Editing Tools (along with the MP
source code and such). In BehaveEd, load up your *level\_start.txt*
file. Simply click on the *Compile\!* button down in the lower right
corner of your screen. This will compile your script into
*level\_start.ibi* which is a compiled version that will work in JO.

Now we're going to implant this into your level. Make sure that
*level\_start.ibi* is in
*jedioutcast/gamedata/yourproject/scripts/project1/level\_start.txt*.
Load up your map in GTKRadiant. Once it's loaded, create a new
*info\_player\_start* entity (right-click on the map and select it from
the entity list \[*info \> info\_player\_start*\]) and place it where
you want your player to start. Then, create another entity near the
*info\_player\_start* called *target\_scriptrunner* (*target \>
target\_scriptrunner*).

With the *target\_scriptrunner* entity selected, open the entity
properties window (press the N key). Once that is open, enter the
following commands in the *Key* and *Value* boxes:

    // This will give your entity a name so you can target it 
    Key                         Targetname 
    Value                      run_level_start
    
    // This is the code to run your script
    Key                         Usescript 
    Value                      project1/level_start 

Once you have added these keys and values, deselect the
*target\_scriptrunner* entity and select the info\_player\_start entity.
We're going to target the *target\_scriptrunner* entity. There are two
ways of achieving this. Both are easy and do the same job.

**Method 1:** Open up the entity property windows (when you have the
*info\_player\_start* entity selected) and enter:

    // This code tells the entity to fire the target when you spawn. 
    Key                         Target 
    Value                      run_level_start 

**Method 2:** First select the *info\_player\_start* entity first, and
then add the *target\_scriptrunner* entity to your selection. Then press
Ctrl-K; this targets the second selection (You must select them in
order. If you select the *target\_scriptrunner* entity first then the
*info\_player\_start* entity, it'll be *target\_scriptrunner* targetting
*info\_start\_player*. This won't work. It needs to be the other way
around.).

Now save and compile your level. Create a new PK3 file with the new
script file in under the *scripts/project1/* folder. Make sure this PK3
file is saved under your mod directory. Start up Jedi Outcast in Single
Player mode. Go to *Options*, then to *Mods*. If you have the patched
version of the game, your mod directory name should appear in the mod
list (If you don't, then [download the new JO
patches](http://support.lucasarts.com/patches/patches.htm) and update
your game\!). Click on your mod and click *Load Mod*.

If you have read through [Single-Player JO Maps, Part 1 : General
Stuff](/tutorials/jo_sp_maps_basics_1/) then your level should load when
you press *New Game*. If not you will have to go in the console and
type:

**devmap levelname** (do not type in the file extension (.bsp)

Well this is it for Force Powers. Feel free to contact me if you need
help getting any of this to work, or post a topic at the Massassi Forums
in the [Jedi Outcast Editing
Forum](http://forums.massassi.net/cgi-bin/forumdisplay.cgi?action=topics&forum=3.+Jedi+Outcast+Editing+Forum&number=17&DaysPrune=2&LastLogin=).
