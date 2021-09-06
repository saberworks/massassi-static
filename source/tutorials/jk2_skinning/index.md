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
Custom Skinning  

-----

Author: [Michael Chang Gummelt](mailto:mgummelt@ravensoft.com)  
  

**Staff Note:** *The following is a copy of the Jedi Knight II Skinning
Tutorial available with the official distribution of RavenSoft's JK2
Editing Tools.*

Here's what you do (this is a bit longwinded, but it's not really that
complicated, I'm just being very thorough)...

1.  First thing you may want to do is extract the original model and
    skins from our assets0.pk3 file. You will find this file in the
    "base" directory (look where you installed the game - there should
    be a "base" dir in the GameData directory). Open that file with
    WinZip (WinZip can open it) and go down the list until you find all
    the files in the directory for the model you want to modify. All
    models are in models/players (sort by "path"). So, for example,
    Lando is in models/players/lando. Select all the files in that
    directory and extract them into your "base" directory. When you
    extract make sure that you have the "use folder names" option
    checked. You should now have a "models" directory inside the "base"
    dir, a "players" dir in the the "models" dir, and inside "players"
    you should see the dir of the model you extracted (in this example,
    "lando").

2.  In that folder, you will find a text file called
    model\_default.skin. This is the file that tells the game what image
    files to apply to each part (surface - collection of polys) of the
    model. Copy this and rename it to use your new skin name (using the
    example "solo", for instance: model\_default\_solo.skin). Note that
    the "default" MUST be in the skin file's name or the game will not
    recognize it as a selectable skin.

