
def gemiddelde():
    zin = input("Schrijf hier een zin : ")
    lijst = zin.split()
    totaal = 0
    for woord in lijst:

        totaal = len(woord) + totaal
    x = len(lijst)
    gem = totaal / x

    return gem



gem = gemiddelde()

print (gem)
