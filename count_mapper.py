#!/usr/bin/python

import string
import sys

special_pages = ['Media:', 'Special:', 'Talk:', 'User:', 'User_talk:', 'Project:', 'Project_talk:', 'File:', 'File_talk:', 'MediaWiki:',
                 'MediaWiki_talk:', 'Template:', 'Template_talk:', 'Help:', 'Help_talk:', 'Category:', 'Category_talk:', 'Portal:', 'Wikipedia:',
                 'Wikipedia_talk:']
bad_extensions = ['.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.txt', '.ico']
bad_titles = ['404_error/', 'Main_Page', 'Hypertext_Transfer_Protocol', 'Search']

for line in sys.stdin:
    splits = line.strip().split()
    try:
        language = splits[0]
        title = splits[1]
        num_access = splits[2]
    except:
        continue
    # Filter non en articles
    if language != 'en':
        continue
    # Filter special pages
    if any([title.startswith(special_page) for special_page in special_pages]):
        continue
    # Filter articles that start with a lowercase letter
    if any([title.startswith(letter) for letter in string.ascii_lowercase]):
        continue
    # Filter bad extensions
    if any([title.endswith(extension) for extension in bad_extensions]):
        continue
    # Filter bad titles
    if title in bad_titles:
        continue
    # Output
    print(title, num_access, sep="\t")
