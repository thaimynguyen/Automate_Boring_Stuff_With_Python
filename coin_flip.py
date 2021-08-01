"""
ebook link: https://automatetheboringstuff.com/2e/chapter4/#calibre_link-188
textbook page 107

If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” 

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. 
Your program breaks up the experiment into two parts: 
_ the first part generates a list of randomly selected 'heads' and 'tails' values
_ the second part checks if there is a streak in it. 

Put all of this code in a loop that repeats the experiment 10,000 times 
so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. 
"""

import random

def calculate_probability():
    #CONSTANT:
    N_RUNS = 10000
    FLIPS_PER_RUN = 100
    TARGET_STREAK = 6

    #reset no of streaks
    number_of_streaks = 0

    #main loop
    for run in range(N_RUNS):
        # Code that creates a list of 100 'heads' or 'tails' values.
        coin_flips = []
        for flip in range(FLIPS_PER_RUN):
            if random.randint(0,1) == 0:
                coin_flips.append('H')
            else:
                coin_flips.append('T')

        # Code that checks if there is a streak of 6 heads or tails in a row.
        streak_count = 0
        for i in range(1, len(coin_flips)):
            if coin_flips[i] == coin_flips[i-1]:
                streak_count += 1
            else:
                streak_count = 0

            if streak_count == TARGET_STREAK:
                number_of_streaks +=1
                break   # once a streak is found, skip to next experiment run
        
    print('Chance of streak: %s%%' % round((number_of_streaks / N_RUNS * 100),2))

calculate_probability()      # the average probabilty of a streak of six heads or tails is about 54%