# Write your code here :-)
"""
Page 107 - LIST
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.
"""

def list_to_string(a_list: list):
    try:
        if len(a_list) > 1:
            return '{0} and {1}'.format(', '.join(a_list[:-1]), a_list[-1])
        else:
            return a_list[0]
    except IndexError:
        return 'The list is empty'

some_list = ['a']
print(list_to_string(some_list))
