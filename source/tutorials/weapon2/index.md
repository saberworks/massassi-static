---
title: "Weapons: Part 2"
author: EvanC
email: ev@wave.co.nz
description: >
    This tutorial teaches you how to make simple modifications in weapon cogs.
date: 1998-08-011
original: weap2.htm
category: jk
---

Author: EvanC
  
In this tutorial you will learn how to modify the bryar pistol to shoot
concusion blasts and sound like a repeator.  
  
You will need an ungob program and a text editor(notepad is fine for
this).  
  
With your Ungob program open up Res2.gob and extract weap\_bryar.cog.
Open the cog up in Notepad. At the top you will notice this:  
  

``` 

# Jedi Knight Cog Script
#
# WEAP_BRYAR.COG
#
# WEAPON 2 Script - Bryar Pistol
#
# The trusty weapon of Kyle Katarn. This is actually an older modified rifle
# that has been cut down to more of a pistol size. It is very accurate but
# somewhat of a low power weapon. This weapon has only one type of fire.
#
# - Affected by MagSealed sectors/surfaces.
#
# [YB & CYW]
#
# (C) 1997 LucasArts Entertainment Co. All Rights Reserved
```

  
  
At the start of each line is a "\#". That means that everything on a
line that comes after the "\#" is ignored. So this entire section is
waffle that doesn't mean anything to JK. In here you can put your
copyright information, email adress ETC when you make your own weapon.
Anyway, skip about one line down from that part. There should be the
word "symbols". This is the start of the symbols section, and this
section ends at the word "end" (which is about 45 lines down). In here
is where you put in all the resources that the cog will use. To start
with we will change the sound that the bryar uses. Scroll down about 10
lines from the "symbols" line. What you should see is this:  
  

    sound       outSound=pistout1.wav               local
    sound       mountSound=df_bry_ready.wav         local
    sound       dismountSound=PutWeaponAway01.wav   local
    sound       fireSound=pistol-1.wav              local

  
  
This is the sound section of this cog. It lists all the sounds used in
the cog. The line with "fireSound" has the name of the bryar pistols
fireing sound, "pistol-1.wav". What we want to do is change the
"pistol.wav" into "rpeatrlp.wav" which is the repeator firesound. Now
the bryar will sound like a repeator when it fires. Now what we will do
is scroll down a line untill we see this:  
  

    template    projectile=+bryarbolt               local

  
  
THis is the projectile the bryar uses (+bryarbolt). We want to change it
to "+concbullet". Now the bryar bolt will fire a concusion bullet and
make the sound of a repeator when it shoots.  
  
To use this modified cog save it as "weap\_bryar.cog" in your
JK/resource/cog folder and run JK.  
  
If you wanted to make your own weapon you probably wouldn't just replace
the projectiles or sounds, you'd make your own. Making new projectiles
is covered in part 3 of this tutorial.  

