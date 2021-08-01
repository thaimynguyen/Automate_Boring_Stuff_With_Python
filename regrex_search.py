#! python 3.8

"""
Requirement:
_ Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. 
_ The results should be printed to the screen.

Link: https://automatetheboringstuff.com/2e/chapter9/#calibre_link-322
"""


import os, re


def search_txt(folder, regex):
    os.chdir(folder)
    files = os.listdir(folder)

    txt_files = list(filter(lambda x: x.endswith(('.txt', '.TXT')), files))

    for file in txt_files:
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                if re.search(regex, line):
                    print(f'"{line}" from "{file}" file')

def prompt_input():
    while True:
  
        # Input folder path
        folder_path = input('Enter the absolute path of the folder that you want to search: \n')
        #folder_path = r'C:\Users\My\Desktop\Python projects\Automate_The_Boring_Stuff_With_Python\RegexSearch'
        # Check if folder path exists:
        if os.path.isdir(folder_path):
            regex_pattern = input('Enter the regular expression pattern that you want to search:\n')
            return folder_path, regex_pattern
        else:
            print("The path you entered is not valid!")
    
        

search_txt(*prompt_input())
#search_txt(r'C:\Users\My\Desktop\Python projects\Automate_The_Boring_Stuff_With_Python\RegexSearch', "\d")


# splitlines() will get a list of lines without "\n" 
# readlines() will get a list of lines with "\n"
