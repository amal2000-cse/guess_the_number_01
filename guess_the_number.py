import random
# random is generally a imported one in which randint() is there
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
       guess =int(input(f'guesss a number between i and {x}  :'))
       if guess<random_number:
           print('sorry, guess again..........too low')
       elif guess>random_number:
           print('sorry, guess again ..............too high')
    print(f"yay..congrats, you are correct ,  the number was {random_number}")

#guess(50)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback!='c':
        if low!=high:
           guess =random.randint(low,high)
        else:
            guess=low
        feedback=input(f'is {guess} too high (H) ,  too low (L), or correct (C) ?  :').lower()
        if feedback=='h':
            high =guess-1
        elif feedback=='l':
            low =guess+ 1
    print(f"yoyy, the computer gussed your number, {guess}, correctly")
computer_guess(500)