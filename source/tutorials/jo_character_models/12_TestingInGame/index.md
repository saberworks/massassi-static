---
title: Character Model Import Tutorial - 12
---

Author: Michael Frost

## In-Game Testing

To pack a model up for in-game consumption, you should create a .ZIP
file, named whatever you like. Within this zip file, you should place
the following folder setup...

> Models/Players/ModelName/

... where ModelName should be your model's name\! (.e.g., DarthDarth)

What I usually do in Windows is right-click within a computer folder,
such as c:\\base\\, and create a new folder, and name it **models**. I
create another folder and name it **players**.

I then take my custom model folder (which contains the textures,
model.glm, .skin file, .surf files, and the sounds.cfg file, if you have
one), put it inside the **players** folder, put the **players** folder
into **models** folder, then lastly zip the **models** folder.

You should now have a .ZIP file containing your completed model\! One
last step: rename the ModelName.zip file to **ModelName.PK3**. And boom,
its all packed up.

Move this PK3 file now into...

> C:\\Program Files\\LucasArts\\Star Wars JK II Jedi
> Outcast\\Gamedata\\Base\\

...which should also contain the assets0.pk3 file.

Fire up Jedi Knight 2, and see if your model's picture shows up in the
select menus\! If it doesn't show up, you may have any one of a number
of errors. For starters, check the console when you load up the game to
see if it gives any errors (the tilde \~ key).

**Common Troubleshooting Tips:**

  - Go back to your model setup and check the setup of the folders in
    the .ZIP
  - Check the naming of the GLM files, the .SKIN files, things like that
  - If the sounds don't work, check and see in the console ingame for
    the specific files

It all comes down to having done something wrong in the process that the
game doesn't like\!

* Back: [Creating .SURF Files to Hide Things](../11_SurfFiles/)
* [Return to this Tutorial's Table of Contents](../)
* Next: [Creating a Custom Sound Pack](../13_Sounds/)
