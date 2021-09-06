---
title: 
author: 
email: 
description: >

date: 
original: index.shtml
category: 
---

Author:[![Printable Version](/images/printable.gif)](tutorial_print.shtml)
Multi-Celled MATs  

-----

Author: [EvanC](mailto:ev@wave.co.nz)  
  

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

Now, open up MatMaster (available at <http://www.darkjedi.com>) and then
click the button "compile MTM to MAT" and then click on the first button
next to the box "input file name" Open up yourname.mtm, select colourmap
options and then click convert. You have a multi-celled mat.

Evan C
