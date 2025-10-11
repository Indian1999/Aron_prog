import random

random.seed(50)
# 1. feladat: Generáljunk egy random listát
lista = []
for i in range(20):
    lista.append(random.randrange(-10, 21)) # -10 és 20 között (21 nincs benne)

print(lista)

# 2. feladat: Írjuk ki a lista elemeinek az átlagát

összeg = 0
for i in range(len(lista)): # i: 0-tól 19-ig
    #összeg += lista[i]
    összeg = összeg + lista[i]
print(f"A lista elemeinek az összege: {összeg}")
print(f"Az átlag: {összeg/len(lista)}")

# 3. feladat: Írjuk ki a legnagyobb számot
maximum = lista[0]
for i in range(1, len(lista)):
    if lista[i] > maximum:
        maximum = lista[i]
print(f"A legnagyobb elem: {maximum}")

# 4. feladat: Olvassunk be és mentsünk el egy mondatot.
mondat = input("Írj valamit:\n")
mondat = mondat.strip() #Az elejéről és a végéről törli a whitespace karaktereket
# Whitespace karakter: szóköz, enter, tabulátor...

while mondat != mondat.replace("  ", " "):
    mondat = mondat.replace("  ", " ")

# 5. feladat: Írjuk ki, hogy hány szóból áll a mondat
szóköz_számláló = 0
for i in range(len(mondat)):
    if mondat[i] == " ":
        szóköz_számláló += 1
print(f"Ez a mondat {szóköz_számláló+1} szóból áll.")



