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

CARD_BACK = """
┌───────────┐
│░░░░░░░░░░░│
│░░░░░░░░░░░│
│░░░░░░░░░░░│
│░░░░░░░░░░░│
│░░░░░░░░░░░│
│░░░░░░░░░░░│
│░░░░░░░░░░░│
└───────────┘
"""

PlayingBJ = False
PlayingPoker = False
PlayingRoulette = False
openSettings = False
typing_speed = 500
previous_menu = ""
finalhands = []

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 1000
        self.bet = 0
    def __str__(self):
        return f"{self.name} (Money: {self.money}, Hand: {self.hand}, Bet: {self.bet})"

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
        2. Music
        3. Reset settings
        4. Exit
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

        print(line)
            

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
    print("Invalid input")
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
    betamnt = 0
    create_players(num_players)
    for c, player in enumerate(players):
        if player.name != "Dealer":
            print(f"Player {c}: {player.name}")
            print(f"Money: {player.money}")
            betamnt = input("Bet amount: ")
            betamnt = validinput(betamnt, "option != '' and option.isdigit() and int(option) <= player.money")
            player.bet = int(betamnt)
    for player in players:      
        for i in range(2):
            print(CURSOR_HOME)
            clear_screen()
            deal_card(decks, player)
            print()
            print()
            print()
            printplayerinfo(players)
            sleep(0.5)
    for player in players:
        BJturn(player)           
def create_players(num_players):
    global players
    players = []

    createDealer()
    for i in range(int(num_players)):
        print(CLEAR_SCREEN + CURSOR_HOME)
        name = input("Name must be 10 characters or less, can be empty. Enter name for player " + str(i+1) + ": ")
        
        name = validinput(name, "len(option) <= 10")
        
        players.append(Player(name))
        



    i = 1      
def printplayerinfo(players):
    max_name = max(len(p.name) for p in players) + 16
    max_hand = max(len(" ".join(p.hand)) for p in players)


    display_players = [p for p in players if p.name != "Dealer"]
    dealer = next((p for p in players if p.name == 'Dealer'), None)

    if dealer:
        printDealerInfo(players)
    if display_players:
        if len(display_players[0].hand) > 0:
            first_card = display_players[0].hand[0]
            card_lines = deck[first_card].splitlines()
            card_height = len(card_lines)

            for row_i in range(card_height):
                line = []
                for p in display_players:
                    phand = "  ".join(deck[c].splitlines()[row_i] for c in p.hand)
                    line.append(phand)
                print("     ".join(line))
    names_line = " ".join(f"{f'Player {i}: '}{p.name:<{max_name}}" for i, p in enumerate(players) if p.name != "Dealer")
    hands_line = " ".join(f"{(h := f'Hand: {' '.join(p.hand)}'):<{32}}" for p in players if p.name != "Dealer")
    money_line = " ".join(f"{'Money: ' + str(p.money):<{max_name+10}}" for p in players if p.name != "Dealer")
    bet_line = " ".join(f"{'Bet Amount: ' + str(p.bet):<{max_name+10}}" for p in players if p.name != "Dealer")
    print(names_line)
    print(money_line)
    print(bet_line)
    print(f"{hands_line:<{max_name+10}}")
    
    
def printBJinfo():
    pass
def printDealerInfo(players):
    cards = players[0].hand
    card_height = len(deck[cards[0]].splitlines())
    if len(cards) > 2:
        for row_i in range(card_height):
            print(" ".join(deck[c].splitlines()[row_i] for c in cards))
        print(f"Dealer: {' '.join(players[0].hand)}")
    else:
        dealerhand = list(zip(CARD_BACK.splitlines(), deck[players[0].hand[0]].splitlines()))
        for row in dealerhand:
            print(" ".join(row))
        print(f"Dealer: {players[0].hand[0]} ")

def createDealer():
    global Dealer
    Dealer = Player("Dealer")
    players.append(Dealer)
    Dealer.money = 100000000000000000000000000000000
def BJturn(player):
    bust = False
    BlackJack = True
    at21 = False
    
    sumofcards = sum(int(cardvalue) for cardvalue in convertedplayerhand)
    playerhand = []
    convertedplayerhand = []
    for hand in player.hand:
        playerhand.append(hand[:-1])
        convertedplayerhand.append(rankvaluepair[hand[:-1]])
    rankvaluepair = {"A" : "1",
                    "2" : "2",
                    "3" : "3",
                    "4" : "4",
                    "5" : "5",
                    "6" : "6",
                    "7" : "7",
                    "8" : "8",
                    "9" : "9",
                    "10": "10",
                    "J" : "10",
                    "Q" : "10",
                    "K" : "10",}
    while not bust and not BlackJack and not at21 and not stand:
        optimal_score = sumofcards + 10 if ("A" in playerhand and sumofcards + 10 <= 21) else sumofcards
        if optimal_score == 21:
            if len(playerhand) == 2:
                BlackJack = True
                at21 = False
            else:
                at21 = True
                BlackJack = False
        elif optimal_score > 21:
            bust = 21
        else:
            stand = turnprint(player)
def turnprint(player):
    stand = False    
    print(f"Player {players.index(player) + 1}: {player.name}'s turn")
    print("1. Hit")
    print("2. Stand")
    print("3. Double down")
    if player[0].hand[0][0] in "AKQJ":
        print("4. Insurance")
    option = input()
    option = validinput(option, "option in '1234'")
    option = int(option)
    if option == 1:
        deal_card(player)
    elif option == 2:
        stand = True
    elif option == 3:
        pass
def deal_card(decks, player):
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
    global deck
    cards = createCards()
    deck = {}
    for card in cards:
        if card[:-1] != "10":
            x = f"""
┌───────────┐
│{card}         │
│           │
│           │
│     {card[-1]}     │
│           │
│           │
│         {card}│
└───────────┘
"""
        else:
            x = f"""
┌───────────┐
│{card}        │
│           │
│           │
│     {card[-1]}     │
│           │
│           │
│        {card}│
└───────────┘
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
    print("Settings")
    option = menu(subroutine=False, parameters="option.isdigit()")
    if option == "1":
        openSettings = False
        menu()
    elif option == "2":
        print("Music settings coming soon")
        print("\n")
        sleep(1)
        Settings()
def Exit():
    print("Exiting")
    print("\n")
    for i in range(randint(0,7)):
        print("."*randint(3,9))
        
        print("\033[A           \n                  \033[A")
        
    exit()
    pass
def home():
    main()
def back():
    pass
def main():
    print(CLEAR_SCREEN + CURSOR_HOME)
    display_logo()

PlayBlackjack()