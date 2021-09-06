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
Templates: A Reference  

-----

Author: [GMS\_Slug](mailto:gms_slug@hotmail.com)  
  

Templates can be found in your jed\\jeddata folder. The two files are
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

    # DESC:
    # BBOX: 0 0 0 0 0 0
    _decor        none       orient=(0.000000/0.000000/0.000000) type=cog collide=1 move=path

*This is the "parent" template. You see it contains a little
information.*

    # DESC:   
    # BBOX: 0 0 0 0 0 0
    _structure    _decor     collide=3 thingflags=0x8

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

> \_actor -- Generic values for actors  
> \_walkplayer -- The player himself.. Walkplayers are spawn points in
> levels, they refer to kyle.cog which handles spawning effects for
> players.  
> \_flyactor -- Any enemy that flies  
> \_humanactor -- Any enemy that walks  
> \_swimactor -- Any enemy that swims  
> \_droidactor -- The template used for droids, this is entirely based
> off of \_humanactor, but has different thingflags.  
> \_civilian -- This is based off of \_humanactor also, but with quite a
> few different values  
> \_darkjedi -- This is.. \*insert dramatic music\* the dark jedi
> template.

**Structures**- Structures are simply objects. From rocks to computer
consoles, most of the 3dos you see in the game are structures.. All
structure templates can be ultimately linked back to \_structure. Like
actors, there are several different types of structure templates.

> \_structure -- Just your average structure  
> \_walkstruct -- Structure you can walk on.  
> \_ghostructure -- This is \_struct with a collide of 0. I have no idea
> why this exists.. My guess would be it helped the level designers keep
> track of what's going on in a level.. IE, if they were moving a
> structure to a ghost object, maybe it helped them to see the word
> "ghostSTRUCTURE" instead of just "ghost"..  
> \_zwalkstruct -- This is pretty much the same as \_walkstruct, only it
> has the "metal" flag.. This simply means that when you step on it,
> it's makes a metal clinking noise.. This saves you from having to make
> a new .snd file for metal objects..  
> \_decor -- This is a structure that you cannot walk on. These are
> generally used for 3dos that the player will never reach in a level..
> It's used instead of other structure templates because there are less
> flags for JK to calculate in \_decor.  
> \_ghostdecor -- This is the same as \_decor, but with a collide of 0.
> I haven't a clue as to why this one exists either.. My guess would be
> the same as \_ghoststructure..  
> \_throwable -- This makes an object throwable by force throw.. It also
> makes it affected by gravity.

**Powerups**- Powerups are just items you can pick up throughout the
game..

> \_powerup -- Just your standard powerup item  
> \_droppowerup -- Nothing special here either, these are just the
> powerups you collect from dead enemies.

**Explosions**- Explosions in JK refer to explosions (duh) and things
like sparks when a laser hits flesh or a wall.

> \_explosion -- Standard explosion..

**Weapons**- A more suitable word for this would be projectile. \_weapon
templates refer to the shots produced by guns, not the actual guns
themselves. Lightning, Destruction, and Blinding are based on \_weapon
along with fists, grenades, and mines.

> \_weapon -- Generic values for projectiles.  
> \_debris -- This is just standard debris from an explosion.  
> \_debris2 -- Same as debris, just uses a different explosion

**Miscellaneous**- Just two templates that don't belong anywhere else..

> \_limb -- Ever lop off an enemy's arm? You made a limb\!
> Congratulations\!  
> \_shard -- Shards are produced when you shatter glass.

**Definitions**- There are alot of things in templates that may need a
little explaining, so here ya go..

