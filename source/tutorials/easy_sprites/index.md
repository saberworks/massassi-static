---
title: Easy Sprites
author: Dustino
email: dustino@hyperaction.net
description: >
    An easy way to add sprites to a level implementing the easysprites.cog.
date: 2000-07-15
original: original.html
category: jk
---
-----

Author: Dustino

###Before You Get Started:###
Be sure to download the [easy\_sprites.zip](easy_sprites.zip) file that
contains everything you need.

###Description of Each File in easy\_sprite.zip:###
1.  **tutorial.txt**: This is the file you're reading right now.
2.  **easy\_sprite.cog**: This COG displays up to 10 sprites at ghost
    positions and has the option to animate the sprite.
3.  **fire\_ani.mat**: This multi-celled fire MAT goes along with the
    tutorial.
4.  **burn.spr**: This is a fire SPRITE. (Uses the **fire\_ani.mat**
    supplied)

###Other Files Needed:###
> **master.tpl** (for JK Project) -or- **mots.tpl** (for MOTS Project)

- The master.tpl and mots.tpl can be found in the jed/jeddata folder
- Copy the filed needed into your project directory

-----

If you want to make your own SPRITE here is what the fire sprite used in
this tutorial looks like:

```
#material     type  width  height  geo  light  tex  extralight  xoff  yoff  zoff
fire_ani.mat  0     0.12   0.12    4    0      0    0.0         0.0   0.0   0.0
```

-----

Now you have all of the files in their correct spots in the project
directory you can now begin the addition of sprites into your level.

Steps for Adding Sprites:

1.  Open up JED and start a new JK/MOTS level.

2.  Save the .jed file in your project directory.

3.  Minimize JED and open your project directory.

4.  Open master.tpl or mots.tpl (depending on which you copied to the
folder).

5.  At the very bottom (always add to the bottom of templates) of the
template add the following lines:  
`# DESC:`  
`# BBOX: 0 0 0 0 0 0`  
`+fire_sprite none orient=(0.000000/0.000000/0.000000) type=cog move=physics`  
`thingflags=0x10000000 sprite=burn.spr mass=0.050000 physflags=0x200`  
`vel=(0.000000/0.000000/0.000000)`

6.  Save the template and close it.

7.  Now maximize JED.

8.  Now goto Commands and click RELOAD TEMPLATES. (Always hit reload
templates when you have edited the template manually)

9.  Now goto THING and insert a GHOST. (Remember the thing \# of this
ghost)

10. Now goto Tools and click PLACED COGS

11. Click ADD COG

12. In the Resource Picker click cog/

13. Select **easy\_sprite.cog**

14. Click OK

15. Setup the COG  
>**Description of each Option:**
>> **SPRITEx** (thing): These are where the thing \# of your ghosts
>> go. Since you only have added 1 ghost so far place its thing \# in
>> the sprite0 (thing) box.  
>>   
>> **SPR** (template): This is where you select the SPRITE you will
>> be using. double click the empty box to open the resource picker.
>> At the end of the list should be +fire\_sprite. Select it and hit
>> OK.  
>>   
>> ***NOTE:** The two options below are for animating the sprite (if
>> the mat used in the sprite is multi-celled). For this tutorial
>> they will be used.*  
>>   
>> **MATANIM** (material): Here you select the MAT you wish to
>> animate. Double-click the box. In the resource picker select mat/.
>> Select the **fire\_ani.mat**.  
>>   
>> **FPS** (flex): This option lets you select how fast the mat gets
>> animated.  

16. Click REFRESH and then OK.

17. Now Save the .jed, setup the level in the Episode Editor, and save
the .jkl and .gob.

18. Run the level.

19. Enjoy
