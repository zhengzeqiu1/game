import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)

print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
print('You will have 6 times to try')

# 给6次机会
for i in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high')
    elif guess == number:
        break

if guess == number:
    guessesTaken = str(i)
    print('Good job,'+ myName + '!You guessed my number in ' + guessesTaken + ' guesses!')
else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