3.  Now open up the .jpg and .tga files in that directory and modify
    whichever ones you want to, then save them out \*under a different
    name\*. When you do, find the name of the image file you modified in
    the new .skin file you copied and replace the name of the original
    image file with the name of the new one you just saved. (When we
    release the model viewer, you'll be able to preview your work).

4.  Now you have a .skin file that points to the new image files. All
    you have to do now is make your "icon" image. This is the small,
    square picture that shows up in the menu when you're browsing what
    skin to use (also shows up in-game on the HUD in certain
    circumstances). You will need to make a new one for your new skin.
    Open up the original for reference, make your new one and save it
    back out with a new name, following the name renaming guidelines as
    the .skin file... so the original icon is called icon\_default.jpg,
    save your new one as icon\_default\_solo.jpg (again, using "solo" as
    the example).

5.  Now you're done\! It will work in the game on your computer (try it
    out), now you just need to put it together for other people to see.
    You need to zip it up into a .pk3 file like the others in the "base"
    dir. Now, since you want to make sure the .zip file remembers the
    path to each file (remember how when you extracted files into the
    "base" dir, it created all the right subdirectories?), you have to
    add the files to the .zip file from a dir higher then "models" and
    you must add using "wildcards" (don't worry, I'm about to explain
    and walk you through it). The best way I've found to do this is to
    make a new directory in "GameData" called "mods" (or whatever you
    want to call it). This acts as a substitute "base" dir for our
    current purpose of zipping up your work. Copy the "models" folder
    into this new folder (if you have more than one skin you've done, be
    sure the copied "players" dir only has the model you just modified).
    Now, go back up to your "mods"(or whatever you named it) dir and
    create a new .zip file. Open it up and hit the "Add" button to add
    files. Browse to the "mods" directory you just made and make sure
    that "include subfolders" is checked. Then click on "Add With
    Wildcards". This will add all the files you just made and include
    the folder/directory path to them (you should be able to verify this
    when you're done adding and look at the file list in the .zip file).
    Make sure the .zip file only contains the new files you made (not,
    for example, the original image files), this way you keep your
    filesize down and don't accidentally overwrite other people's files.
    Now save and exit WinZip, and rename the file to whatever you want
    and change the extension from "zip" to "pk3".

You're done\! Upload the file somewhere and share the goodness\!

-----

Okay, now I know some of you are still going to have questions (after my
initial post that contained the above instructions, I got a lot of
follow-up questions). Here is a bit of Q\&A about this process:

**HELP\! JK2 crashes when I try to view my skin\!**

> There are 2 problems I have seen people have:
> 
> 1.  Over-aggressive jpg compression. When you save your texture as a
>     jpg, use standard compression.
> 2.  Pk3 file has a long path in it. Make sure your pk3 file doesn't
>     have some extremely long file path in it - like "C:\\Program
>     Files\\Lucas Arts\\Star Wars JK II Jedi
>     Outcast\\GameData\\base\\models\\lando". This is the wrong way to
>     zip up your pk3 file and exceeds Jedi Knight 2's 64-character
>     limit on path name length. When zipped up, the files in your pk3
>     should have a path that starts under the "base" directory (in this
>     example: instead of that long path, it should just read
>     "models\\lando" if you zipped it up right. Make sure when you zip
>     up your pk3 you have "Include subfolders" checked, not "Save full
>     path info".

**I see we have ModView now, how can we view the model with the skin we
made?**

> Extract the \_humanoid.gla and animation.cfg following the same
> instructions as above (extract into the GameData/base folder and the
> files should appear in the directory:
> GameData/base/models/players/\_humanoid - remember to have "use folder
> names" checked when you extract).
> 
> Extract the models.shader file using the above instructions (extract
> into GameData/base. the file should appear in the dir:
> GameData/base/shaders).
> 
> Extract any models/players directories you want to view/modify (see
> above instructions). At this point, your directory structure should
> look something like this: GameData/base/models/players/\_humanoid -
> this should have the \_humanoid.gla and animation.cfg in it
> 
> GameData/base/shaders - this should have the models.shader in it
> 
> GameData/Base/models/players/lando (using the running example of this
> tutorial) - this should have the model.glm, model\_default.skin and
> all the .jpgs and .tgas in that directory in it. Open ModView. Go to
> open a file and browse to the .glm file in the
> GameData/base/models/players directory of the model you want to view.
> 
> Voila\! If you get some warnings about missing textures when you load
> the model, you may want to make note of them and go back into the pk3
> file, find them, and extract them as well. Most of the time, it will
> be complaining about not finding the "caps" textures… you do not need
> these in order to view the model, so don't worry about them.
> 
> In the window on the left side, you'll see an expandable list that
> says "model.glm" expand that (click on the "+") and you'll see another
> expandable list called "Skins available". Expand that and you'll see
> all the .skin files in that model's directory. Double-click on them to
> view them. If you touch up your skin and want to see the changes in
> ModView hit ALT+R (or look in the "File" menu).
> 
> Also note that the editor does not draw every stage of multi-stage
> shaders nor does it mask out parts of textures with alpha channels.

**How do I make the red and blue team-play skins for my skin (so the
skin can be used in team multiplayer games like Team FFA, CTF and
CTY)?**

> Using the "solo" skin example at the top of this document:
> 
> Copy the model\_default\_solo.skin you made and make 2 new .skin
> files: model\_red\_solo.skin and model\_blue\_solo.skin.
> 
> Then just make red and blue versions of the textures you want to tint,
> save them with whatever filename you like.
> 
> Then, edit the 2 new .skin files you made to point at those files
> (note: you don't have to replace every texture in the .skin, just the
> ones you want to tint blue or red).
> 
> Then make a red and blue version of your icon\_default\_solo.jpg,
> naming them (again, in this case) icon\_red\_solo.jpg and
> icon\_blue\_solo.jpg.
> 
> That's it\! Now your new skin should be able to be used in team games.

**Okay, I start up multiplayer, choose to play my skin I made, but I
when I join a server, my skin is reset to some other skin. Why?**

> It depends on two things. If the server is "pure". "Pure" is a server
> setting that, when set, does not allow any players to use any files
> that the server does not have (this is to prevent cheating and
> maintain compatibility). If "pure" is not set on the server, you can
> use any files you want, regardless of whether the server also has
> those files.
> 
> If the server is pure, the only way you can use your new skin is if
> the server also has the pk3 file with your skin in it. If you bring
> down the console (press SHIFT+\~) and type "fs\_referencedList", you
> will see all the pk3 files the server is using, including but not
> confined to the assets0.pk3 and assets1.pk3 that came with the retail
> game.
> 
> All that having been said, 99% of the servers running are going to be
> pure. If you find one that is not pure, you can use whatever files you
> want, but it may be less stable. So the best way to get your file to
> be usable in game is to have server admins get your pk3 and put it in
> their base folder for everyone to see and use (more on this in the
> next question).
> 
> More useful console commands:
> 
> path - once you join a server, this will show you all the pk3 files
> you've got in your base dir and whether or not they're on the server's
> "pure" list. If they are, you can use what's in them.
> 
> sv\_pakNames - the names of all the pk3 files you have.
> 
> sv\_paks - the CRC's of all the pk3 files you have. The last 2 should
> be the retail JK2 pk3 files. The game uses the CRC of the file to
> determine if they're the same, not the name. So if the server has a
> darthmaul.pk3 and you have one, you still cannot use yours if the CRCs
> are different (meaning that they're actually different versions of the
> darth maul skin, they just happen to have been named the same thing).
> PK3 names should be unique\!

**Okay, I start up multiplayer, choose to play my skin I made, but
no-one else can see it. Why?**

> Well, only people who actually have the skin you just made can see it.
> Also, if they have "force models" on, they will see every model and
> skin as the model and skin they are using. If they have "defer models"
> on, they only get updated models when they die or when the scoreboard
> comes up.
> 
> Now, they can get your model by either of two means:
> 
> By downloading it from a site like
> [www.jediknighii.net](www.jediknighii.net),
> [www.massassi.net](www.massassi.net) or
> [www.jediknight2files.com](www.jediknight2files.com) and putting it in
> their base dir...
> 
> OR
> 
> They can download your pk3 directly from the server when they join it.
> This will happen automatically if the server has "Allow Downloads" on
> (look at the "g\_allowDownloads" item on the server info for the
> server) and if the player joining the server has "Allow Downloads"
> enabled.

**How difficult will it be to make our own custom meshes and apply them
to your animations?**

> If you have 3D Studio MAX, we will be releasing a plug-in/exporter for
> MAX and our Ghoul2 compiler that should allow you to make custom .glm
> meshes (or modify ours) and apply them to our animation skeleton (the
> \_humanoid.gla file).

**How difficult will it be to make our own custom animations?**

> To make new animations, you'd need a copy of SoftImage... we don't
> expect that many people have access to that...

-----

*Well, that's it (for now), if you have any more skinning questions,
stop by the mod forums are [JediKnightII.net](www.jediknighii.net)
and/or [Massassi.net](www.massassi.net) or, if you're totally stumped,
e-mail me your question at <mgummelt@ravensoft.com>.*

**Michael Chang Gummelt**  
Game Programmer  
Jedi Knight II: Jedi Outcast  
Raven Software
