---
title: Character Model Import Tutorial - 10
---

Author: Michael Frost

## Creating .SKIN Files for Textures

A skin file is a text file -- here is an example of several lines

```
    hips,models/players/darthvader/hips.tga  
    hips_legs,models/players/darthvader/legs.tga  
    hips_innercloak,models/players/darthvader/armor.tga  
    r_leg,models/players/darthvader/legs.tga  
    l_leg,models/players/darthvader/legs.tga
```

The setup for this is like so --

```
    ModelPartName,models/players/modelname/Texturefile.tga or jpg

    helmet,models/players/darthvader/helmet.tga
```

Do this for each model piece.

I suggest when you make the skin file, have 3D Studio Max open with your
model onscreen so you can figure out exactly what parts you have named
or not (if you have named something incorrectly -- e.g., caps, and such
-- you should rename them, re-export, then re-assimilate back to this
point). At the end of the line make sure you list the appropriate
texture file for the part. See the section on proper naming procedures
if necessary.

Do this for each model part, including the caps. Just use the
models/players/stormtrooper/caps.tga file for the caps but it is
possible to use custom caps files; look at Cheshire\_vader.pk3 file for
an example on that.

When you are done creating this text file, save it as "All File Names",
and Save As... Model\_default.skin.

You now have a skin file that will point to all your proper textures\!

You can make multiple skin files, naming them like so:

```
    Model_red.skin  
    Model_blue.skin
```

Hhaving them setup the same way as the normal skin file, just with
different texture names, will allow you to have multiple texture sets on
a single model.

For example, in model\_default.skin:  

```
    Head, models/players/modelname/SamsFace.tga
```

And in Model\_red.skin:  

```
    Head, models/players/modelname/BobsFace.tga
```

On the default model, SamsFace texture appears, and on the Red model,
BobsFace will.

Or you can name it whatever you like and have the person choose the
model by typing in the console of JK2:

```
    Model modelname/model_skinname.skin
```

This allows custom skins to go onto a model and not replace the existing
default or team colors.

* Back: [Using Modview to Test the GLM](../9_Modview/)
* [Return to this Tutorial's Table of Contents](../)
* Next: [Creating .SURF Files to Hide Things](../11_SurfFiles/)
