string = input("Geef een string van 4 charakters: ")

while not len(string) == 4:
    print("string heeft " + str(len(string)) + " letters")
    string = input("Geef een string van 4 charakters: ")
print("Inlezen van correcte string "+string+" is geslaagd")