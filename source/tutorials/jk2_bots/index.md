---
title: 
author: 
email: 
description: >

date: 
original: index.shtml
category: 
---

Author:[![Printable Version](/images/printable.gif)](tutorial_print.shtml) How
To Make A Bot  

-----

Author: [NakTawii Nuji](mailto:GraalYo@hotmail.com)  
  

This is the easy way to create a Bot. You don't need any program at all
except Notepad.

Bot Personality

You will need to copy the .jkb file from the base skin you made or from
another model (editing the galak skin, for example). Open the file with
Notepad and begin editing lines (comments indicating what does what
accompany nearly every line). Rename this file however you'd like. Go to
your desktop, create a new folder called **botfiles**, and put the new
.jkb file in there.

Basic Bot Options

Create a new text document and call it \[the name you want\].bot (don't
forget to change the extension from .txt to .bot). In the .bot write the
following:

``` 
 {
  name          "The name you want to call it, keep the quotes"
  model         (write the name of the model)
  color1        (the color of the saber: 0-red 1-orange 2-yellow 3-green 4-blue 5-purple.)
  personality   /botfiles/(whatever you called the file).jkb
 }
```

Extended Bot Options (for Jedi Mod)

If you want your bot to have the Jedi Mod options you should write this
instead:

``` 
 {
  name             "The name you want to call it, keep the quotes"
  model            (write the name of the model)
  color1           (the color of the saber: 0-red 1-orange 2-yellow 3-green 4-blue 5-purple.)
  tck_saberred     000-255 (the red value)  
  tck_saberblue    000-255 (the blue value)
  tck_saberred2    000-255 (the red value of the second saber)
  tck_sabergreen   000-255 (the green value)
  tck_sabergreen2  000-255 (the green value of the second saber)
  tck_saberblue2   000-255 (the blue value of the second saber)
  tck_doublesaber  0-3 (0-one saber, 1-two bladed lightsaber, 2-two lightsabers, 
                        3-two double lightsabers.)
  hilt "hiltname"  (the hilt that will be on his right hand, for example hilt "yoda")
  hilt2 "hiltname" (the hilt that will be on his left hand, for example hilt "desann")
  personality      /botfiles/(the name you called the .jkb).jkb
 }
```

Final Steps

Create a folder called scripts and put the .bot file in there. Now
create a new zip file, put your models folder, botfiles folder, and
scripts folder into it, and rename the .zip extension to .pk3.

Put the .pk3 in your gamedata/base folder, then start the game and put
the choose the bot (look for whatever you called it)

Congratulations\! You built a bot\!

Troubleshooting

**The Bot don't looks like the skin I made.**  
First make sure your skin is not in models/players/(something that
already exists like reborn or chiss). If it is you need to change the
folder name and in the .skin and in the .bot files. If not, it's
probably because you called the .skin file model\_default\_(something).
You need to call it model\_default. The same applies for model\_red and
blue.

**Something is wrong with the personality.**  
Check every line in the personality (.jkb) file. Start from the basic
options if and retrace your steps.

If you have any other troubles e-mail me at: <GraalYo@hotmail.com>
