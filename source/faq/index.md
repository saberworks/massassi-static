---
title: Jedi Knight Editing Frequently Asked Questions (FAQ)
---

[TOC]

# General Questions

## How do I make levels for Jedi Knight?
The Code Alliance, created a program called JED for making Jedi Knight and MotS 
levels.  The Code Alliance web site is now defunct.  JED source code was 
released and has been taken up by JKHub and has been renamed Zed.  You can 
download it from the [JKHub Tools](http://www.jkhub.net/library/tools.php) web 
site.  JED/Zed is freeware, and very powerful. This is the editor that most 
levels are made in. The other editor is/was JkEdit by Ole Thomasen (web site 
now defunct). It was shareware, with a limit on how many sectors you could 
create before having to pay. For tutorials on JED (which also work for Zed), go 
the [tutorials section](/tutorials.php).  This FAQ covers only JED/Zed.  If JED 
is mentioned it's 99% likely the issue/solution will apply to Zed as well.

## What is a project directory?
When you save your JED files, you should always use a "project
directory." Basically, a project directory is a directory you use to
save all files related to a specific level. For instance, I have JED
installed in "C:\\Jed\\" - Under that, I have a directory called
"Projects." In my "Projects" directory, I have a folder for each of
my levels-in-progress. Why have a project directory? Well, when you
gob your level, JED includes all the files in the directory your
.jed file is saved in (including subdirectories) - so, if you just
save your jed files in the root of your C drive, JED will
automatically include all contents of your C drive. You'd then get a
huge gob file that would most likely crash your computer. From this
point on, we'll assume that you do have a project directory.

## What is a GOB file?
A gob file is simply a non-compressed container file. It can contain
all different types of files that Jedi Knight uses, such as .cog,
.jkl, .3do, .par, .spr, .ai, etc. For more info on these file types,
visit the [Unofficial Jedi Knight Specs](https://www.massassi.net/jkspecs/).

## What goes into the GOB file? Why is it so big?
JED copies every Jedi Knight file type from your project directory
into the GOB file. This means that if you have a .txt file or a .doc
file in your project directory, it won't be in the GOB. Same with
the .jed file -- it is first compiled to a .jkl file, then that is
added to the GOB. The actual .jed file is NOT in the GOB. Also, new
sound (.wav) files are often very big, so if you have a great amount
of custom sounds, your GOB will be much bigger. Custom textures also
make your file be much larger.

## I want to release a level, are there rules?
Maybe.  See the [LEC Addon License Agreement](license.html).

## I'm going to release my level, how should I do it?
First, download Winzip
([http://www.winzip.com](http://www.winzip.com/)) or a similar
program. Include the GOB of your level, along with a readme file
(found in the JED directory) with all the proper info filled out.
Authors sometimes include other text files with sepecial
instructions or background info. You MUST insert the readme from the
JED directory or most sites won't post your level - you'll be in
violation of the LEC License Agreement.

## I'm going to release my level, who do I send it to?
There are a few sites that will post your level. Unfortunately, the
number is slowly dwindling. This site will generally
post any levels/mods provided you follow the submission instructions.

## Can I extract things from MotS levels and insert them into Jedi Knight levels?
No. This violates the license agreement, and if any site finds out
you have done this, they will take down your level. This goes for
cogs, 3DOs, levels, textures, and anything else in MotS.

## Can I extract things from Jedi Knight levels and put them in MotS levels?
Since people MUST own JK in order to own MotS, it is a general
concensus that putting JK components into MotS levels is acceptable.

## Can I take custom components from other people's addon levels and use them in my level?
Only if the author gives specific permission in the readme file, or
is contacted and says yes. Please don't take stuff without
permission. Most authors will give permission with no problem. You
can also download custom components that authors have released to
the public from the Resources section of this site (check the sidebar).

# General Level Questions

## Why do players who try to join games of my multiplayer levels get "Players 1 of 1" when they try to join the game?
You must have more than one walkplayer in the level. Be sure to put
in plenty in interesting locations to make your level interesting
and fun.

## How come I get a "Could not load level" error?
These errors can be caused by numerous things. First, make sure you
saved correctly. First save your JED file in a project directory,
then go to Tools/Episode Editor and fill in all the information you
can. Make sure to enter a level and episode name. After that, be
sure to hit the "UPDATE" button. If you do NOT hit update, the
information won't be saved (Do not choose "save" - it's for
something different). After that, save your JKL and GOB - if not
saving correctly was your problem, this should fix it.  
    
Another way to find errors that can cause this problem is to use
JED's Consistency Checker. Go to Tools/Consistency Checker. If ANY
errors pop up, they need to be fixed. If you are getting very odd,
unexplainable errors like chairs being created randomly, go to
Tools/Options/Misc. tab and make sure that that 'Check overlapping
sectors' option is checked. Then re-check the level for errors.

## How come my level freezes up when I shoot or enter a certain area?
First, do you have any custom 3DOs in that area? Or visible from
that area? Most of the time, custom 3DOs that have errors will cause
this problem. If you DO have a custom 3DO, try deleting it, then
save and re-load the level. If this fixed your problem, you will
have to either find out what's wrong with your 3DO, or re-make it.  
    
Also, if you have a custom 3DO in the area, and deleting it solves
the problem, check the 3DO's template. If it has no parent template,
you will be kicked out as well. Make sure all your new 3DO templates
have parent templates.  
    
Solid color mats that aren't flagged correctly can also cause this
problem. If you have a solid color mat, on a forcefield or
otherwise, make sure that the GEO-mode is set to 3. If it is set to
4, as normal mats are, you will be kicked out of the level. Solid
color mats can also cause problems on 3DOs. If you created a 3DO
with a solid color mat on it, go back and check the geo-modes of
each surface, then re-export it.

## Why does the player seem to ice skate in the floor?
This is because the surface you are walking on is not flagged as
"floor" - In JED, just click on the surface, press \[Enter\], and
when the Item Editor pops up, click on the surface flags area, and
check the "floor" box. If you have a lot of surfaces that have this
problem, go to [the plugin page](/jedplugs/)
and get the Vinkel plugin. This plugin
will search the level for surfaces that are less than 45 degrees and
flag them as floor, leaving the other flags (metal, dirt, etc.) as
they are. Very useful tool, highly recommended.

## I still need help!
Please visit the [basics](/basics/) sections and then the 
[tutorials](/tutorials.php) section.  If you still need help, try the 
[forums](https://forums.massassi.net/).

# Things

## What is a "Thing?"
A thing is a 3do that can be added via the thing mode. All enemies,
weapons, powerups, ships, doors, elevators, and related items are
things.
      
## How do I insert a new thing?
When you create a new level, it will be a box with one light, and
one thing. The thing is called the "walkplayer" - you must have this
in every level, so please just leave it alone. To insert a new
thing, go to thing mode (the walkplayer will be automatically
selected), hover your mouse above the area you want to add the new
thing, and press the <kbd>Insert</kbd> key. This will add a new walkplayer.
Now that you have two, just change the one you just added into the
thing you want. While it is selected, press <kbd>Enter</kbd> to invoke the
item editor, then double click where it says "walkplayer" - this
will bring up a menu of all the things you can add.
      
## I've inserted my thing, but when I play my level, it is floating or halfway into the floor.
This is because you didn't check the side views after you placed it.
Once you place it from any view, you must check it from the other
views to ensure that it is correct. Just use the \[shift+number
keys\] to switch to the different views.
      
## How do I make my thing face a different direction?
This is accomplished by selecting it, pressing \[Enter\] to invoke
the item editor, then changing the pch, yaw, and rol values.
      
## I can't make my thing line up exactly with the floor.
This is because your grid snap is not set low enough. Lower it to
.05 or even .01 and you should be able to get it to line up
correctly. Some 3do's won't line up unless you go even lower than
that (for example, console1).
      
## My thing disappears and reappears, what's up with that?
3DOs that cross sectors will often disappear. Just move it so it is
contained in one sector, and it should be fine. Make sure parts of
it aren't extruding out into space, either.

# Textures

## How come my textures show up with pink/green/blue/etc colors all over them?
This is because of your colormap settings. A colormap is a palette
of 256 colors. Since different levels use a different set of colors,
there are different colormaps for different texture sets. An
outdoor, rocky area uses different colors than an indoor, imperial
gray colored area. Unfortunately, it is difficult to mix these types
of areas and still have a wide variety of textures. Anyway, go to
Tools/Level Header Editor and choose a colormap that corrosponds
with the texture set you would like to use. For example, if you want
your level to have the same colors as Level 1 of Jedi Knight, pick
the 01narsh.cmp colormap. Then, choose textures with an 01 before
them (01stud.mat).

## I've set the Master Colormap, but some of my textures still have  pink in them.
While each level has to have a master colormap, each sector can
still be set with a different one. This is designed to be used with
complementing colormaps, such as the 01 suite. If you set the master
colormap, 3D-accelerated graphics cards will display the level
correctly, but then when non-3D accelerated cards are used, the pink
shows up. This is because the individual sector colormaps are set
differently than the Master CMP. Just multi-select all of your
sectors, press enter, then choose the correct colormap in the
selection area.

## How do I line up my textures?
Texture Stitching is a feature in JED that every author should
become familiar with in his/her beginning stages of editing. To
texture a room, simple double click on a wall (in 3D preview) and
choose a texture. After that, click on the texture once again
(single-click), press the semi-colon key <kbd>;</kbd> to copy the texture,
then click on another wall, and press the apostrophe key <kbd>'</kbd> to
paste it. This should copy your texture as well as line it up.

## Stitching copies my texture, but won't line it up properly.
This happens every once in a while, and so far no fix has been
found. Try stitching to an adjacent wall, then stitching from that
one to the "problem area" - oftentimes this will work correctly, and
they will line up. Be creative and try to find other walls to stitch
off of.  
    
This happens when you have a surface with some odd amounts of
vertices, often caused by merging sectors of surfaces. If you want
to get rid of these annoying vertices, get Vertex Assassin from the
[plugins page](/jedplugs/).

## How do I make a custom texture?
Get an image editor, create a bmp, then use the program called
MatMaster (you get get it from the [programs](/programs/) section) to
convert it to a mat file.

## My custom texture looks fine in my image editor, but when it gets converted, the colors are all messed up.
When you create a custom texture, you need to make it for a certain
colormap. Choose the colormap you are creating the texture for, and
extract it to a folder using JKGob or Conman (both available from the 
[programs](/programs/) section). Also extract
any .mat file that is in that colormap. Use MatMaster to convert
that texture to a BMP file, and load the bmp file into Paint Shop
Pro (there are other image editors, but this is the only way I know
to get the palettes correctly). Go to the Colors menu, and choose
"save palette" - then, open your custom bmp file, go to colors, and
choose "load palette" - choose the palette you just saved. This will
convert your bmp to that colormap. Some of your colors will be
changed, but you have to work inside the boundries of the colormap
you are using. If you are not happy with the color choices, try a
different CMP.

## I have a .mat file from one colormap, but I want to use it with another colormap.
To do this, you will have to use matmaster to map it to a different
colormap. Warning: this can mess up your colors, and you will have
to fix them yourself. Extract the CMP file you want to convert it
TO. Then, in MatMaster, click the Map to Colormap button, and choose
the colormap you just extracted, then convert it.

## How do I rotate/scroll my textures to different angles/directions?
This is done using keyboard commands in the 3D preview. Click on a
surface, and press the comma <kbd>,</kbd> and period <kbd>.</kbd> keys. This 
will scroll your texture. To scroll the other way, hold down <kbd>Shift</kbd>
and press the same keys. You can use <kbd>Shift + arrow keys</kbd> as well.
To rotate it, hold down <kbd>Ctrl</kbd> and use the same keys. After you
have rotated/scrolled one texture, you can stitch it to other
surfaces, and it should line up. See

## How do I get certain parts of my textures to be clear (see-through)?
Assuming you want something like the grate textures, where you can
see through bars, etc, to a different area, do the following: First,
learn how to correctly implement an LEC see-through texture. You
must put it on an adjoin. This means: there has to be a sector on
the other side to look INTO. If you don't have a sector on the other
side, you will get HOM (Hall of Mirrors) - which is bad. So, take
two sectors, adjoin them, select the adjoin, then press enter.
Change the GEO-mode to 4, draw textured. Now, a texture should show
up on one side of the adjoin. You will still be able to walk through
it, however, so set the adjoin flags to "impassable." Now, press
<kbd>Shift+F</kbd> to select the other side of the adjoin. Follow the same
steps to make the texture visible and to make that side impassable.
Now, texture both sides with an LEC see-through mat.  
    
Once you have that working properly, it's time to create your own
mat. Use a SOLID BLACK color anywhere in your mat, and it should
show up as clear in-game.

## I want black in my custom mat, but for some reason it always shows up as clear.
This is because most JK/MotS CMP's use black as their transparent
color. If you want a black color in your .mat, just use a color
that's off-black, like a really really dark gray (it looks just like
black).

## How do I make my texture translucent (like the water surface in Canyon Oasis)?
As with the transparent (grate) type surfaces, this has to be
applied to an adjoin. This will work with any texture. Set the
GEO-mode to 4, and then apply the texture you want to the surface.
Click on it, press enter, and double click in the "face flags" area.
Choose translucent. That's it, you're done.
      
## How do I animate a texture?
For the default LEC textures, JED will tell you whether they are
multi-celled mats. You must use a multi-celled mat. Add the texture,
then use the matanim.cog from the placed cogs (<kbd>F7</kbd>) menu. Enter the
required mat names and you are done.

# Level Architecture

## What's the easiest way to create an adjoin?
Adjoins are accomplished by placing two surfaces directly on
eachother, then cleaving each so they match up. You then select the
part that overlaps, and press the <kbd>a<kbd> key. Newer versions of JED
also have a "join" function. Just place two surfaces so they
overlap, multi-select both surfaces, and press the <kbd>j<kbd> key. This
will join the overlapping areas. What are the disadvantages of this?
You don't have control over where the surface cleaves go, and
sometimes the lighting/texturing can end up looking a bit funny.

## I placed a small square sector inside a large square sector, but when I play, the small sector won't show up.
The Jedi Knight/Sith engine does not let you place a sector inside
of a sector. You are probably a beginner at this stuff, so please
visit the [basics](/basics/).  After that, read the cleaving tutorial in
the tutorials section. If you still need help, ask a question on
on the forums.

## How do I make a ramp/stairs/beams/etc?
Please take a look at the [tutorials](/tutorials.php).

## How do I make an elevator/door/slashable grate/breaking glass/force field/etc?
Please take a look at the [tutorials](/tutorials.php).

## How do I make a beam fall/piece of architecture move?
In Jedi Knight/Sith, architecture cannot move. You must create a 3DO
and make that move.

## What is a 3DO and how do I make one?
3DOs are 3D objects in Jedi Knight/Sith such as the characters,
elevators, doors, enemies, ships, etc. Anything that moves in Jedi
Knight is probably a 3DO (with the exception of sprites, which are
3D animations, and a few other things). To make one, please follow
one of the [tutorials](/tutorials.php).

## I just downloaded/created a custom 3DO, how do I insert it into my level?
All 3DOs must have an entry made into a template file (master.tpl
for JK, mots.tpl for MotS) before the game will recognize them.
Please see the [Templates Tutorial](/tutorials/templates/).

## How do I rotate my 3DO to face different directions?
Mess with the Pch, Yaw, and Roll values in the item editor.

## Why does my 3DO disappear sometimes?
3DOs that cross sectors will disappear. Just move it so it is
contained in one sector, and it should be fine. Make sure parts of
it aren't extruding out into space, either.  This means that elevators, doors, 
etc. should stay in the same sector as they move.

## Why does my 3DO show up as a small yellow box?
This is because of an error in your 3DO. If you have solid color
mats, make sure the GEO-mode of that surface is set to 3. If that
doesn't work, try re-making your 3DO from scratch.

## How do I make a new enemy?
Enemies are 3DOs that have pup and key files for their animation.
At the time of this writing there was no good 3DO animator so it was not 
feasible to create an entirely new enemy.  (This may no longer be true, I don't 
know.) You can, however, re-texture existing enemies, and modify certain parts 
of them. This is called skinning.

## How do I re-skin a 3DO?
There are a few skinning tutorials in the [tutorials section](/tutorials.php).  [Here's one.](/tutorials/skins/)

## How do I make a new weapon?
Check the [tutorials section](/tutorials.php).

## What is cog?
Cog is a scripting language used in the Jedi Knight/Sith engines. It
is similar to C in basic structure. All dynamic aspects of Jedi
Knight/Sith are controlled by cogs.

## I want to learn cog.
Read the JK Specs.  Read the tutorials.  Read the Editing Forums.  Extract, read, and modify the existing cogs from the game.  Good luck!

## I don't think I can learn cog, is there some place that will make my cogs for me?
Not like that. If you join an editing group, or make friends with
some coggers, they will often help you out. Otherwise, you are
forced to ask for a cog on message boards, but those posts normally
go un-answered. Best thing to do is make friends with a cogger, or
learn simple cogging techniques.

## How do I make water?
Select a sector, press <kbd>Enter</kbd> if you do not have the Item Editor
on-top, and change the sector flags to "underwater."

## How do I make the surfaces show up as water?
Select the adjoin above your water, change the GEO-mode to 4, and
give it a water texture. If you want to make it see-through, check
the texture section of this FAQ.

## I have my water, but now I want it to flow.
This is done through sector thrust. Please read the [sector thrust/vector 
tutorial](/tutorials/thrust/tutor.htm).

## Now that my water is flowing, how do I make the surfaces scroll to match?
This is done with a surface scrolling cog. You will have to enter
the vector (direction) the surface will scroll in, the speed, and
the surface number.

## I want my room to be colored red/blue/whatever color.
This is done by setting the sector tint to a certain color. Just
select the sector you want colored, and press <kbd>Enter</kbd>. Go to the
tint area, and choose a color.

## I've tinted my sector, but you can't see the color unless you are in it.
That is correct. If you want to be able to see the sector tint from
outside the sector, you must trick it out. This is done by selecting
the adjoin you want colored, setting it's GEO-mode to 3, and
applying a colored mat to it. Now it shows up as a solid color - to
get it see-through, just select the surface, press <kbd>Enter</kbd>, and
change the face flags to "translucent." If you're using 01narsh.cmp
you can use 01yellow.cmp or 01redmap instead of the translucency
method

## What's the difference between network lag and bad framerate?
Network lag is created when packets in a network game either don't reach
their destination, or are so slow that it impairs network play. If
you have a ping of 300-400 ms, this is pretty good, and you should't
see much lag. When you do get lag, the other players often jump from
one point to another, and are impossible to kill. Framerate,
however, is dependent on your computer/graphics card/etc. If you
have a very complex level, with tons of surfaces and
adjoins in view at the same time, the framerate may
drop, and the level could be very choppy in those areas. To fix the
framerate problem, work on making your architecture and cleaving
more efficient, tone down the detail level, or put architecture in
areas that will block the view of some of the more complex
architecture.

## How do I see my framerate?
Press <kbd>t</kbd> then type the word <kbd>framerate</kbd> - this will
display a number at the top of your screen. Watch it for a little
while to notice the things that cause it to drop (huge firefights,
translucency, complex architecture, etc).

# Lighting

## How do Lights work?

In JED, switch to light mode and place lights in sectors. Be sure not to
place them directly on an adjoin/thing/surface. When a light is
selected, press <kbd>Enter</kbd> to invoke the item editor. Here you can change
the lights properties. The most important values are the range and the
intensity. You will have to experiment to get the lighting correct, but
as common sense will tell you, the range dictates how far away the
lights will be seen, and the intensity is the brightness. After you
place your lights, press the tools/calculate lighting button. Then, your
lighting should show up in the 3d preview and in the game.

## I have a light in a sector, but when I calculate it, everything turns black.

Lighting data is stored in the vertices. If you have a sector that is
larger than the range of the light, the light won't reach the vertices,
and therefore no lighting data will be stored. Try raising the range and
intensity.

## I calculated the lighting, and most of my sector is now lighted, however, one surface is totally black.

This is because your light doesn't have the range/intensity to reach the
entire surface. This problem normally happens on surfaces that are very
long with no vertices. There is a very easy way to fix this, just select
the surface and add a small amount of extra light (like 0.1).  Alternatively, 
cleave the surface (to add vertices).

## I calculated the lighting, and now my whole map is black.

You didn't place enough lights to show up, read the above question, and
if that doesn't help, go to the 3d preview/options menu and click "fully
lit." This won't change it in the game, but in your 3d preview,
everything will show up again.

## How do I do colored lighting in Mysteries of the Sith?

First, go to the 3d preview/options menu and turn on colored lighting.
Make sure you have started a MotS level, and then read the [colored
lighting tutorial](/tutorials/mots_color/).

## Are there other ways to do lighting?

Yes. You can use surface lighting, which will add/subtract extra light
to the entire surface. This is good for darkening or brightening an
entire level or group of sectors. Just select a (or multiselect a group
of) sector(s) and press <kbd>Enter</kbd>. Now change the extra light value at
the bottom of the item editor.

## How do I make a blinking light?

This is done by adding a dynamic light (in thing mode) and adding a cog
to it. There are a couple of lights/cogs you can use, to find the
correct one, enter \*light into the mask box of the cog and thing
selection screens.

