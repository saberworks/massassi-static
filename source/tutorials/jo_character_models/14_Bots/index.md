---
title: Character Model Import Tutorial - 14
---

Author: Michael Frost

## Making Your Model Into a Bot

Bot files allow your model to be used as an AI bot for multiplayer.
Personally, I chose to copy an existing file and rename key text parts
of it to my liking. You can find scripts within the directory /scripts/
within the assets0.pk3 file, named kyle.bot or tavion.bot, etc.

The file can be opened with Notepad, and should look something like
this:

```
    {  
    name "DarthVader"  
    model darthvader  
    color1 0  
    personality /botfiles/darthvader.jk  
    }
```

**Explanation**

|  |               |                                                                              |
|  | ------------: | ---------------------------------------------------------------------------- |
|  |        name - | name shown within the game, this will be the model's name in the player list |
|  |       model - | the model that the bot uses                                                  |
|  |      color1 - | the color used for the model's lightsaber on the bot                         |
|  | personality - | points towards the bot's behaviour scripts                                   |

Save this file as a .Bot file, put it into a Scripts directory, then
pack the scripts directory straight into the zipped custom file\!

## Bot File Behavior Scripts (.JKB Files)

Personally, I chose to copy an existing file and rename key text parts
of it to my liking. You can find bot behaviour scripts within the
directory /botfiles/ within the assets0.pk3 file.

Here, you can adjust the bots capabilities, what Force powers it has,
what powers it uses most, how accurate it is, etc, as well as what it
says in the text taunts and comments upon joining, dying, etc. It's
pretty straightforward; I suggest taking a look at a few JKB files
within the assets0.pk3 file.

Put the file in a folder "Botfiles" and place Botfiles into the zipped
model file.

* Back: [Creating a Custom Sound Pack](../13_Sounds/)
* [Return to this Tutorial's Table of Contents](../)
* Next: [Handling Shaders for JK2](../15_Shaders/)
