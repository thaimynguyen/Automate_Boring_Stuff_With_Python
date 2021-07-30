"""
1. Write a reasonably sized regular expression that can detect dates in the DD/MM/YYYY format. 
- Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. 
- Note that if the day or month is a single digit, it’ll have a leading zero.
2.Then write additional code that can detect if it is a valid date. 

Source: Automate The Boring Stuff with Python
Chapter 7: Pattern Matching with Regular Expressions

Ebook link: https://automatetheboringstuff.com/2e/chapter7/#calibre_link-274
"""

import re



def check_date():
    
    datePattern = re.compile(r'^(.*?)(0[1-9]|[1-2]\d|3[0-1])/(0[1-9]|1[0-2])/([1-2]\d{3})(.*?)$')
    
    valid_date = datePattern.search(input('Please input a string: '))

    if valid_date:
        day = int(valid_date.group(2))
        month = int(valid_date.group(3))
        year = int(valid_date.group(4))
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if int(day) > 31:
                return False
        elif month == 2:
            if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
                if int(day) > 29:
                    return False
            else: 
                if int(day) > 28:
                    return False
        else:
            if int(day) > 30:
                return False
        return True
    
if check_date():
    print('Valid date')
else:
    print('Invalid date')
        