lijst = []
lijst4 =[]
lijst = eval(input("Geeft lijst met minimaal 10 strings:"))
for woord in lijst:
    if len(woord) == 4:
        lijst4.append(woord)
print(lijst4)


