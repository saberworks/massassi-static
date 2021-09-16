---
title: Force Fields
author: GMS_Slug
email: gms_slug@hotmail.com
description: >
    Learn to create a switched force field.
date: 1998-03-20
original: ff.htm
category: jk
---

Author: GMS_Slug

  
You'll need a gob extractor for this one. I suggest conman available
from [the programs section](/programs/).
Yes, there are some forcefield cogs that don't require extraction, but
they're not worth anyone's time.  
  
1. Extract *10\_ffieldswitch.cog* from jk1.gob in the
Jediknight\\episode directory. There are a few others you can use too,
but in my opinion, 10\_ffieldswitch is the best...It allows textures to
be displayed when hit (other forcefields can only handle a solid color
.mat) and the switch can be activated by gunfire as well as regular
activation with the spacebar. There are others you can use, experiment
if you like, they all work the same (some may require a little different
info then others, but nothing confusing once you figure out
10\_ffieldswitch) 00forcefield.cog doesn't have a switch, so you
probably won't want that one..  
  
2. Put it in your project directory. If you don't have one, make one.
The project directory, in case you don't know, is simply where your .jed
and .\~je files are.  
  
3. Open up JED and extrude one side of the default sector (this will
make the adjoin that the force field will be applied to)  
  
4. Note the numbers of both surfaces that make up the adjoin.  
  
5. Now to make the switch.. Just cleave a little 0.1x0.1 square on
another wall. Oh, and in a level that you're going to release, all you
switches should be indented into the wall a little. (don't take the time
to do it right now, this level will never be released to the public.. at
least I hope not) It doesn't impact the game, but a switch on a flat
wall just looks like it was painted on. Note the number of the surface
that will act as your switch.  
  
6. Ok, if you made a project directory for this, you'll have to save
the .jed before you proceed. (otherwise, JED won't recognize that you
have a project directory, and you won't be able to choose
10\_ffieldswitch.cog from "Placed Cogs") Go to the "tools" menu and
click on "Placed Cogs," then go to "Add Cog," and then "Project
Directory".. Select *10\_ffieldswitch.cog*. It will ask for the
following values..  

    <div class="tutorial-table" markdown=1>

    > |                                           |    |
    > |-------------------------------------------|----|
    > | `switch (surface)`                        | This is simply the surface acting as your switch. Sector first then surface.. A switch on sector 0, surface 3 would look like 0 3 (note the space in between them) in "Placed Cogs" |
    > | `damsurf(surface)`<br>`damsurf2(surface)` | These are the surfaces that make up the adjoin. Enter the numbers the same way you entered them for the switch surface. |
    > | `maxdamage`<br />`mindamage`              | These are the maximum and minimum amounts of damage a player can take by hitting the forcefield. The actual amount of damage is a random number between the mindamage and maxdamage. |

    </div>
  
  
7. Textures. Well, if you're using 10\_ffieldswitch, you can use any
texture your heart desires, as long as it's not a single color mat.. As
near as I can tell, 10\_ffieldswitch will not support solid color mats..
However, most textures look ridiculously stupid as a forcefield. A safe
bet would be 00wwarny or 00wwarnr. They're caution textures (like that
yellow and black striped tape they put up near construction sites) Just
make sure that both sides of the adjoin have the same texture.  
  
8. Save and test. If you've done everything correctly, you've got
yourself a nice little forcefield.. Hooray\!
