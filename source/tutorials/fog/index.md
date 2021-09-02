---
title: Making Fog
author: fourwood and EvanC
email: fourwood@ix.netcom.com,ev@wave.co.nz
description: >
    Learn how to make fog.
date: 1998-11-20
original: fog.htm
category: jk
---

by fourwood and EvanC

**NOTE: This is still in a fairly primitive stage.**

For those of you who have read the message boards fairly recently,
you might know that I figured out a way to do fog in Jedi Knight. Well,
one day I was talking to Evan on ICQ and he told me of this great idea
that would greatly improve the fog. When I re-wrote the fog cog, (whoo\!
rhyming words\!) I decided it was time to write this tutorial. To
understand this tutorial, all you need to do is be able to place a cog
and fill in the fields, and place a ghost thing. There won't be any
pictures for following this tutorial, for there isn't much to show. 
There is a screenshot, however.

To start out, you need the [cog](fog2.cog).  Place this in your
project directory under the /cog directory.  Now in your level, place a
ghost thing where you want the thickest, central part of the fog to be
located.  The height *does* matter here, so if you want the fog to be
about head high, put the ghost thing about head high.

Now, go to the placed cogs window and add fog2.cog to your level. 
The fields:

  - ghost(thing): the ghost thing you just placed.
  - r(int): value for red.
  - g(int): value for green.
  - b(int): value for blue.

Yes, you could make colored fog if you wanted to, but for now, we
are going to stick with grey.  For r, g, and b, a number from about 100
to 200 is generally a good fog level.  100 is fairly light, while 200 is
getting rather thick.

Now, save your level, do save jkl and test, or gob it, which ever
you want to do, and play.  If you are a ways away from the ghost, there
will be no fog.  If you get closer, there will be a light fog, the
closer you get, the darker the fog gets.

![fog2.gif (92457 bytes)](fog2.gif)
