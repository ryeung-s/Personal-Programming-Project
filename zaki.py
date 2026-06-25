import os

from time import sleep
import random

def clear_screen():
    os.system('cls' if os.name == "nt" else 'clear')


cards = ['A♡', 'K♡', 'Q♡', 'J♡', 'X♡', '9♡', '8♡', '7♡', '6♡', '5♡', '4♡', '3♡', '2♡', 'A♧', 'K♧', 'Q♧', 'J♧', 'X♧', '9♧', '8♧', '7♧', '6♧', '5♧', '4♧', '3♧', '2♧', 'A♢', 'K♢', 'Q♢', 'J♢', 'X♢', '9♢', '8♢', '7♢', '6♢', '5♢', '4♢', '3♢', '2♢', 'A♤', 'K♤', 'Q♤', 'J♤', 'X♤', '9♤', '8♤', '7♤', '6♤', '5♤', '4♤', '3♤', '2♤',]
print("♣️Welcome to Poker!♣️")
print("I will be your dealer")
num_players = int(input("How many users will be playing?\n"))
while num_players < 2 or num_players > 4:
    print("There must be 2 players minimum and 4 maximum")
    num_players = int(input("How many users will be playing?\n"))
print(f"Ok... Preparing game for {num_players} players")
print("Shuffling cards...")
player_1_m = 500
player_2_m = 500
players_cards = []
player_1_c = random.sample(cards, 2)
players_cards += [player_1_c]
player_2_c = random.sample(cards, 2)
players_cards += [player_2_c]
print(f"Player 1 has {player_1_m}$")
print(f"Player 2 has {player_2_m}$")
cards.remove(player_1_c[0])
cards.remove(player_1_c[1])
cards.remove(player_2_c[0])
cards.remove(player_2_c[1])
total_players = ['player_1', 'player_2']
player_balances = [player_1_m, player_2_m]

if num_players == 3:
    player_3_m = 500
    player_3_c = random.sample(cards, 2)
    players_cards += [player_3_c]
    print(f"Player 3 has {player_3_m}$")
    cards.remove(player_3_c[0])
    cards.remove(player_3_c[1])
    total_players = ['player_1', 'player_2', 'player_3']
    player_balances = [player_1_m, player_2_m, player_3_m]
if num_players == 4:
    player_3_m = 500
    player_4_m = 500
    print(f"Player 3 has {player_3_m}$")
    print(f"Player 4 has {player_4_m}$")
    player_3_c = random.sample(cards, 2)
    player_4_c = random.sample(cards, 2)
    players_cards += [player_3_c]
    players_cards += [player_4_c]
    cards.remove(player_3_c[0])
    cards.remove(player_3_c[1])
    cards.remove(player_4_c[0])
    cards.remove(player_4_c[1])
    total_players = ['player_1', 'player_2', 'player_3', 'player_4']
    player_balances = [player_1_m, player_2_m, player_3_m, player_4_m]
num = 1
card = 0
print("Ok, I will show each player their cards starting with player 1.")
input("Enter 'a' when you are ready to see your cards.\n")
for i in range(num_players):
    print(f"Player {num}, I will show you your cards now")
    print("Other players look away now")
    for i in range(5, -1, -1):
        print(i)
        sleep(1)
    print(players_cards[card])
    yes_no = input("Enter something when you have memorized your cards.\n")
    clear_screen()
    num +=1
    card += 1
print("Now we can start playing!")
community_cards = []
community_cards = random.sample(cards, 3)
cards.remove(community_cards[0])
cards.remove(community_cards[1])
cards.remove(community_cards[2])
print("Here are your first 3 cards.")
print(community_cards)
num = 1
bet = 0
pot = 0
minimum_bet = 0
active_players = [True] * num_players

def get_new_bet(minimum_bet):
    bet = int(input("Enter an amount to bet:\n"))
    while bet < minimum_bet:
        print("That' not enough money!")
        print(f"The minimum amount is {minimum_bet}$.")
        bet = int(input("Enter an amount to bet: \n"))
    return bet

