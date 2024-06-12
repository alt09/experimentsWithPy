
import random
secretNumber = random.randint(1, 1000)
print('choose a number between 1 and 1000')
for guessesTaken in range(1, 10):
    guess = int(input())

    if guess < secretNumber:
        print('low')
    elif guess > secretNumber:
        print('high')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('number of intentos ' + str(guessesTaken))
else:
    print('que pendejo era ' + str(secretNumber))