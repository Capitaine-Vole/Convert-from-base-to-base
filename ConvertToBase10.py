def convert(basefrom, num, out=True, ret=True):
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

convert(int(input("Enter the number of the base you want to convert in base 10 :\n")), int(input("Enter the number you want to convert in base 10 :\n")), ret=True) # we do convert(12, 10, False, False) if you dont want to have the message in the console and the same to get or not the number returned by the function

# little loop at the end to make the cmd windows not closing at the end of the program
run = True
while run:
    input("Push a key to stop the program")
    run = False