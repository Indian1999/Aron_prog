# Írj egy programot ami bekér egy számot és eldönti, hogy a szám prím-e vagy sem
num = int(input("Kérek egy számot: "))

prim = True
for i in range(2, num):
    if num % i == 0:
        prim = False

if prim:
    print("Prím szám")
else:
    print("Nem prím szám")