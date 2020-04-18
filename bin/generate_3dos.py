#
# data/3do.txt is a tab-separated database dump of the massassi 3dos table
#
# Parse the tab-delimited file and output individual 3do md files into the 
# source/3do directory.  Then I can retire the 3do table.
#

import csv
import os

# paths relative to the root of the project, not to this script
source_file = "data/3do.txt"
output_dir  = "data/3do/"

this_dir = os.path.dirname(__file__);

source = os.path.abspath(this_dir + "/../" + source_file)
output = os.path.abspath(this_dir + "/../" + output_dir)

with open(source) as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")

    for row in reader:
        output_file_name = output + '/' + row['file'] + '.md'

        with open(output_file_name, 'w') as f:
            f.write('---\n');
            f.write('file: '       + row['file']       + '\n')
            f.write('author: '     + row['author']     + '\n')
            f.write('email: '      + row['email']      + '\n')
            f.write('type: '       + row['type']       + '\n')
            f.write('date: '       + row['date']       + '\n')
            f.write('screenshot: ' + row['screenshot'] + '\n')

            # put description on own line using > operator because descriptions 
            # have combinations of double and single quotes that break the yaml 
            # parser otherwise
            f.write('description: >\n    ' + row['description'] + '\n')

            f.write('---\n');

