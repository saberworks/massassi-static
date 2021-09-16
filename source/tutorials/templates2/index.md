---
title: "Templates (original)"
author: EvanC
email: ev@wave.co.nz
description: >
    Add a custom 3do to a level.
date: 2063-04-05
original: templates.htm
category: jk
---

<p class="note"><span class="tutorial-orange">Note: I found this tutorial on the server but I couldn't find
any reference to it in the old news or anywhere else.  I hope it works!
-Brian</span></p>

Author: EvanC

  
Before you do this I recommend backing up your master.tpl file.  
  
"How do I add my own 3do to a level?" That is a pretty commonly asked
question on message boards. This tutorial should answer that as well as
giving you a basic understanding of the JED templates.  
  
Well, how to add your own 3do. The first thing you need to do is copy
the master.tpl file from the JEDDATA directory, to your project
directory. Then you open it with wordpad. Once you have opened it,
scroll down to the bottom of the file. There should be these lines:  

```
# DESC: Door 15x10 1/2 of BayDoor type door  
# BBOX: -0.75 -0.499 -0.034859 0.75 0.499 0.034859  
baydoor_b   _walkstruct   model3d=bayd_b.3do size=0.951508 movesize=0.951508  
```
  
Now, I am assuming that your 3do is a door. If it is not a door, search
for a template that best fits what your 3DO is meant to be. What you
need do is select all of the above lines. Press ctrl C to copy them to
the clipboard. Put your cursor at the bottom of the text and push ctrl
V(that pastes them from the clipboard).This has created a new template
to work with. Get the name of your 3do. In your new template(not the old
one) change this line:  

```
baydoor_b   _walkstruct   model3d=bayd_b.3do size=0.951508 movesize=0.951508  
```

To this:  

```
baydoor_b   _walkstruct   model3d=my3do.3do size=0.951508 movesize=0.951508  
```
  
Notice the "model3d=bayd\_b.3do" part has been changed to
"model3d=my3do.3do" (my3do is where you put the name of your 3do). That
has made it so that the template will use my3do.3do instead of the
bayd\_b.3do. Now, because JED does not like having two templates with
the same name you have to rename it. Choose a name that will help you
remember it. I try to make my names easy to understand and I try to make
them so that they give me an idea of what the thing is. The line:  

```
baydoor_b   _walkstruct   model3d=my3do.3do size=0.951508 movesize=0.951508  
```
  
Should now be changed to this:  

```
myname   _walkstruct   model3d=my3do.3do size=0.951508 movesize=0.951508  
```
  
The "baydoor\_b" was changed to "myname". Now when you look in the JED
resource picker there should be a thing at the end called "myname".  
  
If the size of the your 3DO is significantly different than the template
you copied, you will need to change the "codes" size and movesize. The
number is the radius of the object (from the center to its edge) in
JKUs. What I have found in dealing with structures is that it is the
hieght of the object from its center. The actual properties of these
codes are unclear, and sometimes it may be neccesary to experiment with
different numbers to get them right. If you don't, you may find that you
can walk right through your 3DO, or not pass under it even after the
door is open.  
  
The last thing you need to do is change the description of the thing.
This is the writing that comes up above the 3do preview to tell you
exactly what the thing is. An example of this might be "A stormtrooper
with a railgun". This description can be whatever you like. I have just
used "a door" for this tutorial.  

```
# DESC:   a door  
# BBOX: -0.75 -0.499 -0.034859 0.75 0.499 0.034859  
baydoor_b   _walkstruct   model3d=bayd_b.3do size=0.951508 movesize=0.951508  
```

All I have changed is the text after the \# DESC. That is pretty simple
stuff. Now I will go through my understanding of the templates. A
template has a type.  
  
These are some of the types you can give to a template:  
  
<div class="tutorial-table no-headers" markdown=1>

|               |  |
|---------------|--|
| `_walkstruct` | # This is basically a structure that you can walk on. This might be an elevator or a catwalk. |
| `_structure`  | # This is a structure that you do not want to walk on. Eg: a door. Very similar to walkstruct except that if you try to walk on this one you will slide around like an ice skater (Thanks GMS_SLUG for telling me the difference:-)) |
| `_humanactor` | # I think this is any actor. By actor I mean something that has AI(artificial intelligence)

</div>
  
  
Those are the common ones. There are a lot more in the tpl but you can
experiment with them yourself(Make sure you back up your master.tpl file
first). After the type you find some "code words"(I don't know the
correct name for these but that's what I like to call them:-)) here are
some "code words":  
  
<div class="tutorial-table no-headers" markdown=1>

|                |                                                                          |
| -------------- | ------------------------------------------------------------------------ |
| **model3d**    | \# The 3do that the template uses.                                        |
| **soundclass** | \# The snd file it will use.                                              |
| **timer**      | \# I think this is the lifetime of the template. Not sure though.         |
| **cog**        | \# The cog the template uses.                                             |
| **thingflags** | \# Flags for the thing.                                                   |
| **light**      | \# The light that the thing gives off. Not to sure about this one either. |
| **sprite**     | \# If the template uses a spr file this is where you put it.              |
| **puppet**     | \# pup file that the template will use.                                   |

</div>
  
Again, there are more but I don't know what all of them mean. With this
info you should be able to make your own simple templates. I will be
trying to make my own enemy actor in the near future so I will learn a
lot more about templates. What I learn I will include in a tutorial.  
  
Written by EvanC and Mangore Kiramin

