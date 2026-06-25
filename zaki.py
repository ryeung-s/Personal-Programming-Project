## Personal Programming Project - Alvin Lee

from colorama import Fore, Back, Style ## pip install colorama
from time import sleep
import random
import copy
from freedictionaryapi.clients.sync_client import DictionaryApiClient
client = DictionaryApiClient()
import os

# pip install python-freeDictionaryAPI
# pip install httpx

# hi

# constants and configurations

# letters frequency
letter_freq = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2, "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1, " ": 2}

# avaliables letters to give
aval_letters = []
for letter in letter_freq:
    for i in range(letter_freq[letter]):
        aval_letters.append(letter)

# letter points
points = {1: ["E", "A", "I", "O", "N", "R", "T", "L", "S", "U"],
         2: ["D", "G"],
         3: ["B", "C", "M", "P"],
         4: ["F", "H", "V", "W", "Y"],
         5: ["K"],
         8: ["J", "X"],
         10: ["Q", "Z"]}

used_positions = []
used_letter_and_positions = []


def clear_screen():
    # 'nt' is the internal name for Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_letters(letters, n):
    wordlists = [[] for _ in range(n)]
    for i in range(n):
        word = wordlists[i]
        for i in range(7):
            random.shuffle(letters)
            l = letters.pop()
            word.append(l)

    return wordlists
        
def create_board():
    board = []
    for i in range(15):
        board.append("-"*61)
        board.append("|   "*15 + "|")
    board.append("-"*61)

    return board

