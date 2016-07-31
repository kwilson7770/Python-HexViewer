import sys

# If there is an argument passed to it, it will attempt to read it as a file path
if len(sys.argv) > 1:
    filePath = sys.argv[1]
else: # otherwise it will ask for the file path
    filePath = input("What is the file path? ")

# This is my custom function to convert the hexadecimal values into their ASCII characters.
# I don't include any control characters or spaces
def getASCIIChars(theHex):
    toReturn = ""
    for i in theHex.split():
        if int(i,16) >= 33 and int(i,16) <= 126:
            toReturn += chr(int(i,16))
        else:
            toReturn += "."
    return toReturn

# Since I call this twice, I made this a function to print the lines of data
def printHexData(hexNum, theHex):
    # if the length of the hex string is less than 48, pad the rest of it with null bytes (0's)
    while len(theHex) < 48:
        theHex += "00 "
    # tge :05X pads the hex counts on the far left with leading zeros (keeps things aligned better)
    print('{:05x}   {}  {}  {}'.format(hexNum,
                                       theHex[:int(len(theHex) / 2)],
                                       theHex[int(len(theHex) / 2):],
                                       getASCIIChars(theHex)))

# opens the file as read bytes (a python 3 thing)
with open(filePath, "rb") as fileReader:
    byte = " "  # bypass the first while condition check
    theHex = ""
    hexNum = 0
    while byte != b"":
        byte = fileReader.read(1) # reads 1 byte at a time, need to change this to 16 in the future
        if byte != b"": # if it is an empty byte, don't do anything
            theHex += byte.hex() + " " # add the byte and add a space after it
            # 1 byte = 2 hex chars + 1 space = 8*3*2 = 48
            if len(theHex) == 48:
                printHexData(hexNum, theHex)
                theHex = ""
                hexNum += 0x10 # add to the hex counter on the far left
if theHex != "":
    printHexData(hexNum, theHex) # print any characters missed by the above loop
