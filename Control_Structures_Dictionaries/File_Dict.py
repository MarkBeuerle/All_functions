def ticker(a, b):
    """

    :param a: Requesting Ticker code or Company name
    :type a: str
    :param b: Query
    :type b: str
    :return:
    """
    dct = {}
    with open("tickers.txt", "r") as f:
        for l in f.read().splitlines():
            dct[l.split(":")[0]] = l.split(":")[1]
        f.close()

    for k, v in dct.items():
        if a == '1' and k == b:
            print(v)
        elif a == '2' and v == b:
            print(k)


while True:
    print("1. Ticker-code by company name\n2. Company name by Ticker-code")
    ticker(input("Your choice: "), input("Your query: "))
