---
title: New Player Characters
author: CrazedUp
email: jepman@hotmail.com
description: >
    Learn how to use other skins for the main player character (replaces Kyle Katarn or Mara Jade).
date: 1998-09-13
original: original.html
category: jk
---

Author: CrazedUp  
  

In this tutorial, I will teach you how to make a new player character
with the 3do used for Kyle Katarn Or Mara Jade.

I assume you have a new character (skin) made with the `ky.3do` (for JK)
and the `kk.3do` (MOTS KKatarn) or the `mj.3do` (MOTS Mara Jade). I also
assume you have your character ready and that you will not be needing
help in making it. If that is your problem, please see the tutorial on
[Creating a Skin](/tutorials/skins/).

## Part 1 - The Easy Way

1.  Put your character 3do in your Project directory, and do the
    following:
      - If making new character for JK : Just simply save 3do as `ky.3do`
        (This disables you to use the usual KKatarn skin elsewhere)
      - If making new KKatarn for MOTS : Save 3do as `kk.3do` (" ")
      - If making new MJade for MOTS : Save 3do as `mj.3do` (" ")
2.  This is it, just make sure to have all the correct mats in the
    project directory (except if textures already in `Res2.gob` (JK) or
    `JKmres.goo` (MOTS))
3.  In JED the walkplayer should appear as your character, same thing in
    the game.

## Part 2 - The Less Easy Way

This method allows you to use kkatarn or mjade character some other way
in the game (Ex. Enemy, helper). In this tutorial, I use the `002.3do`
(The Kyle Fett Skin from JK BFP) renamed to `bounty.3do`

1.  Name the 3do whatever you want (I renamed `002.3do` to `bounty.3do`).
2.  Open up the `Master.tpl` (JK) or the `MOTS.tpl` (MOTS) in wordpad and do
    the following:
      - Find the `"walkplayer"` template if making new kkatarn character
        in either MOTS or JK
      - Find the `"marawalkplayer"` template (MOTS only) if making new
        mjade character.
3.  Copy the contents from `# Desc:` to `walkplayer/marawalkplayer`. The
    following is the template code I use for my `bounty.3do`:

>     # DESC:
>     # BBOX: -0.03730128 -0.01387423 -0.1184614 0.03811364 0.03983956 0.06454442
>     mercaneryplayer _actor type=player thingflags=0x20000401 light=.2 model3d=bounty.3do size=.065
>     movesize=.065 puppet=ky.pup soundclass=kybobafett.snd cog=ben_m.cog surfdrag=3 airdrag=.5
>     staticdrag=.3 health=100 maxhealth=100 maxthrust=2 typeflags=0x1 error=.5 fov=.71 chance=1

The previous lines should be copied and pasted. They should appear as
three lines in the template file just like above.

  - Enter the description of the template in `# DESC:`  
  - `# BBOX:` already has the right numbers in it
  - In `mercenaryplayer` put the name of the character (No need of
    walkplayer of player)
  - In the `model3d` part put the name of your 3do, and change the
    `soundclass` to the one you one to use for you own character. The
    original snd name is `ky.snd` or `mj.snd` but I use the `kybobafett` one
    for my guy. The rest is to mess around with at risk.

Oh\! The `ben_m.cog` is the cog I use to make the saber green instead of
orange (MOTS stuff here)

This done, I wish you have a great time with your levels and characters.

