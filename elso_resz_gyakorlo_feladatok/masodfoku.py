# Írj egy programot, amely bekéri egy másodfokú egyenlet 3 együtthatóját
# És kiírja a megoldásait.
# Figyelj arra, hogy lehetséges, hogy nincs megoldás, lehetséges, hogy csak 1 megoldás van
# lehetségos hogy 2 megoldás van
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

diszkrimináns = b**2 - 4 * a * c

if diszkrimináns < 0:
    print("Nincs valós megoldás")
if diszkrimináns == 0:
    print("1 megoldás létezik:", -b/(2*a))
if diszkrimináns > 0:
    print("2 megoldás létezik:")
    print("x1 =", (-b + diszkrimináns**0.5 )/(2*a))
    print("x2 =", (-b - diszkrimináns**0.5 )/(2*a))


    