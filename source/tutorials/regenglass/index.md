---
title: Regenerating Glass
author: PC_McCloud
email: PC_McCloud@Hotmail.com
description: >
    Explains how to use the regenerating glass cog available in the cog section of the site.. Also touches upon client/server cog usage in general
date: 1999-01-02
original: tutor.html
category: jk
---

Author: PC\_McCloud  

Also Reference [Breaking Glass](/tutorials/glass/) By Executor

This is a how to make Regenrating Glass and Basic Client/Server .cog
Tutorial

Things Needed :

Regenerating "[Breaking Glass (C/S)](bc.zip)" By Pele

1.  Fire up JED and start a New JK / MotS Project with the Defult sector
    slected Cleave it as I have just about in half like so..

![](1.gif)

2.  Now select one of the surface to be your Glass and Select the .mat
    you would like ...

In Jedi Knight :

  - 00wglas1.mat
  - 00wglas2.mat

In MotS :

  - 00\_glass.mat
  - 00wglas1.mat
  - 00wglas2.mat

There are many mats that make Good Subs for the Glass mats tha give it a
little diffrent look So experment with the mats..

Now you need to Change some on the Serface Properties

1.  The "+GEO" needs to beed changed from "0" to "4" this is so you can
    see the Glass (See Image \#2 Below)
2.  The "+ADJOIN FLAGS" needs to be set from "7" to "5" (See Image \#3
    Below)
3.  If you want to see Past "Transparten" you Can Set the "+FACE FLAGS"
    to "2" (See Image \#4 Below)

<div class="tutorial-table" markdown=1>

|                                     |                                     |                                     |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| ( +GEO ) settings                   | ( +ADJOIN FLAGS) settings           | ( +FACE FLAGS ) settings            |
| [![Click to Inlarge](2.gif)](2.gif) | [![Click to Inlarge](3.gif)](3.gif) | [![Click to Inlarge](4.gif)](4.gif) |
| [Click to inlarge](2.gif)           | [Click to inlarge](3.gif)           | [Click to inlarge](4.gif)           |

</div>

 

3.  Now after cleaving and setting up the serfaces you need to save your
    project ans Place the "bcc.cog" & "bcs.cog" in to your Poject
    Directory

![](5.gif)

4.  After saving you need project press "F7" and "Add Cog" on the left
    of the window click on the "Project Directory" and add Both
    "bcc.cog" & "bcs.cog" the Server .cog is the where you add in your
    Serface infomation Imput in to "Glass (serface)" your first serface
    you want to be glass add in the serface with a space in the middle
    like so "0 5". do the same for the other Glass serface and put it in
    to "Glass2 (Serface)" as i have done .. Don't mess with the
    "spawnpoints" or "density" for now

![](6.gif)

For me my Serfaces were "0 5" and "1 5" See how I placed the Serface
information in to the "bcs.cog". There is No information to imput in to
the Client Cog "bcc.cog" for it to work properly you MUST have it. One
Client Cog can Handle the Operation of more then one Server Cog, So if
you wish to add more then glass serface all you to add in another Server
Cog. The Client Cog will work for all the Glass serfaces in your level.

Now that you have compleated all the Steps above Save and Test your
level if you compleated them Properly you will have Glass the Brakes
when you Shoot it and Respawns after 60 Seconds

<div class="tutorial-table" markdown=1>

|            |
| :--------: |
| ![](7.gif) |
| ![](8.gif) |

</div>

Good Luck and Happy Glass Shooting :-)  
By PC\_McCloud
