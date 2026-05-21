### Personal Programming Project - Ryan Yeung
from operator import index
from os import system
import os
from time import sleep
import sys
from random import randint, random, shuffle

ESC = "\x1b"
CLEAR_SCREEN = f"{ESC}[2J"
CURSOR_HOME = f"{ESC}[H"
HIDE_CURSOR = f"{ESC}[?25l"
SHOW_CURSOR = f"{ESC}[?25h"
PlayingBJ = False
PlayingPoker = False
PlayingRoulette = False
openSettings = False
typing_speed = 500
previous_menu = ""


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 1000
    def __str__(self):
        return f"{self.name} (Money: {self.money}, Hand: {self.hand})"
def typeWriter(text):
    index = 0
    for character in text:
        if text[index-1] == text[index]:
            sleep(randint(8, 50) / typing_speed)
        elif text[index].isupper():
            sleep(randint(10, 60) / typing_speed)
        elif text[index].isalpha():
            sleep(randint(1, 20) / typing_speed)
        else:
            sleep(randint(6, 50) / typing_speed)
        
        index += 1
        sys.stdout.write(character)
        sys.stdout.flush()
def clear_screen():
    if os.name == 'nt':
        _ = system('cls')
    elif os.name == 'posix':
        _ = system('clear')
def display_logo():
    index = 1
    print("\n")
    print("\n")
    print("\n")
    print(HIDE_CURSOR)
    logo = """
   █████████    █████████    █████████  █████ ██████   █████    ███████   
  ███▒▒▒▒▒███  ███▒▒▒▒▒███  ███▒▒▒▒▒███▒▒███ ▒▒██████ ▒▒███   ███▒▒▒▒▒███ 
 ███     ▒▒▒  ▒███    ▒███ ▒███    ▒▒▒  ▒███  ▒███▒███ ▒███  ███     ▒▒███
▒███          ▒███████████ ▒▒█████████  ▒███  ▒███▒▒███▒███ ▒███      ▒███
▒███          ▒███▒▒▒▒▒███  ▒▒▒▒▒▒▒▒███ ▒███  ▒███ ▒▒██████ ▒███      ▒███
▒▒███     ███ ▒███    ▒███  ███    ▒███ ▒███  ▒███  ▒▒█████ ▒▒███     ███ 
 ▒▒█████████  █████   █████▒▒█████████  █████ █████  ▒▒█████ ▒▒▒███████▒  
  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒▒    



CTRL-C to skip animation             CTRL-C to skip animation                      
"""
    list_logo = logo.splitlines()
    counter = 20
    try:
        loop = 0
        while True:
            for index in range(len(list_logo[1])):
                
                buffer= ["\n", "\n", "\n", "\n", "\n"]

                for line in list_logo:
                    #for i in range(len(line)):
                    if index <= (len(list_logo[1])) and index > counter:
                        buffer.append(((" ")*50)+(" "*(index-counter)) + line[index-counter:index])
                        #print(index, counter, (index-counter),(index-160),len(list_logo[0])+40)
                        
                        
                    elif index <= counter:
                        buffer.append(((" ")*50)+line[:index] + (" "*(len(list_logo[1])-counter)))

                        
                    #elif index <= 40 and loop == 0:
                        #buffer.append(line[:index])
                        
                        
                    
                frame = "\033[H" + "\n".join(buffer)
                sys.stdout.write(frame)
                sys.stdout.flush()
                sleep(0.016)
            loop += 1

        
    except KeyboardInterrupt:
        clear_screen()
        print(SHOW_CURSOR)
        print("STOPPED")
        sleep(1)
        clear_screen()
        menu()
def menuprint():
    global PlayingBJ, PlayingPoker, PlayingRoulette, openSettings
    if PlayingBJ:
        menuoptions = """
        1. Home
        2. Continue Playing
        3. Settings
        4. Exit
        """
    elif PlayingPoker:
        menuoptions = """
        1. Home
        2. Continue Playing
        3. AI difficulty
        4. Luck
        5. Settings
        6. Exit
        """
    elif PlayingRoulette:
        menuoptions = """
        1. Home
        2. Continue Playing
        3. Luck
        4. Settings
        5. Exit
        """
    elif openSettings:
        menuoptions = """
        1. Back
        2. Change typing speed
        3. Music
        4. Reset settings
        5. Exit
        """
    else:
        menuoptions = """
        1. Play Blackjack
        2. Play Poker
        3. Play Roulette
        4. Settings
        5. Exit
        """
    
    return menuoptions
