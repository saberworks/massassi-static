---
title: Character Model Import Tutorial - 2
---

Author: Michael Frost

## Extracting Assets0.pk3

A quick explanation of PK3 files, for those of you not familiar: A PK3
file is simply a .ZIP file, renamed to .PK3. Quake uses this format, and
so does JK2. In order to access a .PK3, you first have to rename it to
.ZIP, then extract its contents to another folder, like any ZIP file. I
choose to extract this file to a folder, **C:\\Assets0\\** on my hard
drive. I recommend doing this, but you will need to have *at least 600
MB free* on your hard disk to do so.

After extracting, I also go back and rename Assets0.ZIP to Assets0.PK3.
I recommend doing this, but you will need to have at least 600 MB free
on your hard disk to do so.

**What is Assets0?**

This file here contains the existing model files, textures, and such,
for the characters and some levels of the game, as well as code, etc. It
also contains the file \_humanoid.gla, which we will need to set up the
animations within assimilate\!

Go to C:\\Assets0\\ to find the extracted file \_Humanoid.gla

Look for this 9 MB file in

\\models\\players\\\_humanoid\\

This folder contains the file \_humanoid.GLA.

Copy or Move this file from this directory to
C:\\base\\models\\players\\\_humanoid\\

That's all you need that file for now. Your humanoid file is now ready
for use in future.

* Back: [Setting up for Editing](../1_SettingUp/)
* [Return to this Tutorial's Table of Contents](../)
* Next: [Model Setup](../3_TheModel/)
