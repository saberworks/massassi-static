# core modules
import os
import pathlib
import re
import shutil
import sys
import warnings
import pprint

# installed via pip
import frontmatter
import jinja2
import markdown

source_dir = './source'
output_dir = './output'

# outer template to use; actually maybe this is the only template?
templates_dir = './templates'
outer_template = 'outer.html'

# files ending in these extensions will be processed, anything else will be 
# copied directly
extensions = ['md', 'html', 'shtml', 'htm']

# directories containing "collections"
#
# relative to `source` directory
collections = {
    'tutorials': 'tutorials/*/*',
}

# directory containing "data"
#
# Data directories should contain a bunch of markdown files.  These will be 
# parsed (front matter and body included) and placed in the "data" dict 
# available to templates.  However, _pages_ for these files will not be 
# created.  These are similar to collections but don't generate pages, useful 
# for generating pages that contain a list of the data.  In my case I'm using 
# this for 3dos, md3s, mats, etc.  (things that used to reside in the database 
# but I don't want to maintain anymore)
#
# relative to the root project directory
#
base_data_dir = './data'

# Data dirs:
#   key:
#       key will be used to provide the data in the `data` dict; this allows 
#       you to specify a key different than the directory specified, but I 
#       don't recommend it.
#   values:
#       dir: what directory contains the data files
#       group_by:
#           optionally specify a key (must be present in each of the data 
#           files) that will be used to group the data in the `data` dict.  For 
#           example if each mat belongs to a `category` you can group by 
#           `category` and then the dict will look like:
#
#           data['mat']['stone'] = [ # list of mats in stone category ]
#           data['mat']['floor'] = [ # list of mats in floor category ]
#
#           if group_by is not set, the resulting data will just be in a list:
#           data['mat_categories'] = [
#               { name: foo, title: Foo },
#               { name: bar, title: Bar },
#           ]
#
data_dirs = {
    '3do': {
        'dir': base_data_dir + '/3do',
        'group_by': 'type',
    },
    'mat': {
        'dir': base_data_dir + '/mat',
        'group_by': 'category',
    },
    'mat_categories': {
        'dir': base_data_dir + '/mat_categories',
    },
    'md3': {
        'dir': base_data_dir + '/md3',
        'group_by': 'type',
    },
    'ctfpack': { 'dir': base_data_dir + '/ctfpack' },
    'mlp1':    { 'dir': base_data_dir + '/mlp1'    },
    'mlp2':    { 'dir': base_data_dir + '/mlp2'    },
    'mlp3':    { 'dir': base_data_dir + '/mlp3'    },
    'mlp4':    { 'dir': base_data_dir + '/mlp4'    },
}


#
# Loop through all files in source_dir, process the ones that need processing, 
# and copy to output_dir.
#
def main():
    collection_data = process_collections(collections)
    data = process_data(data_dirs)

    for dir_name, subdirs, files in os.walk(source_dir):
        print('processing directory: {}'.format(dir_name))

        for file_name in files:
            source_path = "{}/{}".format(dir_name, file_name)

            if not should_process(source_path):
                print(f"    copying {source_path}")
                copy_file(source_path, source_dir, output_dir)
                continue

            print(f"    processing {source_path}")
            template_vars = extract_vars_from_file(source_path)

            template_vars['collections'] = collection_data
            template_vars['data'] = data

            inner_tpl = get_template_from_memory(
                template_vars.pop('content', '')
            )

            template_vars['content'] = inner_tpl.render(template_vars)

            if source_path.endswith('.md'):
                template_vars['content'] = markdown.markdown(
                    template_vars['content'], extensions=['extra', 'toc']
                )

            tpl = get_template(outer_template)

            content = tpl.render(template_vars)

            ext = template_vars.get('ext', '')

            output_path = get_output_path(
                source_path, source_dir, output_dir, ext
            )

            output_file(content, output_path)


#
# Given source path & dir, output dir, and optional extension (only taken into 
# account if source file is markdown), generate and return the output path.
#
def get_output_path(source_path, source_dir, output_dir, ext):
    # If source path has .md extension, change it to whatever is in ext.
    # Note if ext was not set explicitly in front matter, .html was set as the 
    # default in extract_vars_...()
    source_path = re.sub(r'\.md$', '.' + ext, source_path)

    return re.sub(source_dir, output_dir, source_path)


#
# Determine proper public-facing web path for the resource.  If extension is 
# .md, look use the extension provided in the `ext` argument.  If the filename 
# is `index.html` just leave off the filename (prefer to link to something like 
# /tutorials/foo/ than /tutorials/foo/index.html).
#
def get_href(source_path, source_dir, ext):
    # If source path has .md extension, change it to whatever is in ext.
    source_path = re.sub(r'\.md$', '.' + ext, source_path)

    href = re.sub(source_dir, '', source_path)

    # replacing the '/' in '/index.html' ensures we're only messing with 
    # `index.html` and not `tutorial_index.html`, for example
    return re.sub(r'/index.html$', '/', href)


