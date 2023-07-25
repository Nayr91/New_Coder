import random
import time

#player character class
class Hero:
    def __init__ (self, name, atkbonus, armcla, basedmg, dicedmg, atkdice):
        self.name = name
        self.atkbonus = atkbonus
        self.armcla = armcla
        self.basedmg = basedmg
        self.dicedmg = dicedmg
        self.atkdice = atkdice

#Enemy class 
class Baddie:
    def __init__ (self, name, atkbonus, armcla, basedmg, dicedmg, atkdice):
        self.name = name
        self.atkbonus = atkbonus
        self.armcla = armcla
        self.basedmg = basedmg
        self.dicedmg = dicedmg
        self.atkdice = atkdice

#different dice options
d20dice = range(1, 20)
d12dice = range(1, 12)
d10dice = range(1, 10)
d8dice = range(1, 8)
d6dice = range(1, 6)

#starting point
player_name = input("Choose your characters name...\n")
player_health = 1

#attributes to be used against classes
player = Hero(name=player_name, atkbonus=6, armcla=15, basedmg=10, dicedmg=2, atkdice=d12dice)
balzog = Baddie(name="Balzog the Cruel", atkbonus=8, armcla=17, basedmg=8, dicedmg=2, atkdice=d8dice)
draygurn = Baddie(name="Draygurn the Butcher", atkbonus=6, armcla=16, basedmg=5, dicedmg=8,atkdice=d6dice)
wolf = Baddie(name="Dire Wolf", atkbonus=8, armcla=14, basedmg=4, dicedmg=4, atkdice=d6dice)
baddie_choice = 0
#choosing the opponent and designating this tot he "opponent" variable for later use
while baddie_choice != 1 or 2 or 3:
    print("Select opponent - 1. Balzog the Cruel, 2. Dragurn the Butcher, 3. Dire Wolf\n")
    baddie_choice = int(input("Type 1, 2 or 3 to select..."))
    if baddie_choice == 1:
        print("You have selected Balzog the Cruel")
        opponent = balzog
        baddie_health = 150
        break
    elif baddie_choice == 2:
        print("You have selected Draygurn the Butcher")
        opponent = draygurn
        baddie_health = 120
        break
    elif baddie_choice == 3:
        print("You have selected Dire Wolf")
        opponent = wolf
        baddie_health = 70
        break


#you deal damage
def playerturn():
    global baddie_health
    global player_health
    while player_health >= 1:
        print("It's your go",player.name,"!")
        time.sleep(1)
        print("Time to attack!")
        time.sleep(1)
        input("Press Enter to attack...\n")
        time.sleep(1)
        attackroll = (random.choice(d20dice)+player.atkbonus)
        print("You rolled",attackroll,"to strike again",opponent.name,"armour class of",opponent.armcla,"!")
        if attackroll >= opponent.armcla:
            damagedealt = player.basedmg + (player.dicedmg*(random.choice(d12dice)))
            print("You deal",damagedealt,"to", opponent.name)
            baddie_health = baddie_health-damagedealt
            print(opponent.name, "has", baddie_health, "HP left")
            time.sleep(1)
            baddieturn()
        else:
            print("Oh no, you missed!")
            time.sleep(1)
            baddieturn()
    else:
        print("Game over, you lose!")
        time.sleep(2)
        exit()

#opponent does damage
def baddieturn():
    global baddie_health
    global player_health
    while baddie_health >= 1:
        print(opponent.name,"'s turn")
        time.sleep(1)
        print("Prepare yourself!")
        time.sleep(1)
        attackroll = (random.choice(d20dice)+opponent.atkbonus)
        print(opponent.name, "rolled",attackroll,"to strike against",player.name,"armour class of",player.armcla,"!")
        time.sleep(2)
        if attackroll >= player.armcla:
            damagedealt = opponent.basedmg + (opponent.dicedmg*(random.choice(d8dice)))
            print(opponent.name, "deals",damagedealt,"damage!")
            time.sleep(1)
            player_health = player_health-damagedealt
            print(player.name, "has", player_health, "HP left")
            time.sleep(1)
            playerturn()
        else:
            print("The",opponent.name,"missed!")
            time.sleep(1)
            playerturn()
    else:
        print("The",opponent.name,"is defeated! Congratulations")
        time.sleep(2)
        gold_won = random.randint(40,300)
        print("The", opponent.name, "has dropped", gold_won,". You place it in your coin purse")
        time.sleep(2)
        exit()

#rolling to see who goes first
def initiative():
    input("Press Enter to roll...\n")
    player_roll = random.choice(d20dice)
    baddie_roll = random.choice(d20dice)
    print("Player rolled", player_roll)
    time.sleep(1)
    print(opponent.name,"rolled", baddie_roll)
    time.sleep(1)
    if player_roll == baddie_roll:
        start()
    elif player_roll > baddie_roll:
        print(player.name, "goes first...")
        time.sleep(1)
        playerturn()
    elif player_roll < baddie_roll:
        print(opponent.name, "goes first...")
        time.sleep(1)
        baddieturn()


#starting point
def start():
    global baddie_health
    global player_health
    while player_health > 0 and baddie_health > 0:
        print("Let's roll for initiative")
        player_health = 150
        time.sleep(1)
        initiative()


if __name__ == "__main__":
    start()