def menu(bet, pot, minimum_bet, locate_player):
    locate_player = int(input("What player are you? (Only enter a number)\n"))
    menu = input(f"Player {locate_player} what would you like to do?:\n1. Place a bet\n2. Look at your cards\n3. Tip the dealer😊\n4. Fold\n")
    if menu == "1":
    
        minimum_bet = get_new_bet(minimum_bet)
        if minimum_bet > bet:
             bet = minimum_bet
             
        pot += minimum_bet
        player_balances[locate_player - 1] -= minimum_bet
        print(f"You have {player_balances[locate_player - 1]}$ left.")
    if menu == "2":
        print(players_cards[locate_player - 1])
        input("Enter 'a' when you have memorized your cards:  \n")
        clear_screen()
        print("You must place a bet now.")
        minimum_bet = get_new_bet(minimum_bet)
        if minimum_bet > bet:
            bet = minimum_bet
        pot += minimum_bet
        
        player_balances[locate_player - 1] -= minimum_bet
        print(f"You have {player_balances[locate_player - 1]}$ left.")
    if menu == "3":
        print("How much would you like to tip the dealer?")
        tip = int(input("Enter an amount to tip:\n"))
        player_balances[locate_player - 1] -= tip
        print("You must place a bet now.")
        minimum_bet = get_new_bet(minimum_bet)
        pot += minimum_bet
        player_balances[locate_player - 1] -= minimum_bet
        print(f"You have {player_balances[locate_player - 1]}$ left.")
    if menu == '4':
        yes_no = input("Are you sure you would like to fold?\n")
        if yes_no in ['yes', 'Yes', 'YES', 'Yeah', 'yeah', 'yeh']:
            print(f"Player {locate_player} has left the game.")
            player_balances[locate_player - 1] = -1
    print("Next player's turn now!")
    return minimum_bet, pot


for i in range(num_players):
    if player_balances[i] != -1:
        minimum_bet, pot = menu(bet, pot, minimum_bet, i + 1)
if player_balances.count(-1) < num_players - 1:
    print("Now we will show the next card.")
    card = random.choice(cards)
    cards.remove(card)
    str(card)
    community_cards.append(card)
    print("Here is your next card:")
    print(community_cards)
else:
    print("There is only one player left, so the game is over.")
if player_balances.count(-1) < num_players - 1:
    print("Let's start the next round")
    minimum_bet = 0
    for i in range(num_players):
        if player_balances[i] != -1:
            minimum_bet, pot = menu(bet, pot, minimum_bet, i + 1)
    card1 = random.choice(cards)
    cards.remove(card1)
    str(card1)
    community_cards.append(card1)
    print("Here is your next card:")
    print(community_cards)
else:
    print("There is only one player left, so the game is over.")
if player_balances.count(-1) < num_players - 1:
    print("Let's start the final round!")
    minimum_bet = 0
    for i in range(num_players):
        if player_balances[i] != -1:
            minimum_bet, pot = menu(bet, pot, minimum_bet, i + 1)
    card2 = random.choice(cards)
    cards.remove(card2)
    str(card2)
    community_cards.append(card2)
    print("Here is your next card:")
    print(community_cards)
else:
    print("There is only one player left, so the game is over.")
print("GAME IS OVER")
print(f"Player 1's card were: {player_1_c}")
print(f"Player 2's card were: {player_2_c}")
if num_players >= 3:
    print(f"Player 3's card were: {player_3_c}")
if num_players == 4:
    print(f"Player 3's card were: {player_3_c}")
    print(f"Player 4's card were: {player_4_c}")
print("The community cards were:")
community_cardss = community_cards[0:5]
print(community_cardss)
print('')
print('')
print("Now we will determine the winner...")
print("Look amongst yourselves to see who has the best hand!")
winner = int(input("Who won? (Only enter a number)\n"))
while winner not in [1, 2, 3, 4]:
    print("Please enter a valid player number.")
    winner = int(input("Who won? (Only enter a number)\n"))
print(f"Congratulations Player {winner} you won {pot}$!")
winner_index = winner - 1
player_balances[winner_index] += pot