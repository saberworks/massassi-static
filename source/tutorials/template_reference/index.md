---
title: Template Reference
author: GMS_Slug
email: gms_slug@hotmail.com
description: >
    Explains all the things you see in templates.
date: 1998-10-08
original: index.shtml
category: jk
---

Author: GMS_Slug

Templates can be found in your `jed\jeddata` folder. The two files are
called master.tpl and mots.tpl; mots.tpl obviously handles templates for
mots, and master.tpl is for JK. Templates are written in the .jkl of
every level. They contain vital info for every single "thing" in the
level, such as what 3do to use for the "thing," whether the thing has ai
or not, etc. If you're going to be adding new 3dos to your level, it's
important for you to know templates. Template knowledge also comes in
handy quite frequently even if you aren't adding new 3dos to your level.
Say you want a shuttle in your level. Now, you may have noticed with the
shuttle that you can't ever walk up to it.. you keep getting blocked by
some kind of invisible wall.. You can change this with a little template
editing. Various things like that which don't seem important now, but
become little hassles in the future if you don't know what to do about
them.

Templates are often based off of parent templates. That is to say, a
template such as \_decor will be referred to in many different
templates. \_decor contains information that will be used for any
template based off of it. This helps template makers because they have
to specify much less.. Confused? Here's an example..

```
    # DESC:
    # BBOX: 0 0 0 0 0 0
    _decor        none       orient=(0.000000/0.000000/0.000000) type=cog collide=1 move=path
```

*This is the "parent" template. You see it contains a little
information.*

```
    # DESC:   BBOX: 0 0 0 0 0 0
    _structure    _decor     collide=3 thingflags=0x8
```

*This template is based off of \_structure so it has a collide of 3, and
since \_structure is based off of \_decor, both \_structure and
\_walkstruct have an orient value of (0.000000/0.000000/0.000000).
\_walkstruct changes the thingflags value however, so it does not have
the same flags as \_structure.*

Easy enough, right? Well, it can get a bit crazy at some points.
Backtracking some templates will make you go through nearly a dozen
others (as opposed to the 2 templates you have to go through to find out
where \_walkstruct is based off of) before you find out where the whole
thing started. You won't ever really need to do that kind of
backtracking though, so don't worry.

<span class="underline">**Different types of parent templates**</span>

Staying on the basics, there are different types of parent templates
(parent templates are what I'm calling templates that start with an
underscore) These include things like powerups, projectiles, enemies,
etc..

**Actors**- Actors are simply enemies, and the player himself. The only
exception I can find to this is grenades. For whatever reason, they are
marked as actors in templates. There are several different types of
actors..


> <span class="tutorial-blue">\_actor</span><br>
> Generic values for actors  
> 
> <span class="tutorial-blue">\_walkplayer</span><br>
> The player himself.. Walkplayers are spawn points in
> levels, they refer to kyle.cog which handles spawning effects for
> players.  
> 
> <span class="tutorial-blue">\_flyactor</span><br>
> Any enemy that flies  
> 
> <span class="tutorial-blue">\_humanactor</span><br>
> Any enemy that walks  
> 
> <span class="tutorial-blue">\_swimactor</span><br>
> Any enemy that swims  
> 
> <span class="tutorial-blue">\_droidactor</span><br>
> The template used for droids, this is entirely based
> off of \_humanactor, but has different thingflags.  
> 
> <span class="tutorial-blue">\_civilian</span><br>
> This is based off of \_humanactor also, but with quite a
> few different values  
> 
> <span class="tutorial-blue">\_darkjedi</span><br>
> This is.. \*insert dramatic music\* the dark jedi
> template.

**Structures**- Structures are simply objects. From rocks to computer
consoles, most of the 3dos you see in the game are structures.. All
structure templates can be ultimately linked back to \_structure. Like
actors, there are several different types of structure templates.

