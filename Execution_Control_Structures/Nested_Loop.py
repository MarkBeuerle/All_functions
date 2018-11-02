num=[1,2,3,4,5,6,7,8,9,10]
def alle_tafels(num):
    for x in num:
        for y in num:
            z=x*y
            print(x," x ",y," = ",z)
alle_tafels(num)