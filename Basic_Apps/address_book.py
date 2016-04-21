'''
Created By: Tyler Linne
Coded in part as a Treehouse Project
Date: 4/20/16
'''
import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.M)

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))