#
# File should be processed if:
#   * it ends in a support extension _and_
#   * it contains at least one var (like title:)
#
def should_process(source_path):
    should_process = False;

    try:
        should_process = has_supported_ext(source_path) \
            and has_tags(source_path)
    except Exception as e:
        print("Unable to check file because of errors: ", source_path, file=sys.stderr)
        print("Error: ", e, file=sys.stderr)
        sys.exit(1);

    return should_process;


#
# True if the file has a supported extension (list at top), False otherwise.
#
def has_supported_ext(path):
    for ext in extensions:
        if path.endswith('.' + ext):
            return True

    return False


#
# For performance, don't parse the entire file; just look at the first line; 
# first line should always have a tag if it wants to be parsed.
#
def has_tags(path):
    f = open(path)
    line = f.readline()
    f.close()

    pattern = re.compile('^---')

    return pattern.match(line)


#
# Write content.
#
def output_file(content, path):
    directory = os.path.dirname(path)

    os.makedirs(directory, exist_ok=True)

    f = open(path, 'w')
    f.write(content)
    f.close()


#
# Copy file from source_dir to output_dir (generally used for files that aren't 
# being processed)
#
def copy_file(path, source_dir, output_dir):
    output_path = re.sub(source_dir, output_dir, path)
    output_dir = os.path.dirname(output_path)

    os.makedirs(output_dir, exist_ok=True)

    shutil.copyfile(path, output_path)


#
# Look in the collections configuration for any directories (relative to 
# source) that hold collections.  A "collection" is a bunch of metadata pulled 
# from source files and collected into a dict.  This information is then 
# available to templates via the "collections" key.
#
# This is useful if you have a directory of files (or a directory of 
# subdirectories, each containing a file) that contain related data.  Our first 
# use case is the tutorials/ directory; each tutorial can contain its own 
# metadata (author, description, pub date, etc.) and it will be collected into 
# list that can be used to automatically generate a tutorials index page.
#
def process_collections(collections):
    if len(collections) == 0:
        return []

    # will contain keys that match the collections key, values are lists of 
    # vars parsed out of the matching files (minus the body)
    collection_data = {}

    for name, pattern in collections.items():
        collection_data[name] = []

        # there are probably other things that can be put into the path vars to 
        # cause this to glob files it shouldn't
        maybe_safe_path = re.sub(r'\.\.', '', pattern)

        for file_path in pathlib.Path(source_dir).glob(maybe_safe_path):
            if not should_process(str(file_path)):
                continue

            template_vars = extract_vars_from_file(str(file_path), False)

            ext = template_vars.get('ext', '')

            template_vars['_path'] = str(file_path)
            template_vars['_href'] = get_href(
                "./" + str(file_path), source_dir, ext
            )

            collection_data[name].append(template_vars)

    # sort all the keys :-|  by document title I guess
    # TODO: allow specifying key to sort by in collection definition?
    for key, collection in collection_data.items():
        collection_data[key] = sorted(
            collection, 
            key=lambda x: (x['title'] is None, x['title'])
        )

    return collection_data


#
# Deal with `data` directories.
#
def process_data(data_dirs):
    data = {}

    for key, data_info in data_dirs.items():
        data_dir = data_info['dir']
        group_by = data_info['group_by'] if 'group_by' in data_info else ''

        if group_by:
            data[key] = {}
        else:
            data[key] = []

        if not os.path.isdir(data_dir):
            print("data_dir specified but missing:", data_dir, file=sys.stderr)
            continue

        for entry in sorted(os.listdir(data_dir), key=str.casefold):
            path = data_dir + '/' + entry

            if not os.path.isfile(path):
                continue

            template_vars = extract_vars_from_file(path)

            if group_by:
                if template_vars[group_by] not in data[key]:
                    data[key][template_vars[group_by]] = []

                data[key][template_vars[group_by]].append(template_vars)
            else:
                data[key].append(template_vars)

    # pprint.pprint(data)

    return data


#
# Read the content file, extract the vars from the top ("front matter") and the 
# body/content from the rest.
#
def extract_vars_from_file(source_path, include_body=True):
    data = frontmatter.load(source_path)

    template_vars = data.metadata
    template_vars['content'] = data.content

    # If source is a markdown file, and desired output extension isn't 
    # specified, use .html.
    if source_path.endswith('.md'):
        template_vars.setdefault('ext', 'html')

    if not include_body:
        try:
            del template_vars['content']
        except KeyError:
            pass  # really don't care

    return template_vars


#
# Returns a jinja2 template object with the filesystem loader enabled (set to 
# look for templates in `templates_dir`).
#
def get_template(template_file_name):
    tpl_env = _get_template_env()
    return tpl_env.get_template(template_file_name)


#
# Returns a jinja2 template object with the passed-in template parsed.
#
# Note: same loader being used (filesystem loader) in case templates need to 
# `import` other templates
#
def get_template_from_memory(template):
    tpl_env = _get_template_env()
    return tpl_env.from_string(template)


def _get_template_env():
    tpl_loader = jinja2.FileSystemLoader(searchpath=templates_dir)
    tpl_env = jinja2.Environment(loader=tpl_loader, extensions=['jinja2.ext.loopcontrols'])
    return tpl_env


main()
