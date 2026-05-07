

def InputPlainText():     
    PlainText = input("Please enter the plaintext: ")
    return PlainText

def InputCipherText():     
    CipherText = input("Please enter the ciphertext: ")
    return CipherText

def InputKey():  
    Key = input("Please enter the key value: ")
    return int(Key)

def Encrypt(PlainText, Key):
    CipherText = ""
    for CharPos in range(0, len(PlainText)):
        Character = PlainText[CharPos]
        CharacterCode = ord(Character)
        if  Character >= "A" and Character <= "Z":
            CharacterCode = CharacterCode + Key 
            if  CharacterCode > ord("Z"):
                CharacterCode = CharacterCode - 26
        CipherText = CipherText + chr(CharacterCode) 

    return CipherText

def LoadPlainText():    
    FileName = input("Enter filename: ")
    if len(FileName) > 0:
        FileHandle = open(FileName)  
        PlainText = FileHandle.read() 
        FileHandle.close() 
    else:
        PlainText = "Error"
 
    return PlainText

def Decrypt(CipherText, Key):
    PlainText = ""
    for CharPos in range(0, len(CipherText)):
        Character = CipherText[CharPos]
        CharacterCode = ord(Character)
        if  CharacterCode >= ord("A") and CharacterCode <= ord("Z"):
            CharacterCode = CharacterCode - Key
            if  CharacterCode < ord("A"):
                CharacterCode = CharacterCode + 26          
                
        PlainText = PlainText + chr(CharacterCode)

    return PlainText

def DisplayMenu():
    print()
    print("K Input Key")
    print("P Input Plaintext")
    print("C Input Ciphertext")
    print("L Load Plaintext")
    print("E Encrypt Plaintext")
    print("D Decrypt Ciphertext")
    print("Q Quit")
    print()

def Main():

    MenuOption = ""  

    while MenuOption != "Q":
        DisplayMenu()
        MenuOption = input("Enter Option > ").upper()
        if MenuOption == "K":
            Key = InputKey()
        elif MenuOption == "P":
            PlainText = InputPlainText()
        elif MenuOption == "C":
            CipherText = InputCipherText()
        elif MenuOption == "L":
            PlainText = LoadPlainText()
            print("Plaintext is : " + PlainText)
        elif MenuOption == "E":
            CipherText = Encrypt(PlainText, Key)
            print("Ciphertext is : " + CipherText)
        elif MenuOption == "D":
            PlainText = Decrypt(CipherText, Key)
            print("Plaintext is : " + PlainText)

Main()

