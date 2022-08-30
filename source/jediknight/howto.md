---
title: How To Install Jedi Knight Levels and Mods
author: Jipe, Tallgeese, Brian
email: nrl1@anet-chi.com, rob_jacoby@hotmail.com
---
Authors: Jipe, Tallgeese, and Brian

So, you've just downloaded a level or mod, and you want to
load it up right away, but you have no idea what to do? Never fear,
Massassi is here\! Well, now that we've got the annoying cliches out of
the way, let's get down to business: describing in-depth how to install
user-made levels, skins, weapons, patches, and whatever else you can
think of.

*2022 Update:* Please give Max Manager a try! This program is available in
the [/programs/](/programs/) section.  It's a modern mod launcher/manager that
works on Windows 10+.

Older instructions follow...

Most files you download from the Levels/Mods section of Massassi will be
ZIP files, with a .zip extension. They can be opened easily with
[WinZip](http://www.winzip.com/), which is shareware - you can try it
out for free, then if you like it, pay $20 to the makers. After
installing WinZip, double-click on your \*.zip file and it should open.
Following are detailed instructions for each of the types of files
available here at Massassi.

## Levels

  - The zip will contain a minimum of two files: a .gob (JK) or .goo
    (MotS), and a readme.txt. If you're sure that it is just a level,
    and does not modify any other part of JK, continue on; otherwise,
    skip down to the "Mods" section.
  - Click on the gob/goo file and hit the "Extract" button. A little
    window should come up, asking where the file should be extracted.
  - Browse to the Episode directory in your JK or MotS folder. The default
    installation path (for the CD version, it may be different if you got your
    copy from Steam or Gog) is `C:\Program Files\LucasArts\Jedi Knight\Episode`
    for JK, and `C:\Program Files\LucasArts\MotS\Episode` for MotS (where C is
    your hard drive).
  - Hit the extract button, and close WinZip when it's finished (it may
    take a few seconds for large levels).
  - Start up JK/MotS, and your newly downloaded level should show up on
    the Singleplayer/Multiplayer selection screen, depending on which
    type of level it is. Remember that there is a limit of around 25
    levels that can be "installed" at any one time. However, you can get
    around this by running them with Patch Commander.

## Mods/Patches:

There are several different ways of running mods for JK/MotS. The most popular
used to be Patch Commander. You could previously download it for free from
http://www.jediknight.net/commander/, but the site is now defunct.  You may be
able to get it from another source, although Massassi doesn't currently have a
copy and it may not work on newer versions of Windows. Once you've downloaded
andinstalled it, read on:

- Open Patch Commander and drag the gob file from WinZip into the
  patch organizer window.
- To activate a patch, double-click on it. All conflicting patches
  will automatically be deactivated and their symbol will change to a
  big "NO". You can still activate them, however, all of their
  conflicting patches will be deactivated in turn.
- To run the game with the patches you have selected, hit the Launch
  button (located in the Toolbar) or the F9 key.

Another way to run patches is via the command line:

- Extract all files to a folder located in your main Jedi Knight/MotS
  directory, named anything you want - let's call it "blah" for
  simplicity's sake. (So your files should be in `C:\Program
  Files\LucasArts\Jedi Knight\Blah`, if you're following along.
- Then go to Start -\> Run... and type in
  `C:\Progra~1\LucasA~1\JediKn~1\jk.exe -path blah`, assuming C
  is your hard drive, you installed JK in the default directory, and
  your folder is named blah. For MotS, it would be
  `C:\Progra~1\LucasA~1\MotS\mots.exe -path blah`, assuming the
  same things as before.
    - Note: the weird tilde `~` in the path is how older versions of the Windows
      command line dealt with spaces in file names.  If you are using a newer
      version of Windows, it's likely you'll need to use the full path, with
      spaces.
- Note that you will need a new folder for **each** patch you install, you
  cannot keep extracting things into one folder for each mod/patch you install
  this way.

A final way to run JK/MotS mods is with a .bat file. Follow the instructions
from the command line method above, but extract all but the .bat file to your
folder. Then extract the batch file to your main JK/MotS directory, and double
click on it to play. You can make your own .bat files, but it's generally easier
just to type a line in at the command prompt, or use Patch Commander, if the
author didn't include one in the download.

## Skins:

If the skins are in a .gob/.goo file, then you can follow the
instructions above for installing mods. If all you have in the zip file
is a bunch of mats and a 3do or two, then read the paragraph above on
running patches with the command line. The 3dos should be in
`blah\3do`, the mats should be in `blah\3do\mats`, and if there is a
models.dat, it should be in `blah\misc`; this is assuming your `blah`
directory is either in `C:\Program Files\LucasArts\Jedi Knight\blah`
or `C:\Program Files\LucasArts\MotS\blah`. Once again, you will need
a new folder for each new set of skins.

The most important thing to remember when dealing with custom levels and
mods is JK's checksum system. All players in a game need to be running
exactly the same patches and levels, or you won't be able to play with
each other. It is crucial that all the people who will be playing have
the same version of everything and are running everything correctly. If
you need any help installing something, head over to the forums and ask.
Happy Gaming\!
