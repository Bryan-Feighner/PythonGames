import random

playerChoice = ''
computerChoice = ''
on = 1
while on == 1:
    print("Please type rock, paper, or scissors to select your move!")
    input(playerChoice)
    random = random.randint(0,2)
    if random == 2:
        computerChoice = 'rock'
        print('The computer has selected rock!')
    elif random == 1:
        computerChoice = 'paper'