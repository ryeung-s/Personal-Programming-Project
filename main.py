### Personal Programming Project - Ryan Yeung
from operator import index
from os import system
import os
from time import sleep
import sys
from random import randint
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
    logo = """
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*#******
@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*#**++++
@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*#******
@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##+:-***
%#####**##########################################################%%#####################################################################################%%%%%%%%%%%%%#*****+
***########***************#######*****##########################%%#####################################******#########################################***###*****######******
+++*++:.+#**********************+++++++++++**********************#***++++++++++++****************+*+++************************+****+**********++++++++++++#*=************+==+
******+:=#**********+=============*******************************##*************************************************************************+=*++*********#+..+++===*********
******+:##******-=:.......-=-::..-+**********=+:......=+*********#***=*=-:....:-==**=+--------===-==*+***++======-****+*+++++===++*****=**+=--:.:::-+=+***##=********+++--=**
::--:-*%%#***+-:..........:-:....:+*********=*.........-********##*=:.:.........:+=*--................*-..........::+==-........::==::+::-::.............:-#+:***************
******#%%##*-=:........**--+*-...:+*********+=..........-*********-.......*##=::-+=*=**+.........+=-=-+**:.........:-*+**+....-**=*++:......:=**-........:-******+--=+*******
########%#++.........-+***##*+=::=+********+=.::........:=+******==.......-+#=***#=*##**-.......--****#**-...........=+**+-...=***+=:.......=+##+*:........-*************=--+
******-.+*+..........==******++==-=******+=-...:=.......:-:=*+++*-=.........:-=-+=-++*=+:........:++++**+:............--*=+::--**==........:=****=*..........=***************
######+:=*=.........==*******************+=....=*-........:-*****+-............:-+##*#+*:.......:=*#####*-...:..........--+..:=*++.......::-*#####+-..........***************
######=.=*=.........++*******************=....++**:.........=*****+=:............--#*#+*:......:--***##**:...:#=:........+=...-*=*.........-*#####=+.........-***************
==***#*:=++:........-+******************=:....-==...........:=****#*=--...........--**++:.......:=*******:...:=++.............:*#==........:******==.........:=*+************
#######-+#=+.........=+******+**-+*****=-...:=+*+===........:-****++==+:+:.........-*##+-.......-=*#####*==-:==#+*....:.......:##=*:........-*###+*..........:=+***++**+*****
%%%%%%*.=##++........:=+****++:..-++**-+...:==++**#+*.........-*##=:..-=**=:......--***+=........=****###=:..:=%%**+..........:#%#++........=-##*+-........:..+****=-+*==++==
%%%%%%@#%%%#=+.......::-+*+-.....=+-=+*....:=+%%%%++=:........:=+++:...-+++:......+=+==+-:.......=--+*=++=....===%%=*-........-#%%#++.........-++.........=-.-******++=+++=++
%%%%%%%%@%%%#*++-..............+*+*+*=-:.....-#%#%=*..........-=*=+-............:++#=*-............:+#=+........:*%%*++-:.....-+####*+*=:..............-++*#.:+*****####%%***
%%%%%%@%%%%%%%%#+=*+=-.:-=+**+=*###+***+==-=+-%%%%=%=====++++*###=*+===++====+*++***+**++=====+++==*+#-*+=-----==*%%%%+##*+==+*+%%%%%%#*+*#+=-:..-==++=+##%#+*%%##**@@@@@@#**
%@@@@@@+#%%%%%%%%%%##+---+#####%%#######%%%%%%%%%%%%%%%%%%%%%%##%%###########################################%%%%%%%%%%########%%%%%%%%%%%###******######%%#**%%###%@@@@@@@@@
@%%%%%%@@%%%####################################################%%%%%%%%%%############################################################################**#%%#**#%***%@@@@@@@@@
@@%%%%@%%%%%%##################################################%%%%######################***********###%################################################%%%+**#%***#@@@@@@@@@
@@@@@%%%**%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####%%%%%%%%%%%%%%##%#########################################################################%%=.=*#%##*#@@%@@%%##
CTRL-C to skip animation                          CTRL-C to skip animation                          CTRL-C to skip animation                        CTRL-C to skip animation                                
"""
    list_logo = logo.splitlines()
    counter = 40
    try:
        loop = 0
        while True:
            for index in range(len(list_logo[1])):
                
                buffer= []

                for line in list_logo:
                    #for i in range(len(line)):
                    if index <= (len(list_logo[1])) and index > 40:
                        buffer.append((" "*(index-counter)) + line[index-counter:index])
                        #print(index, counter, (index-counter),(index-160),len(list_logo[0])+40)
                        
                        
                    elif index <= 40:
                        buffer.append(line[:index] + (" "*(133)))

                        
                    #elif index <= 40 and loop == 0:
                        #buffer.append(line[:index])
                        
                        
                    
                frame = "\033[H" + "\n".join(buffer)
                sys.stdout.write(frame)
                sys.stdout.flush()
                sleep(0.016)
            loop += 1

        
    except KeyboardInterrupt:
        clear_screen()
        print("STOPPED")
        sleep(1)
        clear_screen()
        menu(subroutine=True, parameters=None)
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
def menu(subroutine, parameters):
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
        print("here")
        option = validinput(option=x, parameters="option in funcs", var1=funcs)
        clear_screen()
        funcs[option]()

    else:
        x = input()
        option = validinput(x, parameters)
        
        return option
def invalidinput():
    typeWriter("Invalid input")
    print("\n")
def validinput(option, parameters, var1):
    print("yo")
    print(option)
    
    while not eval(parameters):
        print(parameters)
        invalidinput()
        option = input()
    return option
def PlayBlackjack():
    global PlayingBJ
    PlayingBJ = True
    print("Playing Blackjack")
    pass
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
        menu(subroutine=True, parameters=None)
    pass
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
    if validinput(x, "x.isdigit() and int(x) >= 1 and int(x) <= 1000"):
        typing_speed = int(x)
        typeWriter("Typing speed changed to " + str(typing_speed))
        print("\n")
    else:
        invalidinput()
    return typing_speed
if __name__ == "__main__":
    display_logo()
    