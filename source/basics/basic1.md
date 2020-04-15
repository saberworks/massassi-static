---
title: "The Basics: Lesson 1"
ext: htm
---

Okay, we're going to go BASIC here. I'm talking, as basic as it gets. If
you have any idea about JK Editing, you might want to stop here, but who
knows, you might learn something.  

[TOC]

## Sectors
These are the primary building blocks ("holes" actually, but that will
come later) of a Jedi Knight level. A basic sector is just a cube that
you can walk IN. So, if you want a big square room, you just create one
sector, drop the player down into it, and that's it. The thing to
remember though, is that when you insert a sector, you insert OPEN
space, so the player can walk into it.  
  
## Vertices  
Vertices are points in space, represented by little dots in level
editors. Picture your cube again, and picture a dot at each corner. A
cube sector is made up of a bunch of little dots.  
  
## Surfaces  
A surface is a set of at least 3 vertices, on a plane. Does that make
sense? We're not talking flying here, we're talking FLAT plane. Picture
this: A sheet of paper. One side of a sheet of paper is one surface. Put
a bunch of pieces of paper together, like a house, and you get a sector
right? And put dots at all the corners, and you get all the vertices.  
  
That brings me to another point. A square surface has 4 vertices.
Always. So, if you have a cubed sector, you have 6 surfaces right? Top,
bottom, four sides. Now, if each of these six surfaces has four
vertices, you get what? 6 x 4 = 24 Twenty four vertices in each sector.
Read on:  
  
## Linking  
You can link surfaces or vertices. A sector is made up of 24 vertices,
but are linked together in groups of 3. So, you can only really SEE 8
vertices if you are looking at one cubed sector. This is because when
you link vertices together, they appear as one. Just take it on faith
that there are more than that. You will learn this as you go along
anyway.  
  
## Texture  
Each surface, when created, has a default texture on it. You can change
the texture to any texture you want. It is basically just a picture
file, tiled onto the surface. Textures in Jedi Knight are stored in
files with the extension of .mat -- there are converters out there that
allow you to take a .mat file, and convert it to a .bmp file, and vice
verca. This will allow you to create your own textures.  
  
Okay, a bit more on these. Mat files actually have 4 different picture
files in them. They are all at different sizes. Why? Well when you are
far away, the Jedi Knight engine will make visible the biggest texture.
As you get closer, it cycles through the various sizes, until you
finally get real close, and it shows the smallest one. If you have a
really nice graphics card (I.E. Voodoo II or equivilent) you can
actually see these transitions taking place.  
  
## 3do  
Okay, a 3do is any object that is not made of normal level architecture.
What does that mean? Well first off, .3do is the extension of a
filename. Anything with that extension is referred to as a 3D object.
You get the idea. 3D objects include anything, as stated above, that is
not level architecture. 3dos in JK were created using 3d Studio Max, I
believe. Anyway, 3dos are things like enemies, guns, weapons fire (the
actual projectile), couches, beds, chairs, powerups, at-st's, etc.
Nowadays, you can make 3dos with the Jed level editor, as well as a 3d
program that can export in .asc or similar formats. There is a program
that will convert them to .3do files for you.  
  
3dos, like regular level geometry, are made up of many many surfaces.
Each surface must be textured just like level geometry. Currently there
is no program that will do this for you, so you have to open the .3do
file in Notepad, or a similar text editor, and do it manually. 3dos use
textures in .mat format, just like level architecture. Most 3do-specific
mat files, however, only store 1 size mat in it. This is because 3dos
don't switch textures as you get closer, they always use the same one.  
  
## Sprites  
I don't know much about sprites and how they work. I think I can give
you a quickie definition though. If you play Jedi Knight, and shoot your
gun, you will see the the 3do projectile fly away. When it hits you will
see an animation of the explosion. This animation is created with 2D
sprites. No matter where you are in relation to the explosion, it will
always look the same. That is because it is 2D, not 3d. Sprites also
make up things like the smoke behind a rail charge, sparks, and the
little particle streams you see in some of the levels.  
  
## Cogs  
Cogs are another thing I just don't dealve into very deeply. Basically,
it's like this: Jedi Knight has it's own programming language called,
you guessed it, COG. Cog scripts will allow you to do most anything in
the game. They make doors open (doors are just 3dos with a cog
attached, telling it to open when a switch is hit, etc), elevators move,
rivers flow, textures scroll, and on and on. They are in charge of
weapons, force powers, and all the scoring in a multi-player game.
Basically, if you want your level to DO anything other than just sit
there, you will have to use a cog.  
  
Fear not, however, because you can use all the LEC cogs with little or
no problems, and without having to learn the language. Most things, like
doors and elevators, just require you to fill in a few values from
within the level editor.  

