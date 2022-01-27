import random

print('---------------------------------------------------------------')
print('             GUESS THE NUMBER')
print('---------------------------------------------------------------')
print()

random_num = random.randint(0, 100)
num = -1

while num != random_num:
    num = int(input('Guess a number between 0 and 100: '))
    if num < random_num:
        print('Sorry but {} is lesser than the number'.format(num))
    elif num > random_num:
        print('Sorry but {} is greater than the number'.format(num))
    else:
        print('YES! You\'ve got it. The number was ' + str(num))

print('GAME OVER')
