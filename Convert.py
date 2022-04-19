from math import log

#class Conversion:

def convertFromBase10(num, base, out=True, ret=True):
    num = int(num)
    base = int(base)
    numToChar = {i:"0123456789ABCDEF"[i] for i in range(16)}
    power = int(log(num, base))
    converted = ""
    for pow in range(power, -1, -1):
        converted += numToChar[num // (base**pow)]
        num %= base**pow

    if out == True:
        print(str(converted) + " is the number " + str(num) + " of the base 10 in the base" + str(base))
    if ret == True:
        return converted

def convertToBase10(basefrom, num, out=True, ret=True):
    if basefrom == 10:
        print("Its not the program to calcul from base 10, sorry")
        print(str(num) + " in base 10 is equal to " + str(num) + " in base 10 ... amazing not. lmao")
        return
    num = int(num)
    numstr = str(num)
    basefrom = int(basefrom)
    lenn = int(len(str(num)))
    littlelist = []
    finallist = 0
    for i in range(lenn):
        current = int(numstr[-(i+1)]) * (basefrom**i)
        littlelist.append(current)
    for i in range(0, len(littlelist)):
        finallist = finallist + littlelist[i]

    if out == True:
        print(str(finallist) + " is the number " + numstr + " of the base " + str(basefrom) + " in base 10")
    if ret == True:
        return(finallist)

def convertloop(state=True):
    if state == True:
        run = True
        while run:
            input("Push a key to stop the program")
            run = False