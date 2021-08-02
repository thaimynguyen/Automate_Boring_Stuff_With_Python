"""
Filling in the Gaps

Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder 
and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.

ebook-link: https://automatetheboringstuff.com/2e/chapter10/#calibre_link-348

"""
import os, re


def fill_the_gaps():
    
    # Input processing
    while True:
        folder = input('Enter the absolute path of a folder to search: \n')
        if os.path.isdir(folder):
            os.chdir(folder)
            prefix_pattern = input('\nEnter the prefix to search: \n')
            break
        else:
            print('Invalid link. Please enter the absolute path of a folder to search: \n')

    # Store all the files with filenames starting with the given prefix & sort them in ascending order
    file_list = []
    for file in os.listdir(folder):
        if file.startswith(prefix_pattern):
            file_list.append(file)
    
    def get_number_suffix(file_name):
        match = re.search('(\D+)(\d+)(\.\w+)', file_name)
        if match:
            number_suffix = int(match.group(2))
            return number_suffix
    
    file_list.sort(key=get_number_suffix)
    

    # Find the starting index:
    match = re.search('(\D+)(\d+)(\.\w+)', file_list[0])
    starting_index = match.group(2)
    
    new_file_list = []
    
    # Change names
    for index, file_name in enumerate(file_list):
        match = re.search('(\D+)(\d+)(\.\w+)', file_name)
        if match:
            prefix = match.group(1)
            file_extension = match.group(3)
        new_index = str(int(starting_index) + index)
        new_file_name = prefix + '0'*(len(starting_index)-len(new_index)) + new_index + file_extension
        os.rename(file_name, new_file_name)
        new_file_list.append(new_file_name)
    
    print(f'\nFiles starting with "{prefix_pattern}" had been renamed in order.')
    print('Old file names: ')
    print(*file_list, sep=', ')
    print('New file names: ')
    print(*new_file_list, sep=', ')


fill_the_gaps()