import argparse

# This is my custom function to convert the hexadecimal values into their ASCII characters.
# I don't include any control characters or spaces
def getASCIIChars(rawHex):
    toReturn = ""

    for i in rawHex.split():
        exclamationPoint = 33
        tilde = 126
        if int(i, 16) >= exclamationPoint and int(i, 16) <= tilde:
            toReturn += chr(int(i, 16))
        else:
            toReturn += "."
    return toReturn

# Since I call this twice, I made this a function to print the lines of data
def printHexData(hexNum, rawHex):
    hexStr = ""

    for i in range(len(rawHex)):
        if i % 2 == 0:
            hexStr += rawHex[i:i + 2] + " "  # add the byte and add a space after it
        if (i + 1) % 16 == 0 and i != 0: # add an extra two spaces in between the sets of bytes for a visual separation
            hexStr += "  "

    # the {:05x} pads the hex number on the far left with leading zeros (keeps things aligned better)
    print('{:05x}   {}{}'.format(hexNum, hexStr, getASCIIChars(hexStr)))

def readFile():
    # opens the file as read bytes (a python 3 thing)
    with open(args.filePath, "rb") as fileReader:
        rawHex = ""
        hexNum = 0
        while len(rawHex) == numOfBytes * 2 or hexNum == 0: # if it is smaller than it should be, you reached the end of the file
            rawHex = fileReader.read(numOfBytes).hex()
            if len(rawHex) == numOfBytes * 2: # if it is smaller than it should be, you reached the end of the file
                printHexData(hexNum, rawHex)
                hexNum += numOfBytes
    if rawHex != "":
        # if the length of the hex string is less than numOfBytes * 2, pad the rest of it with null bytes
        while len(rawHex) < numOfBytes * 2:
            rawHex += "00"
        printHexData(hexNum, rawHex) # print any characters missed by the above loop

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Displays the file in hexadecimal and ASCII format')
    parser.add_argument('filePath')
    parser.add_argument('-n', '--narrow', action='store_true', help='Outputs the files information in a narrow format (8 bytes)',
                        required=False)
    parser.add_argument('-w', '--wide', action='store_true', help='Outputs the files information in a wide format (32 bytes)',
                        required=False)
    args = parser.parse_args()

    if bool(args.narrow) and bool(args.wide):
        parser.error('-n/--narrow and -w/--wide cannot be used at the same time')

    numOfBytes = 16 # default size
    if args.narrow is True:
        numOfBytes = 8
    elif args.wide is True:
        numOfBytes = 32
    readFile()
