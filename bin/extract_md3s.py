import os
import re

import bs4

# relative to root of project, not location of this script
md3_file = './data/md3s.html'
out_dir  = './data/md3'

this_dir = os.path.dirname(__file__)
out_dir = os.path.abspath(this_dir + "/../" + out_dir)

def main():

    md3_content = slurp_file(md3_file)

    tables = extract_tables(md3_content)

    objects_table = tables[0]
    players_table = tables[1]

    objects = extract_table_data(objects_table)
    players = extract_table_data(players_table)

    print(players)

    output_data(objects, 'md3.objects')
    output_data(players, 'md3.players')

def output_data(data, category):
    print("outputtting to", out_dir);

    for row in data:
        output_file_name = out_dir + '/' + row['file'] + '.md'

        with open(output_file_name, 'w') as f:
            f.write('---\n');
            f.write('file: '       + row['file']       + '\n')
            f.write('author: '     + row['author']     + '\n')
            f.write('email: '      + row['email']      + '\n')
            f.write('type: '       + category          + '\n')
            f.write('date: '       + row['date']       + '\n')
            f.write('screenshot: ' + row['screenshot'] + '\n')

            # put description on own line using > operator because descriptions 
            # have combinations of double and single quotes that break the yaml 
            # parser otherwise
            f.write('description: >\n    ' + row['description'] + '\n')

            f.write('---\n');


def extract_table_data(table):
    rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')

        # extract email & name from author column
        author_link = columns[3].find('a')

        # skip header row :-|
        if not author_link:
            continue

        email = author_link['href'].replace('mailto:', '')
        author = author_link.text

        screenshot_link = columns[2].find('a')
        screenshot = re.sub(r"^/screenshots/", '', screenshot_link['href'])

        download_link = columns[0].find('a')
        href = download_link['href'].replace('/files/md3/', '')

        row = {
            'file': href,
            'description': columns[1].text,
            'screenshot': screenshot,
            'author': author,
            'email': email,
            'date': columns[4].text,
        }

        rows.append(row)

    return rows

def extract_tables(html_string):
    soup = bs4.BeautifulSoup(html_string, 'html.parser')

    tables = soup.find_all('table')

    return tables


def slurp_file(path):
    this_dir = os.path.dirname(__file__)
    path = os.path.abspath(this_dir + "/../" + path)

    with open(path) as x: f = x.read()

    return f

main()
