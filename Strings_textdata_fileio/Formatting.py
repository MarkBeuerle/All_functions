def convert(celsius):
    return celsius * 1.8 + 32


def table():
    for x in range(-30, 41, 10):
        print("{:5} {:5}".format(convert(x), float(x)))


table()



