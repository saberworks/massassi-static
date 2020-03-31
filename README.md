# Massassi static site generator

## Background

Massassi has a ton of content.  Some of it is stored in a database and served dynamically.  Some of it is stored in a database and written to static files to be served by apache.  Some of it is based on perl, some on php, some ssi-based .shtml.  A lot is just static HTML pages with hard-coded fonts, sizes, etc.  Much of the content also has associated images and other downloads that need to be included.

I want to create a system that will allow me to go through all the _static_ stuff and place it into a filesystem-based repository (that can be checked into git).  I want to upgrade the static stuff so each page has a title, content, images, any associated downloads, but instead of having the entire design, css, etc., in each content page, I want to just store the content and have this static site generator output pages with the content interpolated into whatever design is present in templates/.  The point of this is that I can make design tweaks to the outer template, re-output the site, and have all pages reflect the change.

The main point of this is so I can take a bunch of our existing pages (which are based on frames) and put them into the new design.  This will take a bunch of work to translate all the static html files into "content" files.  This means removing all the outer HTML, specifying titles (to be exported to the "outer" template), removing special colors and fonts, etc.

## Content Format

Most static site generators allow you to write your code in Markdown and then they output HTML.  All my content is already in HTML.  I think we should support both Markdown and HTML sources.

### Markdown example:

```
title: Adjoin Tutorial
author: Brian
author_email: brian@massassi.net

body:

Here is some markdown _content_ that will make up the page body.

```

### HTML example:

```
title: Adjoin Tutorial
author: Brian
author_email: brian@massassi.net

body:

<p>Here is some HTML <strong>content</strong> that will make up the page body.</p>

```

## Images, css, downloads, etc.

Right now the external resources are scattered around the site and are referenced either by `/absolute_path/` or `relative_path/`.  It makes sense to keep storing the assets along side the content.  This means that if the above tutorial references some images, they should be stored in `source/`, relative to the content just like they are in the current system.

The static site generator should _copy_ every file from source/ into output/, but if the file has a recognized content extenstion (.md or .html, to start), processing will be applied.  Everything else will just be copied directly.

## Usage

### Put content in source/

Put your content in the source directory.  Every file in source will be either copied directly (images, other unrecognized file types) or processed and then output to the `output/` directory.  For example, if you have `index.html` in `source/`, it will be processed (templates applied, etc.) and then placed in `output/` as `index.html`.  File extensions will not change.  This is by design!  Since Massassi has a ton of different file extensions (.html, .htm, .shtml, .phtml, .php, etc.), and since many of those pages are linked to from external sites, I don't want the URLs to change.

### Run a build

```
$ python build.py
```

By default, this will look for sources in `source/` and will output to `output/`.  Probably allow optionally setting `--source_dir` and `--output_dir` via cli.

TODO: Consider versioning the output; for example, output to `output/YYYY-MM-DD_HH:MM:SS/` or something.

### Upload the output to server

Upload the contents of the `output/` directory to the server.  Overwrite any files that exist (that's the point).  Probably a good idea to use rsync and only update newer files (to save upload time).

### Future Considerations/Questions

At some point, I will probably want to make the system auto-thumbnail images.  This presents a problem because it will re-thumbnail every image on every build.  Makes sense to implement a build cache and only process if the source file is newer than the cached copy.

One thing I hate about jinja/django templates is that I can't use the content of a block twice (this is so stupid).  However, it looks like I don't need this functionality.  It makes sense to declare the title of a page in the content file, and then use that title to populate the HTML `<title>` as well as a heading at the top of the page.  This requires some crappy hack with vanilla django/jinja.  If I implement the file format above (with metadata including title stored at the top), I can just set the title as a regular template variable instead of using blocks.  Actually all the fields will be regular template variables.


