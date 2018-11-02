numlist = []
num = int(input("Geef een getal: "))

while not num == 0:
    numlist.append(num)
    num = int(input("Geef een getal: "))

print("Er zijn {0} getallen ingevoerd, de som is: {1}".format(len(numlist), sum(numlist)))
