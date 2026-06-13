# Coin Flip Project Chapter 6

import random
number_of_streaks = 0
for experiment_number in range(10000): # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    flipList = []
    streak = False
    for i in range(100):
        i = random.randint(0,1)
        if i == 0:
            flipList.append('H')
        elif i == 1:   
            flipList.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row
    for repeat in range(len(flipList)):
        if flipList[repeat:repeat + 6] == ['H', 'H', 'H', 'H', 'H', 'H'] or flipList[repeat:repeat + 6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            streak = True
    if streak == True:
        number_of_streaks = number_of_streaks + 1
print('Chance of streak: %s%%' % (number_of_streaks / 100))
print(number_of_streaks)