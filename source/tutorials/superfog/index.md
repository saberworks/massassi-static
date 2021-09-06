---
title: Super Fog
author: Zagibu
email: zagibu@gmx.ch
description: >
    This tutorial is about adding fog to JK MP/SP levels using a special cog, allowing the user to create very individual fog (even colorchanging).
date: 2002-04-07
category: jk
---

Author: Zagibu

This tutorial will teach you how to add fog to JK levels using the
[included superfog.cog](superfog.zip). First
of all, you have to know that fog in JK is a difficult thing (not for
the lvleditor, but for the cogger), and that it can't be done very well.
The most common way (used in superfog.cog) is to add a greyshade to the
display via the NewColorEffect() verb. The main problem of this method,
though, is that you can't see any fog from a non-foggy place. There are
ways to work around this problem, and we will discuss one later. Now
let's start:

Build your level. Place a ghost thing where you want the fogcenter to
be. The fogcenter is not really the center of the fog, but the position
where the fog's intensity reaches maximum. The fog gets lighter when
moving away from the fogcenter.

Put the superfog.cog into your level (Placed Cogs F7). Fill in the
fields as listed below (for a quick fogtest with standard grey fog, fill
in the fogcenter, fogsector and offsector fields and leave the default
values in the other fields):

> 
> 
> |                 |                                                                                                                                                                                                                                                 |
> | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `fogcenter`     | The ghost's thing number.                                                                                                                                                                                                                       |
> | `maxfogred`     | Intensity of fogcolor's red. Maximum value is around 290.                                                                                                                                                                                       |
> | `maxfoggreen`   | Intensity of fogcolor's green. Maximum value is around 290.                                                                                                                                                                                     |
> | `maxfogblue`    | Intensity of fogcolor's blue. Maximum value is around 290.                                                                                                                                                                                      |
> | `maxdistance`   | Maximum range of fog in JKUs. The fog will slowly fade out when moving away from the fogcenter, until it reaches 0 at maxdistance.                                                                                                              |
> | `linear`        | This determines the fading style of the fog. Set 1 for standard linear fading or any other value for square function fading. Basically, the second style fades out slower than the first one.                                                   |
> | `fluctuation`   | This is the max amount of random color that will be added to your basic fog color. It makes the fog more realistic, IMO. Put in 0 for no fluctuation.                                                                                           |
> | `psychedelic`   | This is the fluctuation style. If set to 0, the fluctuation will be equally added to all three color values, making a standard grey fluctuation. If set to any other value, the fluctuation will be calculated for all color values seperately. |
> | `interval`      | The fog update interval in seconds.                                                                                                                                                                                                             |
> | `fogsector0-19` | If the player enters these sectors, fog will be displayed. You only have to enter passable sectors, which border on nonfoggy areas (doorsectors, passable windowsectors, ...) and sectors, which contain walkplayers.                           |
> | `offsector0-19` | If the player enters these sectors, the display will be cleared from fog. Enter sectors, which border on foggy areas (usually the sectors bordering on sectors you entered in the fogsector fields).                                            |
> 

That's all of the fields. Don't forget to hit the refresh button...

Two more things:

  - The color values of this cog sum up. So, if you have two cogs with
    overlapping maxdistances, you might get full white fog fx in some
    areas. Make sure that the distance between two fogcenters exceeds
    the sum of the two maxdistances.
  - If you have an open area with fog and a building with a portal to
    this area, you can set the portal sector's surface (the one that can
    be seen from inside the building after setting it's geomode to 4)
    material to a solid white (e.g. whitey.mat, included in zip file)
    and set it's face flags to translucent. That will give the player
    inside the building the feeling as if he was looking into a foggy
    area (set up the fog without this addition and nobody outside it's
    range will notice it). Have a look at the included level.

\[Zagibu\]
