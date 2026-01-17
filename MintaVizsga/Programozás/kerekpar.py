kerekpar = []
with open("MintaVizsga/Programozás/kerekpar-adatok.txt", "r", encoding="utf-8") as forras:
    next(forras)
    for i in forras:
        adat = i.strip().split(";")
        k = {
            "nev": adat[0],
            "telepules": adat[1],
            "szerviz_ar": int(adat[2]) 
        }
        kerekpar.append(k)

# 1. feladat: Boltok száma:
print("Kerékpárboltok száma:", len(kerekpar))

# 2. feladat: Legdrágább szervíz neve és ára
legdragabb = 0
for i in range(len(kerekpar)):
    if kerekpar[i]["szerviz_ar"] > kerekpar[legdragabb]["szerviz_ar"]:
        legdragabb = i
print(f"A legdrágább szerviz a {kerekpar[legdragabb]['nev']} boltban van, {kerekpar[legdragabb]['szerviz_ar']} Ft.")

# 3. feladat: 

def akcio(szerviz_ar):
    return round(szerviz_ar * 0.8)

# 4. feladat:
bolt = input("Adj meg egy bolt nevet: ")

talalat = None
for item in kerekpar:
    if item["nev"] == bolt:
        talalat = item

if talalat != None:
    print(f"Ennél a boltnál akciósan {akcio(talalat['szerviz_ar'])} Ft lenne a szerviz.")
else:
    print("Nincs ilyen bolt!")

# 5. feladat:

with open("MintaVizsga/Programozás/kerekpar-export.txt", "w", encoding="utf-8") as f:
    for i in kerekpar:
        if i["telepules"] == "Budapest":
            f.write(i["nev"])
            f.write("\n")
