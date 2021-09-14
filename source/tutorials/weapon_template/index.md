---
title: Weapons Templates
author: GuNbOy
email: rocesk8er@hotmail.com
description: >
    Unravels the mysteries behind weapons templates, and tips on making your own.
date: 2000-03-21
original: original.html
category: jk
---

Author: GuNbOy

In this tutorial you will learn how to make different types of weapons
templates and how to make them work together in the static.jkl file.

**Things you will need are:**

  - [tempref.txt](tempref.txt)
  - [static.jkl](static.jkl)

## The Basics of Templates

  - All templates that are based on another one, have to come after the
    one they are based on in the jkl.  
    *Example:* when you have a create thing in a template, lets say an
    explosion has the creatething=+smoke or something. you would have to
    put +smoke in the jkl before the explosion you just made or it wont
    work.
  - All templates are either based on something unless you make a new
    one that will be based on **none**
  - **ALL weapons templates (particle weapon and explosion) have to have
    typeflags=0x\* these flags differ for each type so check the [JK
    specs](http://www.code-alliance.com/doc_jk/jk_specs/jkspecs.htm) or
    refer to the tempref.txt file that i give you.**

## Messages in Templates

  - **orient=(0.000000/0.000000/0.000000):** this I'm not sure about. I
    think it's the position at which the template is created. I don't
    suggest you play around with this too much, I don't see any point in
    changing it.
  - **type=(explosion, particle, weapon):**
      - **weapon** is used for the actual weapon projectile that gets
        thrown, shot or dropped, etc.
      - **particle** is for making a bunch of particles appear, then
        disappear over time (this is how smoke is done)
      - **explosion** is for when a weapon hits something and explodes.
  - **collide=(0,1 or 3) used for weapons**
      - **collide=0** means that it won't collide with things. I'm not
        sure how this would be useful in a weapon template...
      - **collide=1** means that it collides when something is within a
        sphere of the object (see: move size)
      - **collide=3** means that it will collide with an object if that
        object touches one of its faces (this is usually used for 3do
        architecture, I think)
  - **creatething=(whatever you want)** means that when the thing is
    fired (weapon) it will create some template that you specify. If
    used in an explosion, it then can create stuff like smoke clouds,
    shockwaves, fire, clouds, etc.
  - **light=flex** gives your template a dynamic light value. Replace
    flex with a number
  - **model3d=\*.3do** gives your template a 3do so you can see it
    (weapons)
  - **move=(none, path or physics)**
      - **none** is pretty self-explanatory; it won't move.
      - **path** means that it will move by a specific path using frames
        and such (usually not used for weapons... something more like an
        actor usually)
      - **physics** means that it moves with physical properties like
        mass velocity etc.
  - **movesize=flex** is for how big the sphere in the collide message
    is. You want to make the flex in this about the same size as the 3do
    you have (in jku's)
  - **par=\*.par** is for particle files like the sphere in Force
    Protection.
  - **soundclass=\*.snd** is for things like explosions making noise and
    when a TD hits the ground and make that \*ping\* sound
  - **sprite=\*.spr** specifies the sprite file used for the template.
    Usually used for explosions, but can be used in a weapon in place of
    a 3do, like Force Destruction.
  - **timer=flex** tells how long the thing will be in the game for.
    When the timer runs out it is removed; when this happens it will
    make its explosion. If there is none then it will simply cease to
    exist.

  

## Specific Messages for Weapon Types

  - **airdrag=flex** is how much resistance from "air" there is on the
    weapon.
  - **angvel=(x/y/z)** refers to angular velocity, I dunno... maybe it
    has something to do with a weapon spinning?
  - **buoyancy=flex** refers to how much buoyancy the weapon has (if it
    floats in water)
  - **maxrotvel=flex** refers to maximum rotational velocity; how fast
    it spins, possibly connected to the angvel message
  - **mass=flex** refers to how much it weighs, so if it has gravity (if
    it falls) in the physics flags then it indicates how fast to fall.
  - **physflags=0x\*** is best left to checking the JK specs or the
    tempref file that comes with this tutorial to figure out what the
    flags do.
  - **surfdrag=flex** determines how much resistance the thing gets from
    from a floor or wall if it has to slide along one of those surfaces.
  - **vel=(x/y/z)** indicates how fast it moves in each direction, the
    "Y" vector being forward, I think...
  - **explode=(template\*)** is for what the weapon does when it hits a
    wall or just explodes.
      - \* the template would be something like a sprite or a dust cloud
        (can be used with a timed sprite to make a bullet hole that
        stays on the walls\!\!\!)
      - if the \*template is an explosion, not just a bullet-hit-type
        thing, you do the same for it, but probably use a bigger sprite
  - **fleshhit=(template\*)** this is for when your weapon hits a player
    or actor (non-droid)
      - you can do cool effects by making the \*template blood or
        something, so that blood appears only when a player is hit
  - **cog=\*.cog** is used for linking the projectile with a cog such as
    00\_smoketrail.cog that will leave a smoke trail behind the
    projectile.
  - **trailthing=template** this is used for the force lightning
    template, those little pieces of "electricity" are 3dos trailing
    after the main projectile

  

## Messages for Explosions

  - **blasttime=flex** is the delay between the explosion and when the
    damage is done (if you'll notice Force Destruction is delayed a
    little like this)
  - **damage=flex** the amount of damage it does
  - **damageclass=0x\*** check the JK specs or the tempref file that
    comes with this tutorial to figure out what the flags do.
  - **debris=template** flings debris out every which way if the
    typeflag=0x80. It can be used up to four times
  - **flashrgb=(r/g/b)** makes a flash with the color of your choice
    (red/green/blue)
  - **force=flex** the force is like how violent the explosion is, more
    force the farther and harder you get thrown from it.
  - **maxlight=flex** refers to the maximum amount of light
  - **range=flex** determines how big of an area the blast will cover
  - **rate=flex** indicates how fast the damage will dissipate (i.e. the
    higher the rate the less damage it does as you get farther away from
    it)

  

## Particle Messages

  - **material=\*.mat** refers to the material of the particles
  - **range=flex** indicates how far away the particles will go from
    their origin
  - **minsize=flex** sets what size the smallest the particles can be
  - **timer=flex** sets how long the particles will last
  - **rate=flex** determines how fast the particles are destroyed after
    the timer runs out (particles per second)
  - **maxthrust=flex** sets how fast the particles move
  - **elementsize=flex** sets the maximum size of the particles
  - **count=flex** determines the number of particles used
  - **yawrange=flex** indicates the range of yaw (not sure, changes the
    way the particles move)
  - **pitchrange=flex** indicates the range of pitch (not sure, same as
    above)

  

## How to Make the Freakin' Things Work\!\!\!

I hope I didn't scare you all away with that crapload of messages...
anyway, first off you go get the static.jkl I included with the
tutorial. Open it up in notepad, then go to the templates section. After
the \_gexplosion and \_gweapon templates, make the templates you want.
Here are some examples to show you how to compile the templates
yourselves (if this wont help you, go look at the tempref document and
look at a weapon similar to the one you want to create, then modify it
to fit your needs. Be sure to put the weapons explosion and anything
that the explosion creates BEFORE the template itself, otherwise it
won't work).

<p class="tutorial-gray">
+bulletcloud none orient=(0.000000/0.000000/0.000000) type=particle timer=0.150000 typeflags=0x3f material=00gsmoke.mat range=0.006000 rate=64.000000 maxthrust=4.000000 elementsize=0.004000 count=16
<em>// this is for when the bullet hits the wall</em>
</p>

<p class="tutorial-gray">
+bloodcloud +bulletcloud material=bloody.mat range=0.030000 count=40
<em>// all I changed from the bullet cloud was: material so it looks like
blood, range so its a bigger area, and count so it will be more dense.
this will be used when a person gets hit by the bullet</em>
</p>

<p class="tutorial-gray">
+bulletfleshhit _gexplosion timer=0.001000 soundclass=exp_bullet.snd creatething=+bloodcloud typeflags=0x0
<em>// for when a person is hit</em>
</p>

<p class="tutorial-gray">
+bullethit _gexplosion timer=0.001000 soundclass=exp_bullet.snd
creatething=+bulletcloud typeflags=0x0
<em>// for when the bullet hits something not living</em>
</p>

<p class="tutorial-gray">
+bullet _gweapon thingflags=0x20000001 light=0.400000 model3d=bullet.3do size=0.001000 movesize=0.001000 soundclass=bry.snd maxrotvel=0.000000 vel=(0.000000/20.000000/0.000000) explode=+bullethit fleshhit=+bulletfleshhit damage=30.000000 mindamage=10.000000 typeflags=0x20440d rate=15.000000
</p>

*As you can see, I put the `+bullethit` under `explode=` and the
`+bulletfleshhit` under the `fleshhit=` so it will do different things when
you hit a person or a wall* :)

Now you can experiment with all sorts of things. I hope that this helped
a little to make people not totally confused about templates.
