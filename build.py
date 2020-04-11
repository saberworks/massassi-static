# core modules
import os
import pathlib
import re
import shutil
import sys

# installed via pip
import jinja2
import markdown

source_dir = './source'
output_dir = './output'

# outer template to use; actually maybe this is the only template?
templates_dir = './templates'
outer_template = 'outer.html';

# files ending in these extensions will be processed
extensions = ['md', 'html', 'shtml', 'htm'];

# directories containing "collections"
# at this point I need a config file :-|
# relative to `source` directory
collections = {
    'tutorials': 'tutorials/*/*',
};

#
# Loop through all files in source_dir, process the ones that need processing, 
# and copy to output_dir.
#
def main():
    collection_data = process_collections(collections)
    print(collection_data)
    sys.exit()

    for dir_name, subdirs, files in os.walk(source_dir):
        print('processing directory: {}'.format(dir_name))

        for file_name in files:
            source_path = "{}/{}".format(dir_name, file_name)

            if should_process(source_path):
                print(f"    processing {source_path}")
                template_vars = extract_vars_from_file(source_path)

                if source_path.endswith('.md'):
                    template_vars['body'] = markdown.markdown(
                        template_vars['body'], extensions=['extra', 'toc']
                    )

                tpl = get_template(outer_template)

                content = tpl.render(template_vars)

                ext = template_vars.get('ext', '')

                output_path = get_output_path(
                    source_path, source_dir, output_dir, ext
                )

                output_file(content, output_path)
            else:
                print(f"    copying {source_path}")
                copy_file(source_path, source_dir, output_dir)

#
# Given source path & dir, output dir, and optional extension (only taken into 
# account if source file is markdown), generate and return the output path.
#
def get_output_path(source_path, source_dir, output_dir, ext):
    # If source path has .md extension, change it to whatever is in ext.
    source_path = re.sub(r'\.md$', '.' + ext, source_path);

    return re.sub(source_dir, output_dir, source_path);

#
# File should be processed if:
#   * it ends in a support extension _and_
#   * it contains at least one var (like title: or body:)
#
def should_process(source_path):
    #print(f"    checking {source_path}")

    if has_supported_ext(source_path) and has_tags(source_path):
        return True

    return False

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

    pattern = re.compile('^\w+:')

    return pattern.match(line)

#
# Write content.
#
def output_file(content, path):
    output_dir = os.path.dirname(path)

    os.makedirs(output_dir, exist_ok=True)

    f = open(path, 'w')
    f.write(content)
    f.close()

#
# Copy file from source_dir to output_dir (generally used for files that aren't 
# being processed)
#
def copy_file(path, source_dir, output_dir):
    output_path = re.sub(source_dir, output_dir, path);
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
    if(len(collections) == 0):
        return [];

    # will contain keys that match the collections key, values are lists of 
    # vars parsed out of the matching files (minus the body)
    collection_data = {}

    print("PROCESSING COLLECTIONS!!!!!!");

    for name, pattern in collections.items():
        collection_data[name] = []

        # there are probably other things that can be put into the path vars to 
        # cause this to glob files it shouldn't, make it clear to the next 
        # person :(
        maybe_safe_path = re.sub(r'\.\.', '', pattern)

        print(maybe_safe_path)

        for file_path in pathlib.Path(source_dir).glob(maybe_safe_path):
            if not should_process(str(file_path)):
                continue;
            
            template_vars = extract_vars_from_file(str(file_path), False)
            template_vars['_path'] = str(file_path)
        
            collection_data[name].append(template_vars)

    return collection_data

#
# Read the content file, extract the vars from the top and the body/content 
# from the `_body:` line to the end of the file.
#
def extract_vars_from_file(source_path, include_body=True):
    # look for _body variable; anything after this is part of the body
    body_pattern = re.compile('body:')

    # look for defined variables at the beginning of the file
    pattern = re.compile('(\w+): (.*)')

    template_vars = {}
    body = ''

    with open(source_path) as f:
        in_body = False

        for line in f:
            if in_body:
                body += line
                continue

            m = pattern.match(line)
            if m:
                name = m.group(1)
                value = m.group(2)

                template_vars[name] = value
            else:
                bm = body_pattern.match(line)

                if bm:
                    in_body = True

    template_vars['body'] = body

    # If source is a markdown file, and desired output extension isn't 
    # specified, use .html.
    if source_path.endswith('.md'):
        template_vars.setdefault('ext', 'html')

    if not include_body:
        try:
            del template_vars['body']
        except KeyError:
            pass; # really don't care

    return template_vars

#
# Returns a jinja2 template object with the filesystem loader enabled (set to 
# look for templates in `templates_dir`).
#
def get_template(template):
    tpl_loader = jinja2.FileSystemLoader(searchpath=templates_dir)
    tpl_env = jinja2.Environment(loader=tpl_loader)
    return tpl_env.get_template(template)

main()

