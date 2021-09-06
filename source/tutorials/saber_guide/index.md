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
Saber Editing : Single Player Saber Color and Saber 2 Sword Tutorials  

-----

Author: [Jepman](mailto:jepman@endormoon.net)  
  

**NOTE:** This tutorial expects you to be familiar already with Jedi
Knight terms, and that you already have the required programs.

Part 1 : Single Player Saber Color

I will start this guide off by showing you how to change your Single
Player character's saber color for your own levels, WITHOUT renaming
existing mats and overwriting and such. It is quite a simple method.
What you need to do is add a few lines to your **kyle.cog** (or whatever
the name of your player character is (see [Part 2](#2)).

Anyway, we'll do this quickly. Open up **res2.gob** in Conman and go to
the /cog folder. Then scroll down to find **kyle.cog**, and extract it
to your project directory. Now, open **kyle.cog** up and add the
following three lines below to the symbols section:

    template    tpl_wall=+ssparks_wall           local
    template    tpl_blood=+ssparks_blood         local
    template    tpl_saber=+ssparks_saber

Here is the list of the saber colors available in Jedi Knight:

Yellow:  
    saberyellow0.mat  
    saberyellow1.mat  
Red 1:  
    saberred0.mat  
    saberred1.mat  
Red:  
    saberdred0.mat  
    saberdred1.mat  
Blue:  
    saberblue0.mat  
    saberblue1.mat  
Green:  
    sabergreen0.mat  
    sabergreen1.mat  
Orange:  
    saberorange0.mat  
    saberorange1.mat  
Purple:  
    saberpurple0.mat  
    saberpurple1.mat

Now, add the following lines to the symbols section:

    material playersbrtip_mat=x.mat           local (eg. x = saberred0.mat)
    material playersbrside_mat=x.mat          local (eg. x = saberred1.mat

Done yet? If so, in **kyle.cog**, go down to the *init\_kyle* section,
and add the line below under "SetTimerEx(1.50, 1, player, 0);"  
  

    jkSetSaberInfo(player, playersbrside_mat, playersbrtip_mat, 
    0.003, 0.001, 0.100, tpl_wall, tpl_blood, tpl_saber);

There you go, now you've changed the saber color. In the above line, you
could try and toy around with the three numbers (0.003, 0.001, 0.100) to
change the size of the saber blade. In order, these three numbers refer
to flex base radius, flex tip radius, and flex saber length. See what
you can come up with\!

<span id="2"></span>

Part 2 : Saber 2 Sword

**NOTE:** I assume that you have an external and internal sword models
ready.

Ok, now I will tell you how to set up your nice sword so that the saber
blade does not show up and you only see the 3DO. The bad news is, to do
this, you have to run this as a patch, and custom sabers are not
compatible with this. First off, download [this file](sabertrans.zip).
It is a zip containing all the default Jedi Knight saber mats, but are
all transparent (invisible) which will hide the saber blade, yet still
do damage.

To change the saber handle to your sword is very easy. Open up
**weapon\_saber.cog** and go to the symbols section. There you should
see the lines below :

    model    povModel=sabv.3do             local
    model    saberMesh=sabg.3do            local

Simply change *sabv.3do* and *sabg.3do* to the name of your models.
*povModel* is the internal model and *saberMesh* is the external one.
Now gob this thing up and run it in Patch Commander. It should work
perfectly fine.

Well anyway, if you have any trouble with these things, please feel free
to contact me at <jepman@endormoon.net>. Thank you for taking the time
to read this tutorial. I certainly hope it will serve you well for your
projects.

This tutorial was brought to you by
[Jepman](mailto:jepman@endormoon.net) of [Specter
Studios](http://www.jedilegacy.net/specter/)
