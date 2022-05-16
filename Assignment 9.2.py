# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Sam Gillenwater
# Creation Date: 15May2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.)  You need to identify the issues and correct them.

import random
import time


def displayIntro():
    print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
# 1The quotes were missing in the below print.
    print("")


def chooseCave():
# 2Spaces and indents were both used below. Corrected.
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

# 3Spelled cave(s) supposed to be cave
    return cave


def checkCave(chosenCave):
    print('You approach the cave...')
    # sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    # sleep for 2 seconds
# 4Above comment says sleep for 2 seconds but the code calls for 3. Switching to 2 for consistency
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
# 5unneccessary print statement
    # sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
# 6Dont need the colon behind else
    else:
# 7missing the parentheses below
        print('Gobbles you down in one bite!')


playAgain = 'yes'
# 8 One of them is yes, the other is y, switched to "no"
if playAgain == 'yes':
    displayIntro()
# 9Below should be chooseCave not choosecave
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')

    playAgain = input()
else: playAgain == "no"
# 10Misspelled "playing" below
print("Thanks for playing")



# 11Nothing was added for if the player types anything other than yes or no.


displayIntro()

chooseCave()



#I tried to change it to if instead of while but I can't get it to exit properly when I input 'no'