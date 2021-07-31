import random
answer = random.randint(1, 10)
i = 1
while i <= 3:
    guess = int(input('please guess the number? '))
    if guess < answer:
        print('oops! your guess is less than answer! try again')
    elif guess > answer:
        print('oops! your guess is bigger than answer! try again')
    elif guess == answer:
        print('bravo! that is right!')
        break
    i += 1
else:
    print('Game over')
