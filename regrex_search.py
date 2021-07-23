#! python 3.8


"""
Requirement:
_ Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. 
_ The results should be printed to the screen.
Link: https://automatetheboringstuff.com/2e/chapter9/#calibre_link-322
"""

"""
Input:
_ folder path
_ regex pattern to search for ==> for multiple patterns?

Output:
_ lines that have a string matching the regex pattern
_ from which textfile?

Assumptions:
_ Accept both .txt and .TXT files

"""



import os, re


# TO DO:


while True:
    
    # Input folder path
    folder_path = input('Enter the absolute path of the folder that you want to search: \n')
    
    # Check if folder path exists:
    if os.path.exists(folder_path):
        os.chdir(folder_path)
        regex_pattern = input('Enter the regular expression pattern that you want to search:\n')
        break
    else:
        print("The path you entered is not valid!")
        


files = os.listdir(folder_path)

txt_files = list(filter(lambda x: x.endswith(('.txt', '.TXT')), files))

for file in txt_files:
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if regex_pattern in line:
                print(f'Line "{line}" from "{file}" file')



# splitlines() will get a list of lines without "\n" 
# readlines() will get a list of lines with "\n"