def menu(subroutine=True, parameters=None, prevfunction=""):
    global PlayingBJ, PlayingPoker, PlayingRoulette, openSettings
    menuoptions = menuprint()
    
    menulist = menuoptions.splitlines()
    for line in menulist:

        typeWriter(line)
            

        print("\n")
    PlayingBJ = False
    PlayingPoker = False
    PlayingRoulette = False
    openSettings = False   
    if subroutine == True:
        for i in range(len(menulist)):
            menulist[i] = menulist[i].strip()
            menulist[i] = menulist[i].replace(" ", "")
        menulist.pop(0)
        menulist.pop(-1)
        funcs = {}
        for i in range(len(menulist)):
            x = menulist[i][2:]
            
            funcs[str(i+1)] = eval(x)
        x = input()
        while x not in funcs:
            invalidinput()
            x = input()
        clear_screen()
        funcs[x]()

    else:
        option = input()
        option = validinput(option, parameters)
        
        return option
def invalidinput():
    typeWriter("Invalid input")
    print("\n")
def validinput(option, parameters):
    while not eval(parameters):
        invalidinput()
        option = input()
    return option
def PlayBlackjack():
    global PlayingBJ
    PlayingBJ = True
    print("Playing Blackjack")
    num_players = input("Enter number of players (1-4): ")
    num_players = validinput(num_players, "option.isdigit() and 1 <= int(option) <= 4")
    decks = makeBJcards()

    create_players(num_players)

    for i in range(int(num_players)):
        deal_card(decks, 2, players[i])
    printplayerinfo(players)
def create_players(num_players):
    global players
    players = []

    
    for i in range(int(num_players)):
        name = input("Enter name for player " + str(i+1) + ": ")
        players.append(Player(name))


    i = 1 
    
        
        
def printplayerinfo(players):
    spaces = 64//len(players)
    names_line = (" "*(spaces)).join([f"Player {i+1}: {p.name}" for i, p in enumerate(players)])
    hands_line = (" "*(spaces)).join([f"Hand: {p.hand}" for p in players])
    money_line = (" "*(spaces)).join([f"Player {i+1} $: {p.money}" for i, p in enumerate(players)])
    
    print(names_line)
    print(hands_line)   
    print(money_line)
def deal_card(decks, num_cards, player):
    
    for _ in range(num_cards):
        card = decks[0]
        decks.pop(0)
        player.hand.append(card)
    
def makeBJcards():
    deck = draw_cards()
    decks = []
    num_decks = input("Enter number of decks (1-8): ")
    num_decks = validinput(num_decks, "option.isdigit() and 1 <= int(option) <= 8")
    for i in range(int(num_decks)):
        for card in deck:
            decks.append(card)
    shuffle(decks)
    return decks
def createCards():
    suits = ['♠', '♥', '♦', '♣']
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    cards = []
    for suit in suits:
        for r in rank:
            cards.append(r + suit)
    return cards
def draw_cards():
    cards = createCards()
    deck = {}
    for card in cards:
        if "10" in card:
            x = f"""
            ┌─────────┐
            │{card}      │
            │         │
            │         │
            │    {card[-1]}    │
            │         │
            │         │
            │      {card}│
            └─────────┘
            """
            
        else:
            x = f"""
            ┌─────────┐
            │{card}       │
            │         │
            │         │
            │    {card[-1]}    │
            │         │
            │         │
            │       {card}│
            └─────────┘
            """
        deck[card] = x
    
    return deck
def PlayPoker():
    global PlayingPoker
    PlayingPoker = True
    print("Playing Poker")
    pass
def PlayRoulette():
    global PlayingRoulette
    PlayingRoulette = True
    print("Playing Roulette")

    pass
def Settings():
    global openSettings
    
    openSettings = True
    print("\n")
    typeWriter("Settings")
    option = menu(subroutine=False, parameters="option.isdigit()")
    if option == "1":
        openSettings = False
        menu()
    elif option == "2":
        global typing_speed
        typing_speed = Changetypingspeed(typing_speed)*50
        Settings()
    elif option == "3":
        typeWriter("Music settings coming soon")
        print("\n")
        sleep(1)
        Settings()
def Exit():
    typeWriter("Exiting")
    print("\n")
    for i in range(randint(0,7)):
        typeWriter("."*randint(3,9))
        
        print("\033[A           \n                  \033[A")
        
    exit()
    pass
def Changetypingspeed(typing_speed):
    typeWriter("Current typing speed: " + str(typing_speed))
    print("\n")
    typeWriter("Enter new typing speed (1-1000%): ")
    print("\n")
    x = input()
    if validinput(x, "option.isdigit() and int(option) >= 1 and int(option) <= 1000"):
        typing_speed = int(x)
        
        typeWriter("Typing speed changed to " + str(typing_speed))
        print("\n")
    else:
        invalidinput()
    return typing_speed
def home():
    main()
def back():
    pass
def main():
    print(CLEAR_SCREEN + CURSOR_HOME)
    display_logo()

PlayBlackjack()