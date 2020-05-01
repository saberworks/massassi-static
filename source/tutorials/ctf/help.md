---
title: How to Setup the Parameters in CTF Cogs
author: SavageX
email: SavageX@spinxs.com
description: >
   More information on setting up the CTF cogs.
date: 
original: ctfhelp.htm
category: jk
---

\-- Written by SavageX

Setting up the parameters in the Cogs for CTF is very easy affair to do
but it can be complicating to setup if you don't understand the
parameter's use. This tutorial will help explain how to set it up.

CTF\_Main.cog
-----

This is obviously the main cog for CTF levels. Without the cog, you
can't play CTF. All values must be set for it to work.

Here are the parameters you'll encounter in this cog when assigning them
in JED:

|                              |                                                                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **flag_red(thing):**         | Set this value to the red team's flag thing in the level.                                                                           |
| **flag_gold(thing):**        | Set this value to the gold team's flag thing in the level.                                                                          |
| **flag_ghost_red(thing):**   | This is for the ghost position (ghost is a thing) that will set the position for the red team's flag to be placed. This is merely used for sending the flag back (teleport) to its original position whenever the flag is dropped or captured. This should be set to the same position as the red flag is at startup, for obvious reasons. |
| **flag_ghost_gold(thing):**  | Same as above, except that it's for the gold team's flag.                                                                           |
| **start_room(sector):**      | Used for the lobby room. All the walkplayer things you've placed in the lobby MUST BE IN THIS SECTOR in order for it to work.       |
| **mark_red(sector):**        | This is used to mark a player as a red team player. This is also the sector that will send the player to the red base.              |
| **mark_gold(sector):**       | This is used to mark a player as a gold team player. This is also the sector that will send the player to the gold base.            |
| **limit1(surface):**         | This is used for the max score limit board in the lobby. This is where the players can change the max score limit. Limit 1 is used to change the number by HUNDREDS. |
| **limit2(surface):**         | Same as limit 1 BUT limit 2 is used to change the number by TENS.                                                                   |
| **limit3(surface):**         | Same as limit 1 BUT limit 3 is used to change the number by ONES.                                                                   |
| **score_display_cog(cog):**  | In order to locate the score display cog for the main cog to use, set this value to the cog number that the score display is using in the cog list (ex. if the score display cog is number 9 in the cog list, set this value to 9) |
| **red_start(thing) (1-7):**  | This is used for placing the players into their base after selecting a team. These are not the team's start positions. Do not set these to walkplayers. These are for ghost positions and are not the respawn positions for the game. |
| **gold_start(thing) (1-7):** | Same as above except it's for the gold team.                                                                                        |
| **players_red1(surface):**   | Used for showing the players in the lobby how many players are on the red team. This value is used to display the players in TENS.  |
| **players_red2(surface):**   | Used for showing the players in the lobby how many players are on the red team. This value is used to display the players in ONES.  |
| **players_gold1(surface):**  | Used for showing the players in the lobby how many players are on the gold team. This value is used to display the players in TENS. |
| **players_gold2(surface):**  | Used for showing the players in the lobby how many players are on the gold team. This value is used to display the players in ONES. |

CTF\_Respawn.cog
-----

This cog is used to set the respawn mask for the players. See the "how
to setup walkplayers" for more info on this.

Here are the parameters you'll encounter in this cog when assigning them
in JED:

|                       |      |
| --------------------- | ---- |
| **mark_red(sector):** | This is used to assign the player to the red team. This should be the exact same value you have used in the mark_red value in the CTF_main.cog. |
| **mark_gold(sector):** | This is used to assign the player to the gold team. This should be the exact same value you have used in the mark_gold value in the CTF_main.cog |


CTF\_safeentry.cog
-----

The purpose of this cog is for incase when a player misses the sector
that is supposed to send the player to his new team. This usually
happens in high lag games. It works by having a player enter a sector
that is below the sector (the one that is supposed to send the player to
the new team) and teleporting him to a ghost position that is in the
lobby. It will also make the player have a neutral skin (the original
Kyle Katarn skin) when this happens.

