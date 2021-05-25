"""
Page 72 from textbook
E-book link
https://automatetheboringstuff.com/2e/chapter3/#calibre_link-146

This program will create a back-and-forth, zigzag pattern until the user stops it by pressing the code editor's "STOP" button or by pressing CRTL-C
A Short Program: Zigzag
Let’s use the programming concepts you’ve learned so far to create a small animation program. This program will create a back-and-forth, zigzag pattern until the user stops it by pressing the Mu editor’s Stop button or by pressing CTRL-C. When you run this program, the output will look something like this:

    ********
   ********
  ********
 ********
********
 ********
  ********
   ********
    ********

"""

import time, sys

indent = 0 #Keep track of the number of white spaces before the 8 asterisks
indentIncreasing = True #Whether the indentation is increasing or not

try:
    while True: # The main program loop
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces in front
            indent += 1
            if indent == 20:
                #Change direction
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                #Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

