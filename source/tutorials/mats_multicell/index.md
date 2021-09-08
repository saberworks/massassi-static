---
title: Multi-Celled MATs  
author: EvanC
email: ev@wave.co.nz
description: >
    Learn how to make MATs with more than one cell (like switches).
date: 1998-10-17
category: jk
---

Author: EvanC
  

This will teach you how to make multi-celled mats. A multi-celled mat is
one like a switch that has 2 different pictures on one mat. When you
activate a switch it goes to it's second cell so it looks like a button
has been pushed, or a switch has been thrown. Here is what you do.
Create 2 bmp files. They should be equal in size and shape and pallette
file. Save one as yourname1.bmp and they other as yourname2.bmp

Now, open up notepad and create a file like this:

> 
> 
>     MATM
>     FILENAME: C:\path\test.mat
>     
>     TEXTURES: 2
>     yourname1.bmp
>     yourname2.bmp

The first line just says that this is a mat master script. The second
line is a path for where the mat will be created. The next line after
the space tells the program how many pictures(cells) are in the mat.
Below it is a list of the pictures in it. Save this file as yourname.mtm

Now, open up MatMaster (available in the [programs section](/programs/)
) and then
click the button "compile MTM to MAT" and then click on the first button
next to the box "input file name" Open up yourname.mtm, select colourmap
options and then click convert. You have a multi-celled mat.

Evan C
