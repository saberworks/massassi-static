---
title: 
author: 
email: 
description: >

date: 
original: llb.html
category: 
---

Author:|                                                                                     |                                                                                                                                 |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [![Recon Gamer](http://www.massassi.net/images/rg.gif)](http://www.recongamer.com/) | [![](http://adservice.recon-networks.com/adserve.asp?F=1&Z=6&N=2)](http://adservice.recon-networks.com/adclick.asp?F=1&Z=6&N=2) |

  
Layered Lightbeams  

-----

Author: [halucid](mailto:halucid@verizon.net) Reprinted with Permission
by: [jEDIkIRBY](mailto:jEDIkIRBY007@hotmail.com)  
  

*I was attempting to make my own level using pretty lightbeams like the
one showcased in halucid's MadaMemorial level, so when I e-mailed him
and asked him to give me a few pointers, he gladly replied with a full
blown tutorial. I asked him if he'd mind me posting it on massassi, and
he was happy to. So here's halucid's Layered Lightbeams Tutorial in
full:*

![](1.jpg)

Yes layered... there's actually two light beams there. An outer and an
inner beam. The technique is very similar to the one used to create a
glowing saber, as they both take advantage of hardware antialiasing to
acheive the effect.

Now first, create the beams. You can choose to either make them 3DOs, or
part of the level architecture. To keep the ammount of visible adjoins
to a minimum, I recommend using 3DOs (Just don't forget to set the thing
flags to render as architecture...0x8) However, since my beams required
sector thrust, I made them out of architecture.

![](2.jpg)

Now the effect cannot be acheived without custom textures. I used 8x8
8-bit MATs, as they don't need to be any larger than that. These
textures MUST have transparent sections.

![](3.jpg)

Now pay attention to the phrasing here... pretty tricky. Place the
"INNER MAT" around the OUTER surfaces of the INNER beam. Then place the
"OUTER MAT" on the INSIDE contours of the OUTER beam (if you're making a
3DO beam, you must first invert the surfaces in order to do this ALT+I).

![](4.jpg)

OK, now the fade effect won't be created unless you set the UV scales so
that the textures are stretched.... a lot. All settings vary depending
on the size and layout of your level, so you'll have to experiment a few
time to acheive the desired effect. Don't forget to add surface lighting
and the translucent flag\!

![](5.jpg)

You're done\! Your level should now look axactly like this\! Hehe, just
kidding. Actually, depending on how you decide to design the tubes and
how you create your textures, your beam will be truly unique. It's
unlikely yours will look like this one at all... but there's only one
way to find out.

Now for an added effect, you can use surface scrolling to make the rays
apear to move. Try conveyor.cog, specially designed just for this effect
by LKOH\_SniperWolf.

Good luck, and I hope this answers any questions you might have.

Attached: [Conveyor.cog](conveyor.cog)  
  

Copyright © 1998-2005 Respective Authors & [The Massassi
Temple](http://www.massassi.net)