> <span class="tutorial-blue">\_structure</span><br>
> Just your average structure  
> 
> <span class="tutorial-blue">\_walkstruct</span><br>
> Structure you can walk on.  
> 
> <span class="tutorial-blue">\_ghostructure</span><br>
> This is \_struct with a collide of 0. I have no idea
> why this exists.. My guess would be it helped the level designers keep
> track of what's going on in a level.. IE, if they were moving a
> structure to a ghost object, maybe it helped them to see the word
> "ghostSTRUCTURE" instead of just "ghost"..  
> 
> <span class="tutorial-blue">\_zwalkstruct</span><br>
> This is pretty much the same as \_walkstruct, only it
> has the "metal" flag.. This simply means that when you step on it,
> it's makes a metal clinking noise.. This saves you from having to make
> a new .snd file for metal objects..  
> 
> <span class="tutorial-blue">\_decor</span><br>
> This is a structure that you cannot walk on. These are
> generally used for 3dos that the player will never reach in a level..
> It's used instead of other structure templates because there are less
> flags for JK to calculate in \_decor.  
> 
> <span class="tutorial-blue">\_ghostdecor</span><br>
> This is the same as \_decor, but with a collide of 0.
> I haven't a clue as to why this one exists either.. My guess would be
> the same as \_ghoststructure..  
> 
> <span class="tutorial-blue">\_throwable</span><br>
> This makes an object throwable by force throw.. It also
> makes it affected by gravity.

**Powerups**- Powerups are just items you can pick up throughout the
game..

> <span class="tutorial-blue">\_powerup</span><br>
> Just your standard powerup item  
> 
> <span class="tutorial-blue">\_droppowerup</span><br>
> Nothing special here either, these are just the
> powerups you collect from dead enemies.

**Explosions**- Explosions in JK refer to explosions (duh) and things
like sparks when a laser hits flesh or a wall.

> <span class="tutorial-blue">\_explosion</span><br>
> Standard explosion..

**Weapons**- A more suitable word for this would be projectile. \_weapon
templates refer to the shots produced by guns, not the actual guns
themselves. Lightning, Destruction, and Blinding are based on \_weapon
along with fists, grenades, and mines.

> <span class="tutorial-blue">\_weapon</span><br>
> Generic values for projectiles.  
> 
> <span class="tutorial-blue">\_debris</span><br>
> This is just standard debris from an explosion.  
> 
> <span class="tutorial-blue">\_debris2</span><br>
> Same as debris, just uses a different explosion

**Miscellaneous**- Just two templates that don't belong anywhere else..

> <span class="tutorial-blue">\_limb</span><br>
> Ever lop off an enemy's arm? You made a limb\!
> Congratulations\!  
> 
> <span class="tutorial-blue">\_shard</span><br>
> Shards are produced when you shatter glass.

**Definitions**- There are alot of things in templates that may need a
little explaining, so here ya go..


