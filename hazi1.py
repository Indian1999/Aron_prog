import random
#1. feladat:
#Generálj egy random számokból álló 100 elemű listát melyek elemei [-20, 100] tartományban lévő számok

szamok = random.sample(range(-20, 101), 100)
print(szamok)
print(type(szamok)) # <class 'list'>

#2. feladat:
#Kérj be egy egész számot a felhasználótól és döntsd el, hogy a megadott szám szerepel-e a listában, az eredményt jelenítsd meg. Ha a program már megtalálta az adott számot, akkor állítsd le a ciklust.

#szam = int(input("Adj meg egy számot: "))
szam = 7
találat = False

for i in range(0, len(szamok)): # i = 0, 1, 2, 3, ..., 98, 99
    if szamok[i] == szam:
        találat = True
        break  # Ha ez a kód lefut, kilép az aktuális ciklusból

if találat:
    print("Benne van a listában")
else:
    print("Nincs ilyen szám a listában")


#3. feladat:
#Határozzuk meg, hogy hány db 7-tel osztható szám szerepel a listában (A 0-t nem tekintjük jelen esetben 7-tel oszthatónak, ezért azt ne számoljuk)

szamlalo = 0
for i in range(0, len(szamok)): # i = 0, 1, 2, 3, ..., 99
    if szamok[i] % 7 == 0 and szamok[i] != 0:
        szamlalo += 1

print(f"A listában {szamlalo} db 7-tel osztható szám szerepel.")


#4. feladat:
#Írd ki a kimenetre a negatív számok összegét!


#5. feladat:
#Írjuk ki, hogy melyik szám a legkisebb és, hogy a lista hanyadik indexén található (ha többször is szerepel, akkor a legkisebb indexet)

min_index = 0
for i in range(0, len(szamok)):
    if szamok[i] < szamok[min_index]:
        min_index = i

print(f"A legkisebb szám a listában a {szamok[min_index]}, a {min_index}. indexen található.")

#6. feladat:
#Határozd meg és írd ki outputra a lista MÁSODIK legnagyobb értékét.