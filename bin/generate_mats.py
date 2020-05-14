#
# data/mats.txt is a tab-separated database dump of the massassi mats table
#
# Parse the tab-delimited file and output individual mat md files into the 
# data/mat directory.  Then I can retire the mats table.
#

import csv
import os
import sys

from datetime import datetime

# columns:
#   mat_id
#   category_id
#   mat_filename
#   mat_description
#   mat_colormap
#   author_name
#   author_email
#   date

# paths relative to the root of the project, not to this script
source_file = "data/mats.txt"
output_dir  = "data/mat/"

cat_output_dir = "data/mat_categories/"

this_dir = os.path.dirname(__file__);

source = os.path.abspath(this_dir + "/../" + source_file)
output = os.path.abspath(this_dir + "/../" + output_dir)

cat_output = os.path.abspath(this_dir + "/../" + cat_output_dir)

#mysql> select * from mat_categories;
#+-------------+---------------+-----------------------------------------------------------+
#| category_id | category_name | category_description                                      |
#+-------------+---------------+-----------------------------------------------------------+
#|           3 | Skies         | Only sky mats allowed.                                    |
#|           2 | Nature        | Leaves, vines, plants, etc.                               |
#|           1 | Winter        | Any mat that has a winter theme.                          |
#|           5 | Numbers       | Number mats for score keeping and such.                   |
#|           4 | Signs         | Mats designed to be used as signs or billboards.          |
#|           6 | Water         | Various water mats.                                       |
#|           7 | Walls         | Mats that could be used for walls.                        |
#|           8 | Grates        | Grates that can be cut.                                   |
#|           9 | Lights        | Lights to warn or lights to add effect.                   |
#|          10 | Floors        | Floor designs or textures.                                |
#|          13 | Decor         | These mats will add those little touches to your project. |
#|          12 | Mat Packs     | Mat packs that don't really belong in a certain category. |
#|          14 | Wood          | Mats having to do with wood.                              |
#|          15 | Sand          | These mats all have something to do with sand.            |
#|          16 | Grass         | All different kinds of grass mats.                        |
#|          17 | Brick         | Mats that were built brick by brick.                      |
#|          18 | Canyon        | These mats have a canyon theme.                           |
#|          19 | Stone/Cement  | Stone and/or cement type mats.                            |
#|          20 | Glass         | Mats that could be used as glass.                         |
#|          21 | Ceiling       | You can find the ceiling mats here.                       |
#|          22 | Metal         | All different kinds of metal can be found here.           |
#|          23 | Jedi Outcast  | Various Jedi Outcast textures.                            |
#+-------------+---------------+-----------------------------------------------------------+
#22 rows in set (0.00 sec)


categories = {
    'skies': {
        'id': '3',
        'description': 'Only sky mats allowed.'
    },
    'nature': {
        'id': '2',
        'description': 'Leaves, vines, plants, etc.'
    },
    'winter': {
        'id': '1',
        'description': 'Any mat that has a winter theme.'
    },
    'numbers': {
        'id': '5',
        'description': 'Number mats for score keeping and such.'
    },
    'signs': {
        'id': '4',
        'description': 'Mats designed to be used as signs or billboards.'
    },
    'water': {
        'id': '6',
        'description': 'Various water mats.'
    },
    'walls': {
        'id': '7',
        'description': 'Mats that could be used for walls.'
    },
    'grates': {
        'id': '8',
        'description': 'Grates that can be cut.'
    },
    'lights': {
        'id': '9',
        'description': 'Lights to warn or lights to add effect.'
    },
    'floors': {
        'id': '10',
        'description': 'Floor designs or textures.'
    },
    'decor': {
        'id': '13',
        'description': 'These mats will add those little touches to your project.'
    },
    'packs': {
        'id': '12',
        'description': "Mat packs that don't really belong in a certain category.",
        'name': 'Mat Packs'
    },
    'wood': {
        'id': '14',
        'description': 'Mats having to do with wood.'
    },
    'sand': {
        'id': '15',
        'description': 'These mats all have something to do with sand.'
    },
    'grass': {
        'id': '16',
        'description': 'All different kinds of grass mats.'
    },
    'brick': {
        'id': '17',
        'description': 'Mats that were built brick by brick.'
    },
    'canyon': {
        'id': '18',
        'description': 'These mats have a canyon theme.'
    },
    'stone': {
        'id': '19',
        'description': 'Stone and/or cement type mats.',
        'name': 'Stone/Cement',
    },
    'glass': {
        'id': '20',
        'description': 'Mats that could be used as glass.',
    },
    'ceiling': {
        'id': '21',
        'description': 'You can find the ceiling mats here.'
    },
    'metal': {
        'id': '22',
        'description': 'All different kinds of metal can be found here.'
    },
    'jo': {
        'id': '23',
        'description': 'Various Jedi Outcast textures.',
        'name': 'Jedi Outcast',
    }
}

categories_by_id = { value['id']: key for key, value in categories.items() }

def main():
    with open(source) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")

        for row in reader:
            output_file_name = output + '/' + row['mat_filename'] + '.md'

            with open(output_file_name, 'w') as f:
                filename   = row['mat_filename'] + '.zip'
                screenshot = row['mat_filename'] + '.jpg'
                category   = categories_by_id[row['category_id']]
                date       = format_date(row['date'])

                f.write('---\n');
                f.write('file: '       + filename            + '\n')
                f.write('author: '     + row['author_name']  + '\n')
                f.write('email: '      + row['author_email'] + '\n')
                f.write('category: '   + category            + '\n')
                f.write('date: '       + date                + '\n')
                f.write('screenshot: ' + screenshot          + '\n')
                f.write('colormap: '   + row['mat_colormap'] + '\n')

                # put description on own line using > operator because 
                # descriptions have combinations of double and single quotes 
                # that break the yaml parser otherwise
                f.write('description: >\n    ' + row['mat_description'] + '\n')

                f.write('---\n');

    for key, value in categories.items():
        cat_output_file = cat_output + '/' + key + '.md'

        with open(cat_output_file, 'w') as f:
            title = value['name'] if 'name' in value else key.title()

            f.write('---\n');
            f.write('name: '      + key   + '\n')
            f.write('title: '     + title + '\n')

            # put description on own line using > operator because 
            # descriptions have combinations of double and single quotes 
            # that break the yaml parser otherwise
            f.write('description: >\n    ' + value['description'] + '\n')

            f.write('---\n');

def format_date(timestamp):
    ts = int(timestamp)

    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')

main()

