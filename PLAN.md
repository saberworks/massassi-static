# The Plan

Move everything possible to static files.  There are 1200 jk mp levels so it's 
probably not feasible to make that page completely client site.  But other than 
the levels section I think everything can be static?  Let's do a list:

## Tutorials

Yes, in progress.  To make things easier, create a "collections" feature.  Each 
tutorial will have its own embedded title, description, author, and category 
(in the header).  This information can be harvested by the build.py script to 
build an index.

Notes:

* categories must have name, title, description (separate page? some place for 
  "data")
* author information and descriptions may need to be pulled from the tutorials 
  index

## Levels

Probably not.  Can probably improve this by putting some screenshots in the 
list and making the level list less dense.  Not sure any of this is worth it?

## Forums

No.  If ever closing the site I wonder if there's an option to ouptput a static 
version?

https://meta.discourse.org/t/archive-an-old-forum-in-place-to-start-a-new-discourse-forum/13433/11

## 3dos

Stored in DB, but there are few enough I can generate a static page and just 
stop taking submissions.

## Mats

Mats are dynamic but any category doesn't have many individual entries.  Can 
remove search and generate a static set of files.  Search can be removed.

## Old News

The really old news is already static.  Beyond that there is a selector thing 
that allows showing old news by date (with a really old single-day picker 
thing).  I think it makes sense to just output static files for month/year and 
link them.

## Recent Levels

Recent levels can be removed from main page.  There are no recent levels.

## Level of the Week

Level of the Week archives are small enough to generate a static page.

## Screenshot of the Day

The SotD archives are _huge_ and can't be distilled to single day.  However, no 
need to be dynamic, I think I can output static pages.  Probably do bigger 
thumbnails and 2x as many screens per page and end up with half the number of 
pages.


