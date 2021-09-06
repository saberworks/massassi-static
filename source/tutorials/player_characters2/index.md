---
title: 
author: 
email: 
description: >

date: 
original: index.shtml
category: 
---

Author:[![Printable Version](/images/printable.gif)](tutorial_print.shtml) New
Player Characters 2  

-----

Author: [Dark Phoenix](mailto:ZarbonDBZ83@aol.com)  
  

This tutorial explains another way to use other models for the player. I
tried doing this myself using the [tutorial by "Crazed
Up"](/tutorials/player_characters/) and it just didn't work for me but
this method worked just fine. Another advantage to using this method is
that you are able to have different models for different levels in a
multi-level episode.

Open the master.tpl file for your episode using WordPad or a similar
text editor. If you do not have a master.tpl file in your project
directory it can be found in your JED directory in the jeddata folder.
Copy the file and put it in your project directory.

Copy these lines from your master.tpl file. It should be somewhere near
the top (or just copy it from this tutorial).

> 
> 
>     # DESC: Player
>     # BBOX: -0.03730128 -0.01387423 -0.1184614 0.03811364 0.03983956 0.06454442
>     walkplayer _actor type=player thingflags=0x20000401 light=0.200000 
>     model3d=ky.3do size=0.065000 movesize=0.065000 puppet=ky.pup 
>     soundclass=ky.snd cog=kyle.cog surfdrag=3.000000 airdrag=0.500000
>     staticdrag=0.300000 health=100.00 maxhealth=100.00 maxthrust=2.00 
>     typeflags=0x1 error=0.50 fov=0.71 chance=1.00

Paste this line on the bottom. Where it says model3d= change it from
ky.3do and put whatever 3do you are using for the player. Now change
where it says walkplayer to walkplayer2 or whatever you want. Now just
make sure the 3do and any mats that go with it are in your project
directory (unless the mats are already included in res2.gob or .goo).

You can make as many different walkplayers as you want if you want to
use different models for different levels.

There are many more neat things you can do besides just change what the
player looks like.

Changing Health and Maximum Health  
All you have to do is change the value beside health= and maxhealth=

Changing the Sounds Your Player Makes  
Where is says soundclass= change the file name to the snd file you want
to use for your player. I wont go into how to create your own snd files
in this tutorial but if you have BFP2 you can find snd files for some of
the BFP2 skins. You can also extract snd files from the res2.gob.

There are alot of other nifty things you can do by fooling around with
this, but I don't recommend changing anything around unless you know
what you're doing. If you *do* decide to mess around, make sure you have
a backup master.tpl file handy in case you mess something up.