def display_board(b):
    # displays board with letter and numbers
    disboard = []
    disboard.append("     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O")
    for row in range(len(b)):
        if row % 2 == 1:
            front = str((row+1)//2)
            if len(front) == 1:
                front += "  "
            else:
                front += " "
        else:
            front = "   "

        disboard.append(front + b[row]) ### play lankybox neighbourhood roleplay

    for row in disboard:
        print(row)

def choose_first_player():
    pass

def update_letters(letters, p):
    n = 7 - len(p)
    for i in range(n):
        random.shuffle(letters)
        l = letters.pop()
        p.append(l)
    return p

def is_connected_to_word(positions):
        if not used_positions:
            return True
        for pos in positions:
            if pos in used_positions:
                return True
            col, row = position(pos)
            row = int(row)
            col_ord = ord(col)
            neighbors = [
                f"{chr(col_ord - 1)}{row}",
                f"{chr(col_ord + 1)}{row}",
                f"{col}{row - 1}",
                f"{col}{row + 1}"
            ]
            for neighbor in neighbors:
                if neighbor in used_positions:
                    return True
        return False

def position(s):
    col = s[0]
    row = int(s[1:])
    return col, row

def enter_letters(words, n, first, board):
    print("Turn: Player", n)
    tempwords = words.copy()
    createword = []
    temporary_position = []
    flag = True

    if first:
        print("Place one letter in the centre position H8\n")

    while flag and len(words) > 0:
        

        print("Your letters:", ", ".join(word for word in tempwords))

        pp = False
        while not pp:

            line = input("Enter placement:\n> ").strip()
            print("\n")
            if line == "":
                if not createword:
                    print(Back.RED + "You must enter a letter." + Style.RESET_ALL)
                    continue
                flag = False
                return createword, tempwords

            place = line.split()
            if len(place) < 2:
                print("Enter letter and position (e.g. J B1)")
                continue

            let = place[0].upper()
            cord = place[1].upper()
            use_existing = len(place) >= 3

            if len(cord) < 2:
                print("Enter a valid position (e.g. B1)")
                continue

            x = cord[0]
            y = cord[1:]
            if x not in "ABCDEFGHIJKLMNO" or not y.isdigit() or not (1 <= int(y) <= 15):
                print(Back.RED + f"{cord} is not a valid position!\n" + Style.RESET_ALL)
                continue

            if use_existing:
                if cord not in used_positions:
                    print(Back.RED + f"{cord} isn't being used!" + Style.RESET_ALL + "\n")
                    continue
                letter = find_letter_from_pos(cord)
                if letter != let:
                    print(Back.RED + f"{letter} is in position {cord}!" + Style.RESET_ALL)
                    continue
                else:
                    print(f"{letter} successfully found in {cord}")
            else:
                if cord in used_positions:
                    print(Back.RED + f"{cord} is in use!" + Style.RESET_ALL + "\n")
                    continue
                if let not in tempwords:
                    print(Back.RED + "You don't have this letter!" + Style.RESET_ALL + "\n")
                    continue
                tempwords.remove(let)

            createword.append([let, cord])
            temporary_position.append(cord)


            board_copy = copy.deepcopy(board)

            board_copy = add_to_board(createword, board_copy)

            display_board(board_copy)
            
            pp = True

            con = input("Continue? (y/n): ").strip().lower()
            print("\n")
            if con == "n":
                flag = False
                if first and "H8" not in temporary_position:
                    print("First player must place one letter in middle position H8 during the first turn")
                    tempwords = words.copy()
                    createword = []
                    temporary_position = []
                    flag = True
                    sleep(1)
                    print("\n")
                    display_board(board)

                    break

                if not first and not is_connected_to_word(temporary_position):
                    print(Back.RED + "Your words must be connected to others on the board!" + Style.RESET_ALL)
                    tempwords = words.copy()
                    createword = []
                    temporary_position = []
                    flag = True
                    sleep(1)
                    print("\n")
                    display_board(board)

                    break

                return createword, tempwords

    return createword, tempwords


def check_valid(letters): # input [['E', 'B1'], ['T', 'C1'], ['I', 'D1'], ['D', 'E1’]]
    cord = letters[0][1]
    ref_column = cord[0] # letter
    ref_row = cord[1:] # number
    same_row = True
    same_column = True

    for pos in letters:
        if ref_column != pos[1][0]: # row
            same_row = False
        if ref_row != pos[1][1:]: # column
            same_column = False

    if same_row or same_column:
        if same_row:
            return True, True
        else:
            return True, False
    else:
        print(Back.RED + "Word positions not valid! Try again" + Style.RESET_ALL)
        return False, False

def check_adjacent(words, ori):
    lettter_list = []
    valid = True

    for set in words:
        pos = set[1]

        if ori:
            lettter_list.append(pos[1:])
        else:
            lettter_list.append(pos[0])


    for i in range(len(lettter_list)):
        if ori:
            x = int(lettter_list[i]) ## numbers increase
            y = i + int(lettter_list[0])
        else:
            x = ord(lettter_list[i])
            y = i + ord(lettter_list[0])  ## letters increase

        if x != y:
            valid = False
                
    return valid

def position(s):
    col = s[0]
    row = int(s[1:])
    return col, row


def check_word(ori, words): ## bubble sort
    n = len(words)
    for i in range(n):
        for i in range(n - 1):
            c1, r1 = position(words[i][1])
            c2, r2 = position(words[i + 1][1])

            if ori:  # same column -> sort by row number
                if r1 > r2:
                    words[i], words[i+1] = words[i+1], words[i]
            else:    # same row -> sort by column letter
                if c1 > c2:
                    words[i], words[i+1] = words[i+1], words[i]

    valid = check_adjacent(words, ori)
    if not valid:
        print(Back.RED + "Letters are not adjacent" + Style.RESET_ALL)
    return valid


def check_possible_word(words):
    final_word = ""
    for let in words:
        final_word += let[0][0]
    try:
        word = client.fetch_word(final_word)
    except:
        return False, final_word, words
    else:
        return True, final_word, words
    

def add_to_board(pos, board):
    for set in pos:
        l = set[1][0]
        n = set[1][1:]

        target_index = 2 + (ord(l) - ord("A")) * 4
        
        row = board[2*int(n)-1]
        
        row = row[:target_index] + set[0] + row[target_index+1:]
        
        board[2*int(n)-1] = row
        
    return board

def player_first_turn():
    pass

def display_score(score):
    print("Score")
    for i in range(len(score)):
        print(f"Player {i+1}: {score[i]}")
    print("\n")

def introduction():
    print("WELCOME TO SCRABBLE!!")

    while True:
        try:
            players = int(input("Enter number of players (1-4): "))
            if players <= 4 and players >= 1:
                break
            else:
                print("Please enter valid number of numbers from 1-4")
        except ValueError:
            print("Please enter valid number of numbers from 1-4")

    sleep(1)

    clear_screen()

    print("\nEnter turn with letter and position of letter (e.g. J B1)")
    print("Enter in this format to extend a word with a letter already on the board (J B1 x)")
    print("Press enter to stop entering letters\n")

    # sleep(3)

    # print("Colour multiplier:")
    # print(Back.RED + "-" + Style.RESET_ALL + " 3x word score")
    # print(Back.YELLOW + "-" + Style.RESET_ALL + " 2x word score")
    # print(Back.BLUE + "-" + Style.RESET_ALL + " 3x letter score")
    # print(Back.CYAN + "-" + Style.RESET_ALL + " 2x letter score\n")

    sleep(3)
    
    return players

def calculate_score(word, p, s):
    score = s
    for let in word:
        for i in p:
            if let in p[i]:
                score += i
    return score

def create_variables(n):
    score = [0 for _ in range(n)]
    round = 1
    count = 1

    return score, round, count

def find_letter_from_pos(cord):
    for i in range(len(used_letter_and_positions)):
        set = used_letter_and_positions[i]
        if set[1] == cord:
            return set[0]

def taken_positions(wordslist):
    for set in wordslist:
        used_positions.append(set[1])

def store_letter_and_positions(wordslist):
    for set in wordslist:
        used_letter_and_positions.append(set)


ascii_logo = """⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⢀⣠⣤⣄⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣀⣤⣤⣄⣀⡀⡀⡀⡀⡀⡀⡀⣀⣀⣀⣀⣀⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢀⣀⣀⣀⣀⣀⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣀⣀⣀⣀⣀⣀⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣀⣀⣀⣀⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⣾⠋⡀⡀⡀⢹⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⢀⣾⠟⠁⡀⡀⡀⠈⣿⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⠈⠻⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢰⣿⡆⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⠙⣿⡄⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡇⡀⡀⠈⠻⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⡀⣿⡀⡀⡀⡀⡀
⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⠟⡀⡀⡀⡀⡀⡀⡀⡀⢠⣿⠃⡀⡀⡀⡀⡀⡀⣿⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡏⠸⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⡀⣿⡇⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⡀⠿⡀⡀⡀⡀⡀
⡀⡀⡀⡀⠈⣿⣦⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡟⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⢀⣿⠃⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣸⡀⡀⣿⣇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⢀⣿⠋⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⣠⣿⠁⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⣶⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⠛⢿⣿⣶⣄⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⣤⣤⣤⣶⠛⠁⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡏⡀⡀⠘⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⠶⠶⠿⣭⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡷⠶⠶⠿⣥⣀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⠶⠶⠶⣿⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⠙⢿⣷⡀⡀⡀⡀⡀⡀⡀⡀⣿⣇⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⠙⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣼⣤⣤⣤⣤⣿⣧⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⠙⣿⡄⡀⡀⡀⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⡀⢻⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⣿⡀⡀⡀⡀⡀⡀⡀
⡀⡀⡀⡀⣤⡀⡀⡀⡀⡀⡀⣿⡆⡀⡀⡀⡀⡀⡀⡀⠹⣿⡀⡀⡀⡀⡀⡀⡀⣰⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⢿⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⢀⠇⡀⡀⡀⡀⠘⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⡀⢠⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⢠⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⡀⢠⡀⡀⡀⡀⡀
⡀⡀⡀⡀⣿⡀⡀⡀⡀⡀⣠⡿⡀⡀⡀⡀⡀⡀⡀⡀⡀⠹⣿⣀⡀⡀⡀⡀⡀⣿⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⠘⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⣾⡀⡀⡀⡀⡀⡀⢿⣷⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⣴⡿⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⡇⡀⡀⡀⢀⣾⠟⡀⡀⡀⡀⡀⡀⡀⡀⡀⢸⣿⡀⡀⡀⡀⡀⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⣿⣿⡀⡀⡀⡀⡀⣾⡀⡀⡀⡀⡀
⡀⡀⡀⡀⠈⠛⠳⠶⠶⠛⠉⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠉⠛⠶⠶⠶⠛⠉⡀⡀⡀⡀⡀⡀⠛⠛⠛⠛⠛⡀⡀⡀⠙⠛⠛⡀⡀⡀⡀⡀⠘⠛⠛⠛⠂⡀⡀⠐⠛⠛⠛⠛⠛⡀⡀⡀⡀⡀⠘⠛⠛⠛⠛⠛⠛⠋⠁⡀⡀⡀⡀⡀⡀⡀⡀⠛⠛⠛⠛⠛⠛⠛⠉⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⠛⠛⠛⠛⠛⠛⠛⠛⠛⡀⡀⡀⡀⡀⡀⡀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⡀⡀⡀⡀⡀
⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
""".splitlines()

def logo_animation(logo):
    word_list = []
    for i in range(8):
        letter_list = []
        for line in logo:
            pos = i * 17
            letter_list.append(line[pos:pos+16])
        word_list.append(letter_list)

    master_canvas = [[" " * 16 for _ in range(8)] for _ in range(11)]

    for index, letter in enumerate(word_list):
        x = 1
        for step in range(11):

            temp_frame = [" " * 16 for _ in range(11)]
            
            for i in range(step + 1):
                temp_frame[i] = letter[i + (10 - step)]
                
            for r in range(11):
                master_canvas[r][index] = temp_frame[r]
                
            clear_screen()
            for row in master_canvas:
                print(" ".join(row))
                
            sleep(0.05/x)
            x = x * 1.4

def main():

    logo_animation(ascii_logo)
    print()

    sleep(0.5)
    plr_num = introduction()
    board = create_board()
    plr_letters = create_letters(aval_letters, plr_num)
    score, round, count = create_variables(plr_num)

    # print(score)

    while len(aval_letters) > 0:

        p_letters = plr_letters[count-1]
        p_score = score[count-1]

        display_board(board)
        display_score(score)

        sleep(1)

        print("Round:", round)
        valid, ori = False, False ## valid determines whether it is valid, ori detemines orientation of word
        while not (valid or ori):
            first_turn = False
            if round == 1 and count == 1:
                first_turn = True
            letter_pos, wordsleft = enter_letters(p_letters, count, first_turn, board)
            valid, ori = check_valid(letter_pos) ## checks if entered positions are valid
            if not valid:
                continue

            valid1 = check_word(ori, letter_pos) ## checks if adjacent
            # print("v1", valid1)

            valid2, word, letter_pos = check_possible_word(letter_pos)
            # print("v2", valid2)

            if valid1 and valid2:
                taken_positions(letter_pos)
                store_letter_and_positions(letter_pos)
                # print(used_positions)
                board = add_to_board(letter_pos, board)
                display_board(board)
                print("Word found: "+ word, "\n")
                sleep(2)
            else:
                if not valid1:
                    print(Back.RED + f"The word '{word}' was not found" + Style.RESET_ALL)
                
                print()
                display_board(board)
                
                valid, ori = False, False

        score[count-1] = calculate_score(word, points, p_score)
        plr_letters[count-1] = update_letters(aval_letters, wordsleft)

        if count == plr_num: ## check if all players have gone
            count = 1
            round += 1
        else:
            count += 1

    high_score = max(score)
    position = score.index(high_score)
    print(f"Player {position + 1} won with the score of {high_score}!")

# # x = False
# y = [['E', 'B1'], ['T', 'C1'], ['I', 'D1'], ['D', 'E1']]
# # a, b = check_word(x, y)
# # print(a, b) 

main()