---
title: "The Basics: Lesson 2"
ext: htm
---

Okay, now we are going to get just a little bit more involved in some of
the level editing features.  

[TOC]

## Surface Flags
Surface flags are the things you can use to give your surface different
properties. The easiest way to explain this is to use the example of the
floors. Notice as you're walking around in Jedi Knight, sometimes you
will be walking on metal, sometimes you will be walking on dirt, and
sometimes you will be just walking. All these different effects are
created with simple surface flags.  
  
What are the different flags? Well, there are many. The most important
one is "floor." If you want to be able to walk on the bottom of your
sector, you must set the bottom surface flag to "floor." You can then
choose a type, as in metal, dirt, whatever. You can also choose from
icy, deep water, very deep water, etc. All these have different effects.
If you ever have a problem with a suface, make sure the correct flag is
set. Oh, just a note, if you want your sky to look like a sky, and act
like a sky (I.E. bullets just fly forever, instead of explode on
impact), just select the surface, and set it's flag to, yep, you guessed
it, "sky."  
  
## Sector Flags
Much like surfaces, sectors have their own flags too. For instance, you
know that water is much different than plain air. So, you just select
the sector you want to be water, and change its flag to "underwater."
Note that this will not LOOK like water at first, but if you walk into
it, you will be swimming.  
  
There are other sector flags, just experiment around with them. Oh, and
if it says "unknown," just leave it alone, nobody can figure out what it
does, and believe me, we've tried.  
  
## Lighting
Okay, lights aren't really physical things. They are more like points in
space you use to calculate lighting. You never see an actual light,
unless you put a light-type 3do in. Even if you do that, the lighting
itself will not really be coming from the 3do.  
  
Lighting information is stored in vertices. If you have a long hallway
with very few vertices, it will be hard to light up. Lighting is
something you just have to learn by trial an error. Insert a light,
calculate your lighting, and take a look at the results.  
  
## Adjoining
Okay, this gets a little deep. Say you have two cubed sectors that are
EXACTLY the same. Notice that if you walk around either of them, you are
trapped in that cube. Well, what if you want to get to the other cube?
The method is called adjoining, and here's the breakdown:  
  
Basically, adjoining is taking two identical surfaces, and linking them
together. When you link them together, you are able to pass through the
adjoin. So, if you have two cubed sectors that are adjoined, when you
actually walk in the level, it will appear as one big rectangular
sector.  
  
To adjoin sectors, you have to pick a surface that's exactly the same on
both sectors. Then, you move them exacly on top of eachother. The
important thing is to have the vertices at exactly the same point in
space. Then, you select the surface, and link it together. Very simple
in theory.  
  
## Rules Regarding Sectors
Rules? Yep, there are rules you have to follow. Actually, there is
really only one, but it is very important. Your sector must be Convex.
What is convex? Well the opposite of concave of course\! Anyway, an
example of a convex sector is a cube, or a pyramid. Now, a NON-convex
sector is one that looks like a hook, or an elbow. If you wanted a
sector shaped like that, you'd have to make sure to have two separate
sectors, adjoined at the elbow joint. That's a very simple example, but
there is more info around the JK editing sites on that, so I won't
elaborate. It's actually kind of hard to get a non-convex sector
anymore, especially if you're aware of what you're doing.  
  
Why none of these types of sectors? Well, the Jedi Knight engine goes
funky if you have them. Sometimes all you will get is some Homming (Hall
of Mirrors -- you will learn about that, trust me). Sometimes the level
simply won't load. Also, you will be walking along, playing the level,
everything looking normal, and then you will enter the sector. All of a
sudden, your player will just start falling and falling, and just die.
Very interesting, but not something you would want to wish on your
dedicated fans eh?  

