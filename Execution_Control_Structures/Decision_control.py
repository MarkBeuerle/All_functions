def seizoen():
    maand = input("Welke maand is het?:")
    if maand == "December" or maand == "Januari" or maand == "Februari" :
          print("Het is winter!")
    elif maand =="Maart" or maand == "April" or maand == "Mei" :
        print("Het is lente!")
    elif maand == "Juni" or maand == "Juli" or maand == "Augustus":
        print("Het is zomer!")
    elif maand == "September" or maand == "November" or maand == "Oktober":
        print("Het is herfst!")
    else:
        print("deze maand ken ik niet")
seizoen()