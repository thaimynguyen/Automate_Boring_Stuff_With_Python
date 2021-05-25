"""
Link: https://automatetheboringstuff.com/2e/chapter3/#calibre_link-150
Textbook page 76

The Collatz Sequence
Write a function named collatz() that has one parameter named number. 
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1
"""

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number

    else:
        number = number * 3 + 1
        print(number)
        return number

try:
    x = int(input('Enter a number: '))
    while x != 1:
        x = collatz(x)
except:
    print("Please enter a valid integer")
