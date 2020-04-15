---
title: "Teachings: Cleaving and Deleting"
ext: htm
---

Welcome to the first installment of
*Teachings*. This column won't address specific topics like our
tutorials do, but will be more of a tips repository, to share things
that I've learned in my short (about 3 months) editing "career."  
  
I can't stress the importance of learning Jed's cleaving tools. Many
levels I have seen seem to have lots of areas that look just like all
the tutorials on this site. The tutorials were never intended to be used
for actual level architecture, but as stepping stones to learn the
basics, therefore allowing you to learn more advanced techniques.  
  
How does this tie in to cleaving? Take the beams tutorial for instance.
There is really nothing more to learn about jed than that. Why do I say
that? If you read and understand the beams tutorial, you are capable of
doing *anything* having to do with level architecture (none of this
applies to cogs, etc.).  
  
Open up a few LEC made levels, and take a look. There are rarely
perfectly square or rectangle hallways. Usually they are laced with
regular old beams, supports, or some fancy stuff. ALL of this can be
done using the concepts taught in the beams tutorial.  
  
For instance, there are hallways that are slanted up towards the
ceiling, but have beam-type supports in some of the walls. This is done
simply by making a diaganal cleave in the sector, rather than the normal
cleave that just follows the contours (or lack thereof) of the wall.
Then, you take that sector, dice it up a bit, and delete any area you'd
like to become solid.  
  
Okay, you want columns along a walkway? just select the sector in which
you want them, switch to the top down view, and sector cleave a column
shape. After that, select the sector that is the column, and delete it.
This makes it solid, and you can now texture the outside of it. You can
also clip the top and bottom of the sector, and make bases for each
column, making it more realistic.  
  
Things like that are very important to making a good level. There are
some things to remember though. First of all, always keep framerate in
mind. What affects framerate?  
  
If you have a huge open area, with lots of complex architecture visible
at once, then framerate will go down. Try to create the level in such a
way that you can only see part of it at one time. For instance, don't
create a building that you can get to the top of, and see the whole
level. Create a window or something that only lets you see part of it at
one time. Bad framerate is one of the best ways to kill a good level.  
  
Another thing that can destroy framerate is sloppy cleaving. Sloppy
cleaving is one of my worst pet-peeves. I tend to merge a lot of my
surfaces (if you merge the edge between two surfaces, you can then
delete the extra vertices, leaving you with one surface). This helps
when the shadows are calculated. You have to be careful though, as it is
easy to create non-convex surfaces and sectors this way. Be sure to KNOW
what you are doing. Plus, save often, as that elusive "undo" isn't
implemented yet.  
  
More on sloppy cleaving? Read the stairs tutorial. Notice that if you
cleave the stairs diagonally first, it saves your top sector from being
all cut up like the bottom. The fewer sectors you have, the better.  
  
Thanks for reading,  
Brian

