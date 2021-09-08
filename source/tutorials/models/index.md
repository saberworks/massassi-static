---
title: Adding Multiplayer Models
author: Dylan
email: dylan_555@hotmail.com
description: >
    Adding Multiplayer Models.
date: 1998-11-16
original: original.html
category: jk
---

Author: Dylan  

First off, download ConMan (Container Manager). You can get this in the
[programs section](/programs/).

After running ConMan, find the Res2.gob file (probably on the CD, it may
be in your Jedi Knight\\Resource folder). Open the file. After you have
done that, follow these directions:

![](modelsaber1.gif)

1\.  Select the "**misc**" GOB directory.  
2\.  Select the files "**models.dat**" and "**sabers.dat**" using the
    **\[CTRL\]** key to multiselect.  
    **NOTE:** <span class="underline">models.dat</span> is the only file
    required to add multiplayer models, but you should also extract
    <span class="underline">sabers.dat</span> while you're at it since
    you'll need it if you want to add new sabers.

  

3\.  Go to the **File Menu** and click on **Extract files...**.

![](modelsaber2.gif)

  

![](modelsaber3.gif)

4\.  Go to the **Jedi Knight** directory.  
5\.  Go to the **Resource** directory.  

  

![](modelsaber4.gif)

6\.  Click the **Create New Folder** button.  
7\.  Name the new directory "**misc**". Click "**Open**".  

  

8\.  Open your **Jedi Knight\\Resource\\misc** directory through Windows
    Explorer and double-click the **models.dat** file. When prompted,
    open the file with **Notepad** (or another text editor).  

![](modelsaber5.gif)

  

![](modelsaber6.gif)

9\.  Go to the end of the file. Add the next number in the sequence
    followed by a colon, then hit **\[TAB\]**.  
10\. Add the 3DO file name, then hit **\[TAB\]**.  
11\. Add the SND file name. Sometimes a SND file will be suggested or
    included in the GOB.  
    **ky.snd** (Kyle's sounds) can be used as a generic male sounds
    file. **kyfemale.snd** can be used as a generic female sounds file.

  

![](modelsaber7.gif)

12\. Go to the top of the file. Add *ONE (1)* to **numModels** for each
    model added to **models.dat**.

After that, you're ready to run JK and use your new models.
