---
title: Character Model Import Tutorial - 11
---

Author: Michael Frost

## Creating .SURF Files to Hide Things

A .SURF file is just a text file meant to disable specific model parts
of a character model. You can say, disable Darth Vader's cape, or
perhaps on the cheshire\_vader model, make it so that his helmet can
disappear. On Exar Kun, I made it a part of the Red and Blue skins for
the model, where on his blue he had no armor nor cape, yet the red and
default had the cape and armor on still. You can play around with other
stuff in game for jan, kyle and others to mess around with their models.

A typical .SURF file contains a line or two of text that looks like
this:

```
    surfoff "torso_r_pauldron torso_l_pauldron
    torso_r_pauldron_medal torso_cape torso_l_pauldron_bones"
```

Saved in Notepad as model\_default.surf, it makes the model pieces
torso\_r\_pauldron and such disappear.

It will be named to the appropriate skin file so that if, for example,
it is affecting the default, model\_default.surf -- surfacing the blue
model, model\_blue.surf

You can have one .SURF file per .SKIN file, named the same as the
corresponding .SKIN file with just the different extension of .SURF

* Back: [Creating .SKIN Files for Textures](../10_SKINfiles/)
* [Return to this Tutorial's Table of Contents](../)
* Next: [Testing In-Game](../12_TestingInGame/)
