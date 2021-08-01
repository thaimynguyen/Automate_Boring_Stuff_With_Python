"""
Here’s what the program does:

1. It searches all the filenames in the current working directory for American-style dates.
2. When one is found, it renames the file with the month and day swapped to make it European-style.

ebook-link: https://automatetheboringstuff.com/2e/chapter10/#calibre_link-333


Assumptions:
- American style format: mm-dd-yyyy
  European style format: dd-mm-yyyy

Questions:
- How can we differentiate a date like 08-01-2020 to be American style or European style?
- Date validation? 

"""
import os, re

American_dates = re.compile(r"""^(.*?)                  # group1: before_text
                                (0[1-9]|1[0-2])         # group2: month
                                ([/\.-])                # group3: separator
                                (0[1-9]|[12]\d|3[01])   # group4: date
                                ([/\.-])                # group5: separator
                                (\d{4})                 # group6: year
                                (.*?)$                  # group7: after_text
                            """, re.VERBOSE)

dir = os.chdir(r'C:\Users\My\Desktop\Python projects\Automate_The_Boring_Stuff_With_Python\Rename_dates')
# dir = os.getcwd()
files = os.listdir(dir)

for file in files:
    match = American_dates.search(file)
    if match:
        new_name = match.group(1) + match.group(4) + match.group(3) + match.group(2) + match.group(5) + match.group(6) + match.group(7)
        print(f'File "{file}" has been renamed to"{new_name}."')
        os.rename(file, new_name)
