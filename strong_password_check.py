"""
STRONG PASSWORD DETECTION

Write a function that uses regular expressions to make sure the password string it is passed is strong. 
A strong password is defined as one that is:
_ at least eight characters long,
_ contains both uppercase and lowercase characters, 
_ and has at least one digit. 

Automate The Boring Stuff with Python
Chapter 7: Pattern Matching with Regular Expressions

Ebook link: https://automatetheboringstuff.com/2e/chapter7/#calibre_link-275
"""

import re


def strong_password_check():
    password = input('Enter password for validation:\n')

    def check_length(password: str):
        if len(password) >= 8:
            return True
        else:
            return False

    def uppercase_check(password: str):
        if re.search('[A-Z]', password):
            return True
        else:
            return False

    def lowercase_check(password: str):
        if re.search('[a-z]', password):
            return True
        else:
            return False

    def digit_check(password: str):
        if re.search('\d', password):
            return True
        else: 
            return False

    if not check_length(password):
        print('Your password is weak! Password needs to be at least 8 characters long.')
    elif not uppercase_check(password):
        print('Your password is weak! Password needs to be have at least one uppercase character.')
    elif not lowercase_check(password):
        print('Your password is weak! Password needs to be have at least one lowercase character.')
    elif not digit_check(password):
        print('Your password is weak! Password needs to be have at least one digit.')
    else:
        print('Your password is strong!')


strong_password_check()


# ALTERNATE METHOD - Using lookahead assertions

def strong_password_check2():
    password = input('Enter password for validation:\n')

    password_pattern = re.compile(r'''(
                                ^(?=.*\d+)        # at least 1 digit
                                (?=.*[A-Z]+)      # at least 1 uppercase character
                                (?=.*[a-z]+)      # at least 1 lowercase character
                                .{8,}           # at least 8 characters
                                )''', re.VERBOSE)

    if re.match(password_pattern, password):
        print('Your password is strong!')
    else:
        print('Your password is weak!')

#strong_password_check2()
