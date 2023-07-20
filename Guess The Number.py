import random
import time

computer = 0
player = 0
number = range(1, 10)


def cpu_guess():
    global computer
    if computer == 0:
        computer = random.choice(number)


def player_guess():
    global player
    try:
        player = int(input("Select a number between 1-10: \n"))
    except ValueError:
        print("Numbers only...")
        time.sleep(0.5)
        player = 0
        player_guess()


def compare():
    if player == computer:
        print("You are correct!!")
        time.sleep(1)
    elif player != computer:
        print("You lose!")
        time.sleep(1)
    restart()


def start():
    print("Play Guess The Number vs the Computer!")
    time.sleep(1)
    input("Press Enter to continue...\n")
    cpu_guess()
    print(computer)
    player_guess()
    compare()


def endgame():
    print("Thanks for playing!")
    time.sleep(2)
    exit()


def restart():
    global player
    global computer
    data = input('Would you like to try again? Yes/No\n').lower()
    time.sleep(0.5)
    if data == "yes":
        player = 0
        computer = 0
        start()
    elif data == "no":
        endgame()
    elif data != "yes" or "no":
        print("Player answer yes or no...")
        time.sleep(0.5)
        restart_game = ""
        restart()


start()
