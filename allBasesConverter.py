#!/usr/bin/python3
# kirsten san nicolas


initBase=""
finBase=""


while((initBase != "hex") & (initBase != "binary") & (initBase != "octal") & (initBase != "decimal")):
    initBase = input("What base would you like to convert from? \n")
    initBase = initBase.lower()

while((finBase != "hex") & (finBase != "binary") & (finBase != "octal") & (finBase != "decimal")):
    finBase = input("What base would you like to convert to? \n")
    finBase = finBase.lower()

initVal = input("What value would you like to convert? \n")

#conversion to hex
if finBase == "hex":
    if initBase == "binary":
        finVal = hex(int(initVal,2))
    elif initBase == "octal":
        finVal = hex(int(initVal,8))
    else:
        finVal = hex(int(initVal))
#conversion to binary
elif finBase == "binary":
    if initBase == "hex":
        finVal = bin(int(initVal,16))
    elif initBase =="octal":
        finVal = bin(int(initVal,8))
    else:
        finVal = bin(int(initVal))
#converstion to octal
elif finBase == "octal":
    if initBase == "hex":
        finVal = oct(int(initVal,16))
    elif initBase == "binary":
        finVal = oct(int(initVal,2))
    else:
        finVal = oct(int(initVal))
#conversion to base10
else:
    if initBase == "hex":
        finVal = int(initVal,16)
    elif initBase == "octal":
        finVal = int(initVal,8)
    else:
        finVal = int(initVal,2)

print ("The " + initBase + " number " + initVal + " in " + finBase +
       " is " + str(finVal) + ".")