> aiclass -- The .ai file that a template uses.  
> airdrag -- How much of a drag effect air has on an object (ie. How
> much air slows down an object's movement )  
> angvel -- The direction in which a thing spins. The format is x/y/z  
> blasttime -- Determines how long a blast will last. Found in explosion
> templates.  
> buoyancy -- This is the floating ability of an object. You'll notice
> when you shoot into water, your projectile floats up a bit or just
> slows down.. Buoyancy at work..  
> chance -- chance that the dark jedi will block with his saber (thnx to
> JM for this info)  
> cog -- This is the a cog that the template uses.. Enemies use actor
> cogs, the walkplayer uses kyle.cog, powerups use pow\_blah.cogs,
> etc...  
> collide -- The type of collision detection on an object.. 0= no
> collision checking, 1=collision checking along the radius of the
> object, and 3= collision checking on the faces of the object... If the
> object is gonna be solid, it must have either 1 or 3... 1 will make a
> bubble of "solidity" around an object so you often cannot climb around
> on the 3do (a great example of this is the lambda shuttle).. 3 will
> detect collisions along the faces of the 3do, this is the best way,
> but it's hard on the system. (Thnx to Necare for the info)  
> count -- This is the amount of sprites that a template produces.  
> creatething -- This tells the template to create a thing when it is
> called... A good example is the rail detonator charge.. When it is
> fired, it's template tells JK to create a smoke trail using the
> creatething command.  
> damage -- This is the amount of damage something inflicts.. damage is
> done randomly though, so this is simply the most that it can
> inflict.  
> damageclass -- This is the type of damage something inflicts.. It can
> be either force, magic, fire, impact, energy, crushing, or freezing..
> I may have missed something, but you get the point.  
> debris -- This is the debris released when an explosion occurs  
> elementsize -- This is the size of individual sprites in a template.
> Sprites are generally very very small..  
> error -- the chances of an aiming error--found in darkjedi templates  
> explode -- This tells which template to use for the explosion. An
> example is when the bryar bolt hits a wall it uses +laserhit.  
> eyeoffset -- The distance from the ground to an enemy/player's
> vertical line of sight (ie, the measurement from the ground to their
> eyes)  
> fireoffset -- This is the distance in x/y/z form that the projectile
> appears from the enemy/player.  
> flashrgb -- This is the rgb (red, green, blue) value of a flash
> produced by an explosion. RGB value is a ratio system showing the
> ratio of red to green to blue in a given color.  
> fleshhit -- Same as explode, only it tells which template to use when
> it hits a player.  
> force -- No, it's not THE force.. It's the force of impact on a punch
> or any other type of impact.  
> fov -- Field Of Vision.. Just the range of vision from left to right
> that an enemy/player can see at once.  
> health -- The starting health of an enemy, player, and in some
> instances, an object.  
> height -- ????????????????????????????????????????????????????????  
> jumpspeed -- The speed at which you jump.  
> light -- Things in JK give off light.. This is the amount that they
> give off  
> lightintensity -- The intensity of the player's field light.  
> lightoffset -- The distance from the ground to the source of the
> player's field light.  
> mass -- This is the objects mass. As far as I can figure, it simply
> dictates at what speed an object falls.  
> material -- The .mat file that a template uses.. You'll only see
> "material" in a template for a sprite.  
> maxheadpitch -- The highest an enemy/player can look up.  
> maxhealth -- The maximum amount of health an enemy/player can get.
> (player can get health boosts or force healing, dark jedi can
> regenerate health using force healing.. nothing else regenerates
> health)  
> maxlight -- Maximum light a thing can give off  
> maxrotthrust -- Max Rotation Thrust..I'm guessing it's the fastest
> that an enemy/player can START turning around (IE, when you first
> start turning, it's the maxrotthrust, then as you pick up speed, you
> reach the maxrotvel).. maxrotthrust is always a little lower then
> maxrotvel, that's what leads me to believe this.  
> maxrotvel -- Max Rotation Velocity.. It's the fastest that an
> enemy/player can turn around.  
> maxvel -- Max Velocity.. It's the fastest an enemy/player can move in
> a straight line.  
> mindamage -- This is the least damage something can deal out.  
> minheadpitch -- The lowest an enemy/player can look down.  
> minsize -- Minimum size that a sprite can be  
> model3d -- The .3do that the template uses.  
> move -- This is the method of movement for an object. Not many
> templates include "move". Options are either physics, which means JK's
> physics affect the thing, or path, which means it cannot be
> affected.  
> movesize -- The movesize is always the same as the size, except for
> one instance, the sequencer charge template. It's guessed that the
> movesize is larger and is the bubble which triggers the explosion of
> the secondary mode of the sequencer charge. (thanks for the seq charge
> info from Erwinl)  
> Orient -- This is simply the orientation in x/y/z form.. Only 1
> template has an orientation other then (0.0000/0.0000/0.0000), so I
> think it's a safe bet to use it for all your templates..  
> particle -- Refers to a .par file.. That little green sphere that
> wraps around you when you use protection is a .par file, to give you
> an idea of what they are..  
> phsyflags -- These determine what factors of JK physics will affect
> the thing.  
> pitchrange -- The range of error either up or down.. (ie, how far
> below or above your target the projectile can hit)  
> puppet -- Puppets are actually .pup files. They control what .keys
> will be played for specific actions. For more info on pups and keys go
> to darkjedi.com's unnoficial JK specs.  
> range -- This is the maximum range that a smoke cloud (made of
> sprites) will spread before dissapearing..  
> rate -- Rate of creation for certain templates like projectiles and
> sprites.. This is to prevent too many projectiles or sprites existing
> at once which would hurt bandwidth and memory. (Also, who wants a
> rateless projectile? \[other then a cheater that is\] That'd mean no
> pause in between shots..)  
> respawn -- The time before an object respawns.. Found in powerup
> templates  
> thingflags -- These play significant roles in every template. Flags
> can control a huge amount of things. Look at darkjedi.com's Unofficial
> Jedi Knight Specs to see alot of the flags..  
> size -- Size is just the radius of the 3do.. There are some
> exceptions, but nearly every LEC 3do uses the radius... Oh, in case
> you don't know... Radius of a 3do can be found by opening it up with a
> text editor..  
> soundclass -- This is a .snd file. A .snd controls what sound (in .wav
> format) will be played for specific events like running on metal,
> falling, etc.. .snd files are simply text files.  
> sprites -- Sprites are 2d images. Sparks and explosions among other
> things are sprites  
> staticdrag -- A thing's natural resistance to things like sector
> thrust. (Thnx to Necare for that explanation)  
> surfdrag -- Like airdrag, only it controls the amount of drag a
> surface has on the object.  
> timer -- If there's a timer in a template, it means that the object is
> destroyed after a given amount of time.. This is used to cut down the
> amount of objects in a level, freeing up memory and in multiplayer
> games, bandwidth.  
> trailrandangle -- Randomizes the aim of the trailing thing.  
> trailthing -- Creates a trailing thing for a projectile. Used to
> create the smoke of the secondary fire concussion blast, and also used
> in force lightning..  
> type -- This doesn't mean anything to JK, it's documentation for
> editors.. Unless you're making alot of templates, and you won't be
> able to remember what each one is, you won't ever need to use this..
> It's just an editing crib-note :)  
> typeflags -- Type of thing the template is for.  
> vel -- This is just a thing's velocity  
> weapon -- This is the template of the weapon an enemy uses.  
> weapon2 -- This is the weapon an enemy will switch to in certain
> circumstances.. Enemies with rail detonators for instance, will swipe
> at you with the rail detonator when you get close.. That swiping
> attack is their "weapon2".  
> yawrange -- The range of error either left or right.. (ie, how far
> left or right of your target that the projectile can hit)
