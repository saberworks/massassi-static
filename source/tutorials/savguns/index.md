---
title: Creating New Weapons
author: SavageX
email: savagex@sprynet.com
description: >
    This tutorial helps you make an external, internal, and a powerup of a gun.
date: 1999-06-13
original: original.html
category: jk
---

Author: SavageX  
  
*Note: This is an htmlized version - if you would like, feel free to
download the [original Microsoft Word version](savguns.zip).*  
  
Tools needed:

  - JED v.93
  - Puppet JED
  - Wordpad (or any other text editor)
  - [temp.3do](temp.3do) (that 3do that comes with this tutorial)

Step 1: making a fist/hand shape for JED  
Step 2: making a weapon powerup  
Step 3: making an external mesh  
Step 4: making a internal mesh  
  

-----

Note: Do NOT skip a step for each step is need to complete the gun
making process.

-----

  
**Step 1: making a fist/hand shape for JED**

> To first start out, first, open JED. Go to your Map settings (F4), go
> to "Grid" settings, and set your "Snap every" to 0.00125. Then go to
> "Other" and Set your "3D preview step" to 0.05.  
>   
> Now go to import and import the fistg.3do from the Jedi Knight's (or
> MotS) res2.gob (or res2.goo for MotS). Once you've done that, export
> the 3do as a new shape in JED's shape section. Name it as fist (or
> hand) so you know what shape it is.  
>   
> The Reason why you making a hand shape is because you'll need it for
> Step 3.

**Step 2: making a weapon powerup**

> Make sure you just completed step 1 before doing this step.  
>   
> Now onto making you gun\! To start, start a new project in JED. When
> you have it all set, select the walkplayer (thing). Now depending on
> what weapon you wanna make, turn the walkplayer (thing) into a
> existing weapon powerup (I.E. if you are making a pistol, use
> "bryarpistol". If you are making a stormtrooper size weapon, use
> "strifle".) This should help you scale your gun properly. Now, zoom in
> on the power up (thing). Make sure the powerup is yaw, pitch, and roll
> are set at 0 before preceeding. Now build you weapon around the
> powerup BUT do not go into 3D preview yet. Don't forget to set the
> flags of you weapon (the sectors) as 80000000 (or select the "preview
> as 3do"). Once you have the basic shape right, multiselect the weapon
> (the sectors) and change the layer to "K\_RHAND". Go into map settings
> and hide the layer0 so that the powerup (thing) will disappear.  
>   
> Now go into 3D preview. As you see, your new weapon is covered in
> "dflt.mat" texture. All you have to do now is texture it. Once you put
> on the textures (make sure you don't use more than 9 textures so you
> can do step 4), selsect the sector on the gun (if it has more than one
> sector) to where you want the center to be (where x, y, and z meet)
> and then export you thing as "namep.3do" (where it says name, put your
> weapon's name in there. Don't forget the "p" after the name since your
> making a powerup of the gun).  
>   
> Don't close JED just yet because it is time for step 3 ...

**Step 3: making an external mesh**

> Make sure you just completed step 1 and step 2 before doing this
> step.  
>   
> Now that you have made the powerup, it is time to make the external
> mesh. Multiselect your weapon (the sectors) and then open your tools
> box (F9). Rotate you weapon 90 degrees on the X axis. This should have
> you gun facing downward. Now, go to the Map settings (F4), go to
> "Shapes", and select you fist shape you made in Step 1. Now use the
> "K" command and make a tiny little box with you mouse that is smaller
> than 0.2. Since JED can't make a shape smaller the 0.2, the shape of
> the fist will be the size you export it from. Now, multiselect the
> faces on the hand (Cool trick: select the sector (the hand) and press
> the spacebar to multi select it. Then press "F" to switch to surface
> mode and all the faces of the sector will be selected\! Cool huh?) Set
> the surface's U and V scale to 4. This will make the textures fit the
> hand. If you notice, the "kyhandf.mat" texture on the hand is off. Go
> to that surfaces info (press enter key), go to the "SURF FLAGS" and
> click the "texture flip" box. This will make the hand flip into the
> correct postion. Now, move you fist to where you want it on the the
> gun (must likely the guns handle) and then multiselect all the
> sectors. Select the hand (so that the center will be at the hand) and
> then export it as "nameg.3do" (don't forget the "g" since this gun is
> a external mesh.)  
>   
> Now that the external is completed, lets make the internal mesh\!  
>   
> Don't close JED just yet because it is time for step 3 ...

**Step 4: making a internal mesh**

> Make sure you just completed step 1, step 2, and step 3 before doing
> this step.  
>   
> Now this step is gonna get a little hard because you going to use
> wordpad to make this 3do, Don't worry, you not going to make a whole
> 3do with wordpad, just a little cut and pasting. Make sure you have
> the temp.3do that I included in the tutorial before preceeding.  
>   
> Now, delete the hand mesh (the sector) from you weapon. Multiselect
> the weapon (the sectors) and change the layer to "K\_WEAPON". Now
> export the gun as "name.3do" (There is no letter after the name
> because your gonna to delete this file after the step).  
>   
> Now exit JED and fire up Wordpad. Open the temp.3do. Now open the 3do
> you just exported in a seperate wordpad. Copy the textures that you
> have used in the weapon 3do and paste them over the ones is the
> temp.3do BUT don't paste them over the textures under 9-15 -- you need
> those for your hand meshes. Once you have done that, go down to the
> temp.3do's "K\_WEAPON" mesh (hint: use the find command to find this).
> Now switch back to the 3do you made and find it's "K\_WEAPON" mesh.
> Now simple copy all the the mesh's info and then paste them over the
> temp's "K\_WEAPON" mesh. Now save your file as "namev.3do" (the v is
> for point of view which is the internal mesh). Don't close you new
> file yet.  
>   
> Now open Puppet JED. Open you new 3do. Is it aligned right? Are the
> textures properly on it? If you gun is off a bit, go back into you 3do
> (namev.3do) and go to the bottem where it says "SECTION: HIERARCHYDEF"
> and find "K\_WEAPON". now just enter in the right numbers into the x,
> y, and z to move it. Reload it into Puppet JED to see if you numbers
> made it move right. if it didn't, just do it again until you've got it
> in place. Now go ahead and load key files into Puppet JED and see if
> the 3do move correctly with the keys  
>   
> Yahhoo\!\! You did it\! You made your new gun\! That wasn't to hard
> was it?

