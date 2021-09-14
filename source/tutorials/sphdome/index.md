---
title: Perfect Spheres And Domes
author: Matt The Hutt
email: matt_the_hutt@hotmail.com
description: >
    Another way of making spheres and domes.
date: 1999-11-17
original: Tutorial.htm
category: jk
---

Author: Matt The Hutt

The dome tutorials here are OK, but you have to play with it a little to
get it just right. I was looking at the [Perfect Pipes
tutorial](/tutorials/perfect_pipes/) today
and it just hit me that with a little modification it could be used to
make perfect domes or spheres, with any number of segments.  
I'll be making a sphere in this tutorial, but you can cleave it in half
if you need a dome. First you have to decide how many segments your
sphere will have around (Longitude lines on a globe), and up-and-downs
(Latitude lines on a globe). LEC used 16 segments around and 8
up-and-down, even for that huge sphere in level 9. That's the numbers
I'm going to use in this tutorial.  
To start it, you create a circular shape. You can use FreeSector, or
make it using the [perfect
polygons](/tutorials/perfect_polygons/) method.
Either way, make it have twice the number of points you want the sphere
to have up-and-down.  
  
![](Tut1.jpg)  
Then, cleave it in half.  
  
![](Tut2.jpg)  
Now, look at it from a top view. This is the hard part. If you want 16
segments around, you need to rotate it 11.25 degrees around the grid,
and cleave it off.  
  
![](Tut3.jpg)  
Then rotate it the other way, and cleave it off again. The tricky part
is making sure the index vertex (the big dot) is on the point of the
triangle. You don't have to, but it makes life sooooo much easier. You
may have to try it a few times, cleaving in different directions, until
you get it that way.  
  
![](Tut4.jpg)  
Now just copy this shape, and paste it. Rotate it 22.5 degrees, and line
it up with the other one. This is why it is so much easier to have the
index vertex on the tip--you can line things up very easily.  
  
![](Tut5.jpg)  
Keep pasting, and rotate it 22.5 degrees more each time. When you line
them all up, you can adjoin the sectors and merge them into one big
sphere. Then you can cleave it in half if you need a dome.  
  
![](Tut6.jpg)
