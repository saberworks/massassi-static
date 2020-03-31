# core modules
import os
import re
import shutil

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

#
# Loop through all files in source_dir, process the ones that need processing, 
# and copy to output_dir.
#
def main():
    for dir_name, subdirs, files in os.walk(source_dir):
        print('processing directory: {}'.format(dir_name))

        for file_name in files:
            path = "{}/{}".format(dir_name, file_name)

            should_process = 0;
            file_type = ''

            for ext in extensions:
                if file_name.endswith('.' + ext):
                    should_process = 1;
                    file_type = ext

            if should_process:
                print(f"    processing {path}")
                content = process_file(path, file_type);

                output_file(content, path, source_dir, output_dir)
            else:
                print(f"    copying {path}")
                copy_file(path, source_dir, output_dir)

#
# Process an individual file.
#
# Processing means to read the file from filesystem, interpolate the template 
# vars, and return the page content.
#
def process_file(path, file_type):
    template_vars = extract_vars_from_file(path)

    if file_type == 'md':
        template_vars['body'] = markdown.markdown(template_vars['body'], extensions=['extra'])

    tpl = get_template(outer_template)

    return tpl.render(template_vars)

#
# Write content to the same path in output_dir as it is in source_dir.
#
def output_file(content, path, source_dir, output_dir):
    # If source content has .md extension, change it to .html :-|
    path = re.sub(r'\.md$', '.html', path);

    output_path = re.sub(source_dir, output_dir, path);
    output_dir = os.path.dirname(output_path)

    os.makedirs(output_dir, exist_ok=True)

    f = open(output_path, 'w')
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
# Read the content file, extract the vars from the top and the body/content 
# from the `_body:` line to the end of the file.
#
def extract_vars_from_file(path):
    # look for _body variable; anything after this is part of the body
    body_pattern = re.compile('body:')

    # look for defined variables at the beginning of the file
    pattern = re.compile('(\w+): (.*)')

    template_vars = {}
    body = ''

    with open(path) as f:
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

