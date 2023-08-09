import random

playerChoice = ''
computerChoice = ''
on = 1
gameCount = 0
winCount = 0
winRate = 0.0
def chooseNum():
    global playerChoice
    global computerChoice
    print("Please type rock, paper, or scissors to select your move!")
    input(playerChoice)
    randomNum = random.randint(0,2)
    if randomNum == 2:
        computerChoice = 'rock'
        print('The computer has selected rock!')
    elif randomNum == 1:
        computerChoice = 'paper'
        print('The computer has selected paper!')
    else:
        computerChoice = 'scissors'
        print('The computer has selected scissors!')
def gameState():
    global winCount
    global gameCount
    global playerChoice
    global computerChoice
    if playerChoice == computerChoice:
        print('You have tied! Nobody wins!\n')
        gameCount+=1
    elif playerChoice == 'rock' and computerChoice == 'scissors':
        print('You have won!\n')
        gameCount+=1
        winCount+=1
    elif playerChoice == 'scissors' and computerChoice == 'rock':
        print('You have lost!\n')
        gameCount+=1
    elif playerChoice == 'rock' and computerChoice == 'paper':
        print('You have lost!\n')
        gameCount+=1
    elif playerChoice == 'paper' and computerChoice == 'rock':
        print('You have won!\n')
        gameCount+=1
        winCount+=1
    elif playerChoice == 'scissors' and computerChoice == 'paper':
        print('You have won!\n')
        gameCount+=1
        winCount+=1
    elif playerChoice == 'paper' and computerChoice == 'scissors':
        print('You have lost!\n')
        gameCount+=1
while on == 1:
    global gameCount
    global winCount
    global playerChoice
    global computerChoice
    chooseNum()
    gameState()
    #winRate = winCount/gameCount
    print("You've won " + str(winCount) + " out of " + str(gameCount) + " games!\n")
    #print('Your current winrate is ' + str(winRate) + "\n")
    print("Would you like to play again? Type 1 for yes and 0 for no!\n")
    input(on)
