---
title: Targeting Reticule
author: Obsidian
email: Dragons_bane@hotmail.com
description: >
    Close-up look at the COG implemented in the targeting reticule used in certain Force powers.
date: 1999-11-16
original: reticule.html
category: jk
---

Author: Obsidian

This tutorial isn't meant for the new coggers... You have to have an
understanding of how cog works and some knowledge of where files go in
the resource directory.  I'm going to assume you know what goes where in
this tutorial.

The targeting reticule is mainly used in force powers (blinding, grip,
pull, ect.) and tells the player who/what they have targeted.  It has no
effect other then that, as the force power's cog already knows what's
targeted and what's not.

I reviewed many ways to write this tutorial, and I concluded that
displaying the cog I made and giving detailed comments would be the best
route, as (how i first started writing this tutorial) doing it step by
step takes a long time, and is quite confusing (not only when writing
it, but reading one as long as this one would have to be would be no
walk in the park either).

There are 3 commands (there may be more, but you only need 3)
specifically used for the target reticule.

* `JkSetTargetColor(color1, color2, color3);`
* `JkSetTarget(Thing);`
* `JkEndTarget();`

`JkSetTargetColor` sets the colors of the 3 'bouncing' circles. `color1` is
the color of the 1st circle, `color2` is the color of the 2nd circle, and
`color3` is the color of the 3rd circle.

`JkSetTarget` sets the bouncing circles on the specified thing.  Only one
thing can be targeted in this manner at a time.

`JkEndTarget` removes the circles from whatever they were set to by
`JkSetTarget`.

Below is the cog i wrote for this tutorial, it is also (should be
anyway) available in the zip.  It replaces force pull.  
(note: the included cog is not commented)

```
# Jedi Knight Cog Script
# force_pull.cog
#
# Cog for the Target Reticule tutorial.
#
# Obsidian 11-14-99

symbols

int      player              local
int      potential          local
int      victim              local

flex    MaxDist=5      local

message    startup
message    activated
message    deactivated
message    pulse

end

# ==========

code

startup:

player = GetLocalPlayerThing();

return;

# ..........

Activated:

victim = -1;

SetPulse(.33);

return;

# ..........

pulse:

   victim = -1;

   potential = FirstThingInView(player, 90, 8, 0x404);  // Get the First thing in player's sight that is either a player (0x400) or an actor (0x4)

   while(potential != -1)
   {
     if(
         HasLOS(player, potential) &&    // If the player can see potential
         (potential != player) &&    // if the player isn't potential
         (VectorDist(GetThingPos(player), GetThingPos(potential)) <= MaxDist) &&    // Make sure potential is no farther then MaxDist (5 JKUs)
         !(GetThingFlags(potential) & 0x200)    // *shrugs*
       )
        {
            victim = potential;    // If potential passes all the filters, then make it the victim.  Victim, however, will not be killed until the deactivated: message is run.
        }

      potential = NextThingInView();    // Get the next thing if potential was filtered out
   }

   if(victim != -1)     // If we have a victim targeted
   {
      jkSetTargetColors(1, 2, 3);    // Set the colors for the target circles
      jkSetTarget(victim);    // Set Victim as the target and activates the circles
   }
   else
   {
      jkEndTarget();    // If we have no victim, then turn off the circles/cancel the last target.
   }
 

return;

# ..........

deactivated:

If((HasLOS(player, victim)) && (victim != -1))    // Makes sure that victim is still in sight, and that we actually have a victim to kill
{
   DamageThing(victim, GetThingHealth(victim), 0x4, player);    // Turns the lights out on whoever is targeted
}

SetPulse(0);
jkEndTarget();    // Turn circles off

return;

end 
```

That is the bare bones necessary for using the target reticule as it is
used in the force powers.  By changing the flags on `FirstThingInView`
(thing type flags) you can make it select other things besides
players/actors (such as in force pull).  

Good luck and happy editing,

Thanks go out to ThreeDee for inspiring this tutorial (those that are
wondering if I could have made this thanks any smaller.. no, believe me
i tried :)) (j/k)
