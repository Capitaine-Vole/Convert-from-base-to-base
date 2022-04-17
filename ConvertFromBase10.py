from math import log

def convertFromBase10(num, base):
    num = int(num)
    base = int(base)
    numToChar = {i:"0123456789ABCDEF"[i] for i in range(16)}
    power = int(log(num, base))
    converted = ""
    for pow in range(power, -1, -1):
        converted += numToChar[num // (base**pow)]
        num %= base**pow
 
    return converted

print(convertFromBase10(int(input("Entrez le nombre que vous voulez convertir :\n")), int(input("Entrez la base en la quelle cous voulez convertir votre nombre :\n"))))