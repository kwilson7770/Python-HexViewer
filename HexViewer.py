filePath = input("What is the file path? ")

def getASCIIChars(theHex):
    toReturn = ""
    for i in theHex.split():
        if int(i,16) >= 33 and int(i,16) <= 126:
            toReturn += chr(int(i,16))
        else:
            toReturn += "."
    return toReturn


def printHexData(hexNum, theHex):
    while len(theHex) < 48:
        theHex += "00 "
    print('{:04x}   {}  {}  {}'.format(hexNum,
                                       theHex[:int(len(theHex) / 2)],
                                       theHex[int(len(theHex) / 2):],
                                       getASCIIChars(theHex)))

with open(filePath, "rb") as fileReader:
    byte = " "  # bypass the first while check
    theHex = ""
    hexNum = 0
    while byte != b"":
        byte = fileReader.read(1)
        if byte != b"":
            theHex += byte.hex() + " "
            # 1 byte = 2 hex chars + 1 space = 8*3*2 = 48
            if len(theHex) == 48:
                printHexData(hexNum, theHex)
                theHex = ""
                hexNum += 0x10
if theHex != "":
    printHexData(hexNum, theHex)
