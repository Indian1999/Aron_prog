# Olvassuk be egy háromszög 3 oldalának a hosszát
# Dönstük el, hogy derékszögű-e a háromszög

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
    print("Derékszögű")
else:
    print("Nem derékszögű")