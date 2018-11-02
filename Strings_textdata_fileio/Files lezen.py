f = open("kaartnummers.txt")
lines = f.readlines()
for line in lines:
    kaart = line.split(',')[0]
    naam = line.split(',')[1].strip()   #split haalt de enter weg en andere onnodige tekens
    print(naam + " heeft kaart nummer " + kaart)
