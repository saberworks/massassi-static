# Massassi static site generator

## Current Status (2021-09-08)

The majority of static pages have been updated.  I'm still working through the 
tutorials.  I've decided to keep a lot of the dynamic stuff dynamic and used 
that as an opportunity to learn Django.  There is a separate repository for the 
dynamic stuff (news, levels, users, comments, ratings, etc.) that will also be 
open source.  I'm doing final integration and when the site is ready, the 
source will be linked here.

## Background

[The Massassi Temple](https://www.massassi.net/) is a long-running fan site for
the game Dark Forces II: Jedi Knight (and Jedi Outcast and Jedi Academy).  The
site was pretty popular back in the day but there aren't a lot of people
editing these games anymore.  However, I would like to keep the site alive and
there are problems with the current design/system:

* it uses frames which means when people land on a specific page on the site
  they don't get a menu
* it's written in a combination of various languages, styles, and generations,
  and much of the dynamic content doesn't really need to be dynamic anymore
* it's got many generations of outdated and bad old HTML
* it takes too much maintenance

The goal of this repo is:

* get help updating the content to be in a format usable by the included
  static site generator
* make the content available/open so it doesn't disappear if I get hit by a
  bus, lose my job and can't make the hosting payments, etc.
* accept PRs that improve the site in any way (if you're planning on making a
  big change please let's talk first so no effort is wasted)


## More Background

Massassi has a ton of content.  Some of it is stored in a database and served 
dynamically.  Some of it is stored in a database and written to static files to 
be served by apache.  Some of it is based on perl, some on php, some ssi-based 
.shtml.  A lot is just static HTML pages with hard-coded fonts, sizes, etc.  
Much of the content also has associated images and other downloads that need to 
be included.

I want to create a system that will allow me to go through all the _static_ 
stuff and place it into a filesystem-based repository (that can be checked into 
git).  I want to upgrade the static stuff so each page has a title, content, 
images, any associated downloads, but instead of having the entire design, css, 
etc., in each content page, I want to just store the content and have this 
static site generator output pages with the content interpolated into whatever 
design is present in templates/.  The point of this is that I can make design 
tweaks to the outer template, re-output the site, and have all pages reflect 
the change.

The main point of this is so I can take a bunch of our existing pages (which 
are based on frames) and put them into the new design.  This will take a bunch 
of work to translate all the static html files into "content" files.  This 
means removing all the outer HTML, specifying titles (to be exported to the 
"outer" template), removing special colors and fonts, etc.

## Set Up

* Clone this repo.
* Make sure you have python3 installed
* cd into the cloned repo directory
* create a virtual environment:
    * python3 -m venv ./env
* activate it:
    * source env/bin/activate
* install dependencies:
    * pip install -r requirements.txt


## Content Format

Most static site generators allow you to write your code in Markdown and then 
they output HTML.  All my content is already in HTML.  I think we should 
support both Markdown and HTML sources.

### Markdown example:

```
---
title: Adjoin Tutorial
author: Brian
email: brian@massassi.net
---

Here is some markdown _content_ that will make up the page body.

---
```

### HTML example:

```
---
title: Adjoin Tutorial
author: Brian
email: brian@massassi.net
---

<p>Here is some HTML <strong>content</strong> that will make up the page body.</p>

```

## Images, css, downloads, etc.

Right now the external resources are scattered around the site and are 
referenced either by `/absolute_path/` or `relative_path/`.  It makes sense to 
keep storing the assets along side the content.  This means that if the above 
tutorial references some images, they should be stored in `source/`, relative 
to the content just like they are in the current system.

The static site generator should _copy_ every file from source/ into output/, 
but if the file has a recognized content extenstion (.md or .html, to start), 
processing will be applied.  Everything else will just be copied directly.

## Usage

### Put content in source/

Put your content in the source directory.  Every file in source will be either 
copied directly (images, other unrecognized file types) or processed and then 
output to the `output/` directory.  For example, if you have `index.html` in 
`source/`, it will be processed (templates applied, etc.) and then placed in 
`output/` as `index.html`.  File extensions will not change.  This is by 
design!  Since Massassi has a ton of different file extensions (.html, .htm, 
.shtml, .phtml, .php, etc.), and since many of those pages are linked to from 
external sites, I don't want the URLs to change.

Note: if you create a markdown file it should have the .md extension.  By 
default, markdown files get rendered and written as html with the .html 
extension.  If you want the markdown file to have a different extension, put 
the `ext` variable in the front matter.  Example (page named foo.md):

```
---
title: some foo
ext: htm
---

page body goes here
```

In above example, the foo.md will be output as `foo.htm` (instead of 
`foo.html`).


### Run a build

```
$ python build.py
```

By default, this will look for sources in `source/` and will output to 
`output/`.  Probably eventually allow optionally setting `--source_dir` and 
`--output_dir` via cli.

TODO: Consider versioning the output; for example, output to 
`output/YYYY-MM-DD_HH:MM:SS/` or something. (probably always output to a dated 
directory and then symlink or copy to output/).

### Upload the output to server

Upload the contents of the `output/` directory to the server.  Overwrite any 
files that exist (that's the point).  Probably a good idea to use rsync and 
only update newer files (to save upload time).

