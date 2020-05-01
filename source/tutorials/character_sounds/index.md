---
title: New Sounds for Jedi Knight
author: EvanC
email: ev@wave.co.nz
description: >
    Learn how to make new character sounds.
date: 1998-07-28
category: jk
---

Author: EvanC
  
In this tutorial we will change the sound of a stormtrooper. You will
need a gob/ungob program (like
[ConMan](http://www.massassi.net/programs/) from the Code
Alliance and a sound recording program
(not the Windows Sound Recorder--it doesn't work).

Open your gob program and open the file **res2.gob**. Go to the
directory misc\\snd and then export the file st.snd into your project
directory. Now you can create your sound. It is a standard windows .wav
file recorded at 11KHz mono. Don't use Windows Sound Recorder because JK
doesn't work right with sounds recorded by it. I suggest you get a
freeware program from somewhere like <http://shareware.com>. Once that's
done you can open up **st.snd** with Notepad.  
  
Here is the structure of the SND file:

```
help        I00S114Z.WAV        0x10000     # Call for reinforcements.
```

The first word, "help" is the situation when the sound is played. In
this case it would be when the AI is in trouble.

The second word "I00S114Z.WAV" is the sound file that will be played.

Thirdly there are the sound flags, "0x10000".

Often after those words is a description of the sound file. This makes
it easy to modify. On this line it is "Call for reinforcements". Because
of the file descriptions it should be easy to figure out what each of
your sounds needs to be like.

Once you have made your sounds go through and change the file names on
each line into your file names.

Put the snd file and all the wavs into your project directory and then
gob it up and run the level. All the custom wavs also need to go in too.
When you run the level the stormtroopers will now use your sounds.

If you want to modify the players SND file it is called **ky.snd**
