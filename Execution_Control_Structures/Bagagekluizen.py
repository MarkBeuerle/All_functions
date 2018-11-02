import os

def toon_aantal_kluizen_vrij():
    count = len(open("kluizen.txt").readlines())
    aantal = 12 - count
    return(print("Het aantal kluisjes die op dit moment beschikbaar zijn is " + str(aantal) + "."))

def nieuwe_kluis():
    lijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    f = open("kluizen.txt","r")

    for file in f:
        for kluis in lijst:
            if int(file.split(';')[0]) == kluis:
                lijst.remove(kluis)

    if not lijst:
        print("Helaas, er zijn geen kluisjes beschikbaar. Probeer later opnieuw.")
    else:
        keuze = str(input("De kluisjes die momenteel vrij zijn: \n" + str(lijst) +
                          "\nVoer een beveiligingscode voor je kluisje in om het te ontvangen: "))

        a = open("kluizen.txt","a")
        if os.stat("kluizen.txt").st_size == 0:
            a.write (str (lijst[0]) + ';' + str (keuze))
        else:
            a.write ('\n' + str (lijst[0]) + ';' + str (keuze))
        print("U heeft kluisnummer " + str(lijst[0]) + '.')


def kluis_openen():
    kluisnummer = str(input("Voer uw kluisnummer in: "))
    kluiscode = str(input("Voer uw kluiscode in: "))

    f = open("kluizen.txt","r")
    for file in f:
        if kluisnummer == str(file.split(';')[0]) and kluiscode == str(file.split(';')[1]):
            print("Uw kluisje is open!")


def kluis_teruggeven():
    print ("Hello world!")

keuze = input("1: Ik wil weten hoeveel kluizen nog vrij zijn \n"
              "2: Ik wil een nieuwe kluis \n"
              "3: Ik wil even iets uit mijn kluis halen \n"
              "4: Ik geef mijn kluis terug \n"
              "Maak uw keuze: ")

if(int(keuze) == 1):
    toon_aantal_kluizen_vrij()

elif(int(keuze) == 2):
    nieuwe_kluis()

elif(int(keuze) == 3):
    kluis_openen()

elif(int(keuze) == 4):
    kluis_teruggeven()

else:
    print("Voer een correct getal in!")