Here are the parameters you'll encounter in this cog when assigning them
in JED:

|                         |                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Mark_red(sector):**   | This is used for the sector that will teleport the player back to the lobby (by using the ghost_red thing for placement) if the player missed the mark_red sector that is used in the CTF_respawn.cog and the mark_red in the CTF_main.cog. This sector should NOT be the same as the mark_red sector used in those two cogs. This should be linked to a sector that is below the mark_red of the other cogs.                                                          |
| ** Mark_gold(sector):** | Same as above, except for the gold team.                                                                               |
| **Ghost_red(thing):**   | Used to placement of the player when player is teleported back up to the lobby. Use in conjunction with the mark_red.  |
| **Ghost_gold(thing):**  | Used to placement of the player when player is teleported back up to the lobby. Use in conjunction with the mark_gold. |

CTF\_displayscore.cog
-----

This cog layout is a bit tricky to understand so bare with me here. This
cog is used to display the score in the game via scoreboards on the
walls in the level. This display will allow up to the max of 4
scoreboards for each team. The cog's values are organized in a certain
fashion. The first letter is the team it's for (r or g), the second is
for the number it is for (l is the large number, m is for the middle
number, and r is for the last number) and the last one is the number it
should be grouped with (ex. rl0 + rm0 + rr0 is the first scoreboard for
the red team) since I have explained the layout here, I won't list the
values here since it would be redundant.

CTF\_iconsclient.cog
-----

There are no values to set for this cog BUT you MUST have this placed in
the "placed cogs" section in your level so that the level is aware of
the cog. This is used to sync the icon display (such as the flags and
keys) so that level will run smoothly in MP. Without this, only the host
of the game will have his icons working.

CTF\_keysclient.cog
-----

There are no values to set for this cog BUT you MUST have this placed in
the "placed cogs" section in your level so that the level is aware of
the cog. This is used to sync the inventory items such as the keys so
that everyone in the game will know when a player has a key or not.
Without this cog, don't expect the CTF doors that use the keys to work
for the players that are not the host.

CTF\_keyred.cog and CTF\_keygold.cog
-----

Like the icon and key client cogs, these cogs have no values to set BUT
MUST be placed in the cog section of your level so that the game is
aware of the cogs. These are for the key powerups that player will find
in CTF games.

CTF\_doorred.cog and CTF\_doorgold.cog
-----

These work just like the 00\_door.cog in Jedi Knight so I won't explain
these since it's pointless.

How to Setup Walkplayers
-----

Ok, here is the number one thing in CTF that is probably the most
confusing element to understand. Walkplayers are not setup by the CTF
Cogs at all\! It is the way they are inserted into the level. If you
have already placed walkplayers in your level before reading this
tutorial, DELETE them. Here is the way you should place them in you
level:

|                             |                                                                                                       |
| --------------------------- | ----------------------------------------------------------------------------------------------------- |
| **walkplayers (1-8):**      | The first 8 walkplayers you place in the level must be used for the start positions for the red team. |
| **walkplayers (9-16):**     | The next 8 walkplayers you will place are for the gold team starting positions.                       |
| **walkplayers (the rest):** | The rest of the walkplayers you will place are for the lobby room. There is no limit here since it is only the first 16 walkplayers you insert that are for the teams. |

Because of this, you cannot (no matter how much you complain) have more
than 8 start positions (walkplayers) for each team. The reason why it is
like this because of the Respawn Mask (a flag value) that is set to the
players when they pick a team. The CTF\_Respawn.cog is the cog the gives
the respawn mask value to the players.

Well, I hope this tutorial has helped you understand how to setup the
cogs for a CTF level. If you still have questions regarding CTF, you can
email me. For even more help, just examine the
LEC CTF levels that come with JK in JED.
