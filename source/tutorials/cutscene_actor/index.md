---
title: Making an Actor for a Cutscene from a Skin
author: Violata
email: dshahoud@dircon.co.uk
description: >
    Straightforward method to make an actor for a cutscene out of a skin in MotS.
date: 2000-01-12
original: tutorial.html
category: jk
---

Author: Violata

**Sometimes, you're just doing nothing, and not thinking much, and then
suddenly an idea clicks. That's what happened to me, I had been racking
my brain to try and make an actor for a cutscene out of a skin. No one
would help. And then, it clicked.**

What you will need:

  - The skin you want to use
  - ConMan
  - 3do Viewer (Not compulsory)
  - A text editor (Notepad will do fine)

**Here's how to do It. it's really simple:**

1.  Get your skin, I suggest using one that looks like it uses the Kyle
    model. it's easier. If it uses another model, it may be a bit hard.
    I am using a Thrawn skin.

2.  Open ConMan and open **jkmres.goo/gob**, usually located at
    **C:/program files/Lucasarts/Mots/Resource/Jkmres.gob/goo**

3.  Find the **kk.3do** or **ky.3do** and extract it to your level
    directory.

4.  Rename the 3do to whatever you want it to be called. (In my case -
    thrawn\_actor)

5.  Now open it and change all the mats it uses to that of your skins'.
    I presume you know how to match up mats. For example: You would
    replace **kydneck.mat** to (in my case) **athneck.mat**.

6.  Now you have a 3do from your skin. I bet you're thinking, what was
    that all about? I could have just used the 3do that came with the
    skin. But you can't, that doesn't have AI. Or maybe you can, but
    it'll be hard. This is the easy way.
    
    Now, we're nearly done. Copy the bit below into your **mots.tpl**
    file in the level directory. Then paste it at the bottom of the file
    And change the bits that are in red to yours. This will provide you
    with AI and animations for the actor. And it will place him at the
    bottom of the 3do list when you're in JED.
    
    `# DESC: An actor for cutscenes`  
    `# BBOX: -.036449 -.016107 -.120075 .037661 .02734 .064161`  
    `thrawn_actor _humanactor model3d=thrawn_actor.3do puppet=mj_cuts.pup soundclass=ky.snd maxvel=.4 health=20000 maxhealth=20000 maxthrust=1 maxrotthrust=60 aiclass=jan.ai`

    *Do not copy this line or below it.*
    
    The `DESC:` value is the description that will appear in the
    preview window of JED's 3do browser. You don't really need to change
    it; it doesn't really make a difference. The first value on the third line (`thrawn_actor`) is the
    name as it will appear in the 3do list of JED. The `model3d=` value is the name
    of the 3do that you renamed earlier. Write the exact one in there.
    Try to use underscores in the 3do name, if you haven't just go and
    rename it again.

That's it. Your actor will now move as you want it to in your cutscenes.
In a level, it will run around aimlessly just like if you put the
**jan\_actor.3do** in JK or **Mara\_actor.3do** in MotS. You can't kill
him in a level. It took me this long to work out, if I'd had worked it
out earlier, maybe it would have been more use to me. But I don't do
much editing now, so it should be useful to you.

**Extra useful notes:**

It's possible to do some neat things by just modifying 3do files and
.tpl outtakes. Here's an easy way to make a boss from a normal enemy, as
a bonus for you:

1.  Extract a 3do of an enemy, using Conman, to your level's 3do
    directory.

2.  Rename the 3do

3.  Open the .tpl and copy the part with your enemy's info. E.g. if your
    boss is a very strong Ree-Yees or probe droid, copy the bit with
    them and paste it at the bottom of the file. Then change the red
    bits.
    
    `# DESC: boss enemy`  
    `# BBOX: -.037893 -.021815 -.12043 .03746 .022321 .066407`  
    `icommando _humanactor thingflags=0x20000400 model3d=ic.3do size=.06595 movesize=.06595 puppet=ic.pup soundclass=ic.snd cog=actor_ic.cog maxvel=.3 weapon=+elaser weapon2=+st_punch health=90 maxhealth=90 maxthrust=1.1 maxrotthrust=90 typeflags=0x20001 fireoffset=(.014/.059/.031) aiclass=icdefault.ai`

4.  Change the `health=` and `maxhealth=` values to a high number, and the boss is done. This
    .tpl outtake above is from the imperial commando. He won't die as
    easy, and you'll keep this one as a special boss. It won't affect
    the other imperial commandos, they will be normal. All you need is
    some dark lighting and shadows, a large room, not too many powerups
    and an intimidating background sound, and he'll be a powerful enemy
    to round up a good level.

See how easy things are? This is probably one of the tutorials that
everyone will rush to do as soon as they read it. If you want to
customise the boss, then just edit it's Mats, (see the [Making a Skin
Tutorial](/tutorials/skins/)) and tell
the 3do to use them instead. So you can have a powerful commando, with a
scarred up face, and a brilliant boss. Cool eh?

Any problems? Contact Violata
