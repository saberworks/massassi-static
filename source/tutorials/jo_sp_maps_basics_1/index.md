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
Single-Player JO Maps, Part 1 : General Stuff  

-----

Author: [Jepman](mailto:jp_laliberte@hotmail.com)  
  

The tutorials below were too small to stand individually so they were
grouped into one tutorial that covers the following basics.

1.  Running your map in Single-Player with New Game
2.  Spawning your Single-Player hero with only a Bryar and Stun Baton
3.  Changing the Single-Player hero's model

<!-- end list -->

  - **Tools needed:**  
    GtkRadiant / JK2Radiant — Jedi Outcast map editor
    Wordpad — Text Editor

-----

Running your map in Single-Player with New Game

*Thanks to AKPiggott for showing this*

First you're going to create a project folder within the
*jedioucast/gamedata/* directory. Once that is done, go into your
project folder and create a new text file. Name it *gamestart.cfg* and
then open it up in Wordpad. All you need to type in there is the
following

``` 
// This will tell JO to load your map. 

map        nameofyourmap       
```

Now you need to go in extract ui/*newgame.menu* from *assets1.pk3* to
your project folder and open it up in Wordpad. Go down and find the
following line:

    uiScript        startgame

Delete it and replace it with this line:

    exec        "exec gamestart.cfg" 

Now create a new .pk3 file with this modified file in under the "ui"
folder. Make sure this .pk3 file is saved under your mod directory.

Now start up Jedi Outcast in Single Player mode. Go to *Options*, then
to *Mods*. If you have the patched version of the game, your mod
directory name should appear in the mod list (If you don't, then
[download the new JO
patches](http://support.lucasarts.com/patches/patches.htm) and update
your game\!). Click on your mod and click *Load Mod*.

-----

Spawning your Single-Player hero with only a Bryar and Stun Baton

It doesn't get much easier than this, but some people might not notice
just how easy it is and search for a way to do this through scripts and
such.

Simply load up your Radiant editor and create a *player\_start\_info*
entity where you want your player to start. Then select it and open up
the Entity Properties window (Press the **N** key).

Now go down to the *Key* and *Value* boxes and enter the following:

``` 
// This will give your entity a name so you can target it
Key                spawnflags 
Value             32   
```

Alternatively, you can simply check the *Stun\_Baton* box, which spawns
the player with a Stun Baton and a Bryar Pistol by default. Not too
difficult, huh?

-----

Changing the Single-Player hero's model

Unfortunately, right now there is no real professional way of changing
the Single-Player model from Kyle to something else, so this is more of
a workaround.

First you're going to create a project folder within
*jedioucast/gamedata/*. Take whichever model you want to use, then copy
its files into your project folder under:

*projectfolder/models/players/modelname/*

If the model has a shader file that comes with (eg., the custom Wookie
model has a shader that will render his hair textures transparent so
they look right) Simply take that shader file and put it in your project
folder under:

*projectfolder/shaders/*

Now rename your *modelname/* folder to *kyle/* and load up the .skin
files that come with the model (*model\_default.skin*) and change the
path for each of the textures that lead to the model's folder name.

> **For example:**  
> If you have the line :  
>   
> *head,models/players/**han\_anh**/face.tga*  
>   
> change it to:  
> *head,models/players/**kyle**/face.tga*  

**Do not** change lines that point to caps.tga textures (they are in the
stormtroopers folder)  
*eg. r\_arm\_cap\_r\_hand\_off,models/players/stormtrooper/caps.tga*

Now create a new .pk3 file with these modified files in their respective
folders (*models/players/kyle/ , shaders/*). Make sure this .pk3 file is
saved under your mod directory.

Now start up Jedi Outcast in Single Player mode. Go to *Options*, then
to *Mods*. If you have the patched version of the game, your mod
directory name should appear in the mod list (If you don't, then
[download the new JO
patches](http://support.lucasarts.com/patches/patches.htm) and update
your game\!). Click on your mod and click *Load Mod*.

-----

Well this is pretty much it for these tutorials. Remember, you don't
need to pack each different modification into separate .pk3 files. You
can simply pack it all into one .pk3 file. Just make sure each file is
stored in its respective folder.

Feel free to contact me if you need help getting any of this to work, or
post a topic at the Massassi Forums in the [Jedi Outcast Editing
Forum](http://forums.massassi.net/cgi-bin/forumdisplay.cgi?action=topics&forum=3.+Jedi+Outcast+Editing+Forum&number=17&DaysPrune=2&LastLogin=).
