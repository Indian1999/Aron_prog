# Írj egy programot, ami bekéri egy derékszögű háromszög, 2 befogójának a hosszát

a = int(input("a:"))
b = int(input("b:"))
# a, és kiírja az átfogó hoszsát

c = ( a**2 + b**2 )**0.5
print("Átfogó:", c)
# b, kerületet
print("Kerület:", a+b+c)

# c, területet
print("Terület:", a*b*0.5)