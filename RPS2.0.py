from tkinter import *
import random
playerChoice = StringVar(value='')
computerChoice = StringVar(value='')
gameCount = IntVar(value = 0)
winCount = IntVar(value = 0)
winRate = DoubleVar(value=0.0)
def chooseNum():
    global playerChoice
    global computerChoice
    print("Please type rock, paper, or scissors to select your move!")
    input(playerChoice)
    randomNum = random.randint(0,2)
    if randomNum == 2:
        computerChoice.set('rock')
        print('The computer has selected rock!')
    elif randomNum == 1:
        computerChoice.set('paper')
        print('The computer has selected paper!')
    else:
        computerChoice.set('scissors')
        print('The computer has selected scissors!')
def gameState(playerChoice, computerChoice): # This entire section not working, not sure if it's an if statement issue?
    global winCount
    global gameCount
    if playerChoice == computerChoice:
        print('You have tied! Nobody wins!\n')
        gameCount = 1 + gameCount
    elif playerChoice == 'rock' and computerChoice == 'scissors':
        print('You have won!\n')
        gameCount = 1 + gameCount
        winCount = 1 + winCount
    elif playerChoice == 'scissors' and computerChoice == 'rock':
        print('You have lost!\n')
        gameCount = 1 + gameCount
    elif playerChoice == 'rock' and computerChoice == 'paper':
        print('You have lost!\n')
        gameCount = 1 + gameCount
    elif playerChoice == 'paper' and computerChoice == 'rock':
        print('You have won!\n')
        gameCount = 1 + gameCount
        winCount = 1 + winCount
    elif playerChoice == 'scissors' and computerChoice == 'paper':
        print('You have won!\n')
        gameCount = 1 + gameCount
        winCount = 1 + winCount
    elif playerChoice == 'paper' and computerChoice == 'scissors':
        print('You have lost!\n')
        gameCount = 1 + gameCount