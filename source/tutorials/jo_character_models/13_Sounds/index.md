---
title: Character Model Import Tutorial - 13
---

Author: Michael Frost

## Creating a Custom Sound Pack

To have custom sounds, you must make a file named **sounds.cfg**, a
simple text file, and have it point to where you will have your custom
sounds folder. If you will not be using custom sounds, simply copy a
sounds.cfg file from the appropriate models/players/model folder within
the assets0.pk3 file and place it in your custom model folder.

In the sounds.cfg folder, it will say something like this:

```
    chars/darthvader/misc  
    m
```

This points towards the directory, within the zip file,
"sound/chars/darthvader/misc", and the "M" below it points out male, I
believe, but I may just be guessing here. So, if you have custom sounds,
pack them up like this;

Take the custom WAV or MP3 files, and put them in a folder called "Misc"

**WAV or MP3 Sound Naming**

> Choke1  
> Choke2  
> Choke3  
> Death1  
> Death2  
> Death3  
> Death4  
> Falling1  
> Gasp  
> Jump1  
> Land1  
> Pain25  
> Pain50  
> Pain75  
> Pain100  
> Pushed1  
> Pushed2  
> Pushed3  
> Taunt  

**Tip:** Mods are available that support multiple taunts. To take
advantage of this, name taunts successively: "Taunt1", "Taunt2", etc.

Place the **misc** folder within a **ModelName** folder (such as
DarthDarth like in the page's example). Make a folder **chars** and put
**ModelName** within **chars**.

Make a folder "sound", then place "chars" within "sound"

Place "sound" folder within the modelname.ZIP file, beside the Models
folder.

Rename ModelName.zip to ModelName.pk3

* Back: [Testing In-Game](../12_TestingInGame/)
* [Return to this Tutorial's Table of Contents](../)
* Next: [Making Your Model Into a Bot](../14_Bots/)
