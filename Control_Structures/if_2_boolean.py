leeftijd = int(input("Geeft je leeftijd:"))
paspoort = input("Heb je een nederlands paspoort")


def stemmen (leeftijd, paspoort):
    if leeftijd == 18 or leeftijd > 18 and paspoort == "Ja":
        print("Je mag stemmen")
    elif leeftijd < 18  or paspoort == "Nee":
        print("Jij mag niet stemmen")
stemmen(leeftijd, paspoort)