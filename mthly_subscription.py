"""
Program: average_scores.py
Author: Daniel Heiden
Last date modified: 06/08/2020

The purpose of this program is to solicit subscriptions, and provide type and cost to subscribe
The input is 'Y' or 'N' to subscribe, then the subscription-level.
the main "subscribe_level" function will return the subscription-level and cost
The output is the printout of the returned values from the main function.
"""

# defines subscribe_level function


def subscribe_level():
    level = input('What level would you like? ')
    if level in ('Platinum', 'platinum'):
        return '$60'
    elif level in ('Gold', 'gold'):
        return '$50'
    elif level in ('Silver', 'silver'):
        return '$40'
    elif level in ('Bronze', 'bronze'):
        return '$30'
    elif level in ('Free Trial', 'Free trial', 'free trial'):
        return '$0'

# gives subscription choices


def choices():
    print('Excellent!')
    print('Your choices are: \nPlatinum \nGold \nSilver \nBronze \nor Free Trial')


# defines generic end function if subscription declined
def end():
    print('That\'s too bad, goodbye!')
    quit()


if __name__ == '__main__':
    yes_no = input('Would you like to subscribe? ')
    if yes_no in ('n', 'no', 'No', 'nope'):
        end()
    else:
        choices()
    subscribe_cost = subscribe_level()
    print('Your subscription cost is ', subscribe_cost)

""" 
Test# reply    sub-level ExpectVal   CalcVal
1       nope    -         goodbye!    goodbye!     
2       yes    Platinim     $0        None
3       yes      Gold       $50       $50
4       Yes    Free trial    $0        $0

NOTE: Test #2 is purposely misspelled, noted multiple bugs/instances of bad input that I could not 'catch'
"""