> <span class="tutorial-red">aiclass</span><br>
> The .ai file that a template 
> uses.  airdrag -- How much of a drag effect air has on an object (ie. How
> much air slows down an object's movement )  
> 
> 
> <span class="tutorial-red">angvel</span><br>
> The direction in which a thing spins.  The format is x/y/z  
> 
> 
> <span class="tutorial-red">blasttime</span><br>
> Determines how long a blast will last. Found in explosion
> templates.  
> 
> <span class="tutorial-red">buoyancy</span><br>
> This is the floating ability of an object. You'll notice
> when you shoot into water, your projectile floats up a bit or just
> slows down.. Buoyancy at work..  
> 
> <span class="tutorial-red">chance</span><br>
> chance that the dark jedi will block with his saber (thnx to
> JM for this info)  
> 
> <span class="tutorial-red">cog</span><br>
> This is the a cog that the template uses.. Enemies use actor
> cogs, the walkplayer uses kyle.cog, powerups use pow\_blah.cogs,
> etc...  
> 
> <span class="tutorial-red">collide</span><br>
> The type of collision detection on an object.. 0= no
> collision checking, 1=collision checking along the radius of the
> object, and 3= collision checking on the faces of the object... If the
> object is gonna be solid, it must have either 1 or 3... 1 will make a
> bubble of "solidity" around an object so you often cannot climb around
> on the 3do (a great example of this is the lambda shuttle).. 3 will
> detect collisions along the faces of the 3do, this is the best way,
> but it's hard on the system. (Thnx to Necare for the info)  
> 
> <span class="tutorial-red">count</span><br>
> This is the amount of sprites that a template produces.  
> 
> <span class="tutorial-red">creatething</span><br>
> This tells the template to create a thing when it is
> called... A good example is the rail detonator charge.. When it is
> fired, it's template tells JK to create a smoke trail using the
> creatething command.  
> 
> <span class="tutorial-red">damage</span><br>
> This is the amount of damage something inflicts.. damage is
> done randomly though, so this is simply the most that it can
> inflict.  
> 
> <span class="tutorial-red">damageclass</span><br>
> This is the type of damage something inflicts.. It can
> be either force, magic, fire, impact, energy, crushing, or freezing..
> I may have missed something, but you get the point.  
> 
> <span class="tutorial-red">debris</span><br>
> This is the debris released when an explosion occurs  
> 
> <span class="tutorial-red">elementsize</span><br>
> This is the size of individual sprites in a template.
> Sprites are generally very very small..  
> 
> <span class="tutorial-red">error</span><br>
> the chances of an aiming error--found in darkjedi templates  
> 
> <span class="tutorial-red">explode</span><br>
> This tells which template to use for the explosion. An
> example is when the bryar bolt hits a wall it uses +laserhit.  
> 
> <span class="tutorial-red">eyeoffset</span><br>
> The distance from the ground to an enemy/player's
> vertical line of sight (ie, the measurement from the ground to their
> eyes)  
> 
> <span class="tutorial-red">fireoffset</span><br>
> This is the distance in x/y/z form that the projectile
> appears from the enemy/player.  
> 
> <span class="tutorial-red">flashrgb</span><br>
> This is the rgb (red, green, blue) value of a flash
> produced by an explosion. RGB value is a ratio system showing the
> ratio of red to green to blue in a given color.  
> 
> <span class="tutorial-red">fleshhit</span><br>
> Same as explode, only it tells which template to use when
> it hits a player.  
> 
> <span class="tutorial-red">force</span><br>
> No, it's not THE force.. It's the force of impact on a punch
> or any other type of impact.  
> 
> <span class="tutorial-red">fov</span><br>
> Field Of Vision.. Just the range of vision from left to right
> that an enemy/player can see at once.  
> 
> <span class="tutorial-red">health</span><br>
> The starting health of an enemy, player, and in some
> instances, an object.  
> 
> <span class="tutorial-red">height</span><br>
> ????????????????????????????????????????????????????????  
> 
> <span class="tutorial-red">jumpspeed</span><br>
> The speed at which you jump.  
> 
> <span class="tutorial-red">light</span><br>
> Things in JK give off light.. This is the amount that they
> give off  
> 
> <span class="tutorial-red">lightintensity</span><br>
> The intensity of the player's field light.  
> 
> <span class="tutorial-red">lightoffset</span><br>
> The distance from the ground to the source of the
> player's field light.  
> 
> <span class="tutorial-red">mass</span><br>
> This is the objects mass. As far as I can figure, it simply
> dictates at what speed an object falls.  
> 
> <span class="tutorial-red">material</span><br>
> The .mat file that a template uses.. You'll only see
> "material" in a template for a sprite.  
> 
> <span class="tutorial-red">maxheadpitch</span><br>
> The highest an enemy/player can look up.  
> 
> <span class="tutorial-red">maxhealth</span><br>
> The maximum amount of health an enemy/player can get.
> (player can get health boosts or force healing, dark jedi can
> regenerate health using force healing.. nothing else regenerates
> health)  
> 
> <span class="tutorial-red">maxlight</span><br>
> Maximum light a thing can give off  
> 
> <span class="tutorial-red">maxrotthrust</span><br>
> Max Rotation Thrust..I'm guessing it's the fastest
> that an enemy/player can START turning around (IE, when you first
> start turning, it's the maxrotthrust, then as you pick up speed, you
> reach the maxrotvel).. maxrotthrust is always a little lower then
> maxrotvel, that's what leads me to believe this.  
> 
> <span class="tutorial-red">maxrotvel</span><br>
> Max Rotation Velocity.. It's the fastest that an
> enemy/player can turn around.  
> 
> <span class="tutorial-red">maxvel</span><br>
> Max Velocity.. It's the fastest an enemy/player can move in
> a straight line.  
> 
> <span class="tutorial-red">mindamage</span><br>
> This is the least damage something can deal out.  
> 
> <span class="tutorial-red">minheadpitch</span><br>
> The lowest an enemy/player can look down.  
> 
> <span class="tutorial-red">minsize</span><br>
> Minimum size that a sprite can be  
> 
> <span class="tutorial-red">model3d</span><br>
> The .3do that the template uses.  
> 
> <span class="tutorial-red">move</span><br>
> This is the method of movement for an object. Not many
> templates include "move". Options are either physics, which means JK's
> physics affect the thing, or path, which means it cannot be
> affected.  
> 
> <span class="tutorial-red">movesize</span><br>
> The movesize is always the same as the size, except for
> one instance, the sequencer charge template. It's guessed that the
> movesize is larger and is the bubble which triggers the explosion of
> the secondary mode of the sequencer charge. (thanks for the seq charge
> info from Erwinl)  
> 
> <span class="tutorial-red">Orient</span><br>
> This is simply the orientation in x/y/z form.. Only 1
> template has an orientation other then (0.0000/0.0000/0.0000), so I
> think it's a safe bet to use it for all your templates..  
> 
> <span class="tutorial-red">particle</span><br>
> Refers to a .par file.. That little green sphere that
> wraps around you when you use protection is a .par file, to give you
> an idea of what they are..  
> 
> <span class="tutorial-red">phsyflags</span><br>
> These determine what factors of JK physics will affect
> the thing.  
> 
> <span class="tutorial-red">pitchrange</span><br>
> The range of error either up or down.. (ie, how far
> below or above your target the projectile can hit)  
> 
> <span class="tutorial-red">puppet</span><br>
> Puppets are actually .pup files. They control what .keys
> will be played for specific actions. For more info on pups and keys go
> to darkjedi.com's unnoficial JK specs.  
> 
> <span class="tutorial-red">range</span><br>
> This is the maximum range that a smoke cloud (made of
> sprites) will spread before dissapearing..  
> 
> <span class="tutorial-red">rate</span><br>
> Rate of creation for certain templates like projectiles and
> sprites.. This is to prevent too many projectiles or sprites existing
> at once which would hurt bandwidth and memory. (Also, who wants a
> rateless projectile? \[other then a cheater that is\] That'd mean no
> pause in between shots..)  
> 
> <span class="tutorial-red">respawn</span><br>
> The time before an object respawns.. Found in powerup
> templates  
> 
> <span class="tutorial-red">thingflags</span><br>
> These play significant roles in every template. Flags
> can control a huge amount of things. Look at darkjedi.com's Unofficial
> Jedi Knight Specs to see alot of the flags..  
> 
> <span class="tutorial-red">size</span><br>
> Size is just the radius of the 3do.. There are some
> exceptions, but nearly every LEC 3do uses the radius... Oh, in case
> you don't know... Radius of a 3do can be found by opening it up with a
> text editor..  
> 
> <span class="tutorial-red">soundclass</span><br>
> This is a .snd file. A .snd controls what sound (in .wav
> format) will be played for specific events like running on metal,
> falling, etc.. .snd files are simply text files.  
> 
> <span class="tutorial-red">sprites</span><br>
> Sprites are 2d images. Sparks and explosions among other
> things are sprites  
> 
> <span class="tutorial-red">staticdrag</span><br>
> A thing's natural resistance to things like sector
> thrust. (Thnx to Necare for that explanation)  
> 
> <span class="tutorial-red">surfdrag</span><br>
> Like airdrag, only it controls the amount of drag a
> surface has on the object.  
> 
> <span class="tutorial-red">timer</span><br>
> If there's a timer in a template, it means that the object is
> destroyed after a given amount of time.. This is used to cut down the
> amount of objects in a level, freeing up memory and in multiplayer
> games, bandwidth.  
> 
> <span class="tutorial-red">trailrandangle</span><br>
> Randomizes the aim of the trailing thing.  
> 
> <span class="tutorial-red">trailthing</span><br>
> Creates a trailing thing for a projectile. Used to
> create the smoke of the secondary fire concussion blast, and also used
> in force lightning..  
> 
> <span class="tutorial-red">type</span><br>
> This doesn't mean anything to JK, it's documentation for
> editors.. Unless you're making alot of templates, and you won't be
> able to remember what each one is, you won't ever need to use this..
> It's just an editing crib-note :)  
> 
> <span class="tutorial-red">typeflags</span><br>
> Type of thing the template is for.  
> 
> <span class="tutorial-red">vel</span><br>
> This is just a thing's velocity  
> 
> <span class="tutorial-red">weapon</span><br>
> This is the template of the weapon an enemy uses.  
> 
> <span class="tutorial-red">weapon2</span><br>
> This is the weapon an enemy will switch to in certain
> circumstances.. Enemies with rail detonators for instance, will swipe
> at you with the rail detonator when you get close.. That swiping
> attack is their "weapon2".  
> 
> <span class="tutorial-red">yawrange</span><br>
> The range of error either left or right.. (ie, how far
> left or right of your target that the projectile can hit)
