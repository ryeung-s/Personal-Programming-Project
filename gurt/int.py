FileHandle = open("1234.txt")  
PlainText = FileHandle.read() 

for line in PlainText:
    chr = ""
    for character in line:
         print(chr, end="")