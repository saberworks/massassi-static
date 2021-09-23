---
title: "How to get Jedi Knight: Dark Forces II running under Linux/Wine"
---

[TOC]

## Prerequisites

* have a working Linux install; I'm using Ubuntu 20.04 (but this also worked
  on 18.04)
    * If you're on a different distro, you'll need to figure out the wine
      installation yourself, but the rest of the instructions should work
* have 2 ISOs, one for each original JK CD

If you don't have these ISOs, but you do have a computer with a CD drive, and each of the 2 JK disks, you can follow these instructions to rip an ISO of each:

[Create an ISO Image from a CD under Linux](https://www.thomas-krenn.com/en/wiki/Create_an_ISO_Image_from_a_source_CD_or_DVD_under_Linux)

Please Note: it is possible to use wine to run the installers from the CDs directly.  I have done it in the past but my JK CDs are so old and messed up I just ripped ISOs that I will save for later.

In my case, I ripped ISOs from the two JK CDs and I'm using those.  The filenames of the ISOs are `jk1.iso` and `jk2.iso`.

![](isos.png)

## Install Wine

In a terminal, run:

```
    sudo apt install wine64
```

Once it's finished, you can run winecfg to test the application.  Feel free to poke around in the options and then close it when you're done.

![](winecfg.png)

## Mount the first disk ISO.

Create a directory into which you will mount the ISO.  In my case, the directory I want is `/home/brian/fake_cd_drive`:

```
    cd
    mkdir fake_cd_drive
```

Now mount the ISO into the directory that was just created:

```
    sudo mount -o loop /home/brian/iso/jk1.iso /home/brian/fake_cd_drive
```

Example output:

```
    brian@oree:~$ sudo mount -o loop /home/brian/iso/jk1.iso /home/brian/fake_cd_drive
    mount: /home/brian/fake_cd_drive: WARNING: device write-protected, mounted read-only.
    brian@oree:~$ 
```

Verify it by changing into the directory and listing files:

```
    cd /home/brian/fake_cd_drive
    ls -l
```

Example output:

```
    brian@oree:~/fake_cd_drive$ ls -l
    total 576
    dr-xr-xr-x  1 root  root    2048 Sep 11  1997 ./
    drwxr-xr-x 58 brian brian   4096 Sep 22 21:22 ../
    -r-xr-xr-x  1 root  root      52 Sep 11  1997 autorun.inf*
    dr-xr-xr-x  1 root  root    4096 Sep 10  1997 directx/
    dr-xr-xr-x  1 root  root    2048 Sep 10  1997 gamedata/
    dr-xr-xr-x  1 root  root    2048 Sep 11  1997 install/
    -r-xr-xr-x  1 root  root  214528 Sep 11  1997 jedi.doc*
    -r-xr-xr-x  1 root  root  309760 Sep 11  1997 jedi.exe*
    -r-xr-xr-x  1 root  root    1736 Sep 11  1997 jedi.txt*
    -r-xr-xr-x  1 root  root   31319 Sep 11  1997 readme.txt*
    -r-xr-xr-x  1 root  root   16896 Sep 11  1997 setup.exe*
```

## Run the installer

Run the installer using wine.

Still in the `fake_cd_drive` directory, run:

```
    wine setup.exe
```

This should open the installer, and it looks mostly like it does on Windows:

![](installer1.png)

Run through the installation steps as normal.

* Choose Complete Installation when prompted
* The default Destination Directory is fine
* The start menu nonsense is nonsense
* Jedi Knight does appear in the "Wine" section of my Cinnamon "start" menu

After installation, you should see the launcher.

![](launcher.png)

Click Play!

Everything works for me.  Important things to set up once the game is launched:

* Enable 3d Acceleration
* Choose the resolution that matches your monitor

<a href="game.png"><img src="game.png" width=800 class="sotd-list-thumbnail"></a>

## Launching the game

After you exit the game, you can launch it again by finding the Jedi Knight entry in your "start" menu.

## What about the CD music?

It doesn't seem to work with the ISO.  However, if you have a CD drive and you can install from the original JK CDs, and you leave the CD inserted while playing, the music works.

## It prompted me for Disc 2

I think you can alt-tab out of the game to do this.

Unmount the first ISO, and then mount the second one using a similar command.

```
    sudo umount /home/brian/fake_cd_drive
    sudo mount -o loop /home/brian/iso/jk2.iso /home/brian/fake_cd_drive
```

Then alt-tab back into the game.
