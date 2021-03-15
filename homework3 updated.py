def price(orange, apple, lemon):
    if int(orange) == int(apple) or int(orange) == int(lemon) or int(lemon) == int(apple) or int(orange) == int(lemon):
        print(True)
    else:
        print(False)

price(5, 7, 6)

price(7, 8, 8)

price(7, 8, 7)

price(5, 5, 7)

price(10, 10, 10)

price(5, "5", 5)
