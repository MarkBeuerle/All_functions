def names(a):
    """

    :param a: Name
    :type a: str
    :return:
    """
    obj = {}
    while len(a) != 0:
        if a in obj:
            obj[a] += 1
        else:
            obj[a] = 1
        a = input("Give me a name: ")

    for k, v in obj.items():
        print(
            "There {0} {1} {2} with the name: {3}".format(
                ("are" if int(v) > 1 else "is"),
                v,
                ("people" if int(v) > 1 else "person"),
                k
            )
        )


names(input("Give me a name: "))
