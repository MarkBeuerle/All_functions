arr = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk",
       "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven",
       "Weert", "Roermond", "Sittard", "Maastricht"]


def stations():
    print("You can choose from the following stations.")
    for station in arr:
        print(" - {0}".format(station))
    pass


def start():
    s = input("Where do you leave: ").capitalize()
    while s not in arr:
        print("This train doesn't go to, {0}!".format(s))
        s = input("Where do you leave: ").capitalize()
    return arr.index(s)


def end(a):
    s = input("What is your destination: ").capitalize()
    while s not in arr or arr.index(s) < a:
        print("This train doesn't go to, {0}!".format(s))
        s = input("Where do you leave: ").capitalize()
    return arr.index(s)


def recap():
    s1 = start()
    s2 = end(s1)

    print("You leave at, {0}, station #{1}.".format(arr[s1], s1 + 1))
    print("You arrive at, {0}, station #{1}.".format(arr[s2], s2 + 1))
    print("The distance is {0} stations.".format(s2 - s1))
    print("You ticket wil be €{0:.2f}\n".format((s2 - s1) * 5))
    print("You enter the train at {0}".format(arr[s1]))
    if s2 - s1 > 1:
        print("You'll pass the following stations")
        for n in range(s1 + 1, s2):
            print(" - {0}".format(arr[n]))
    print("You leave the train at {0}".format(arr[s2]))
    pass


stations()
recap()
