from random import *


def throw():
    d1=randint(1,6)
    d2=randint(1, 6)

    if d1 != d2:
        print(str(d1)+" + "+str(d2)+" = "+str(d1+d2))
    elif d1 == d2:
        print(str(d1) + " + " + str(d2) + " = " + str(d1 + d2))
        d3=randint(1, 6)
        d4 = randint(1, 6)
        if d3 != d4:
            print(str(d3) + " + " + str(d4) + " = " + str(d3 + d4))
        elif d3 == d4:
            print(str(d3) + " + " + str(d4) + " = " + str(d3 + d4))
            d5 = randint(1, 6)
            d6 = randint(1, 6)
            if d5 != d6:
                print(str(d5) + " + " + str(d6) + " = " + str(d5 + d6))
            elif d5 == d6:
                print("Ga direct naar de gevangenis")
print(throw())