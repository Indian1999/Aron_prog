import os
class Konyv:
    def __init__(self, cim, szerzo, kiadas_eve, oldalszam):
        self.cim = cim
        self.szerzo = szerzo
        self.kiadas_eve = kiadas_eve
        self.oldalszam = oldalszam

    def hosszu(self):
        if self.oldalszam >= 300:
            return "hosszú"
        else:
            return "rövid"

konyvek = []
path = os.path.join(os.path.dirname(__file__), "konyvek-adatok.txt")
with open(path, "r", encoding="utf-8") as forras:
    sorok = forras.readlines()
    for i in range(1, len(sorok)):
        sor = sorok[i] #"Egri csillagok;Gárdonyi Géza;1901;420\n"
        sor = sor.strip().split(";") # ['Egri csillagok', 'Gárdonyi Géza', '1901', '420']
        konyv = Konyv(sor[0], sor[1], int(sor[2]), int(sor[3]))    
        konyvek.append(konyv)

# 1. Feladat: Könyvek átlagos oldalszáma

összeg = 0
for i in range(len(konyvek)):
    összeg += konyvek[i].oldalszam
atlag = összeg / len(konyvek)
print(f"A könyvek átlagos oldalszáma: {round(atlag, 1)}")

# 2. Feladat: Legrégebbi könyv címe és szerzője

legregebbi = 0
for i in range(len(konyvek)):
    if konyvek[i].kiadas_eve < konyvek[legregebbi].kiadas_eve:
        legregebbi = i

print(f"A legrégebbi könyv: {konyvek[legregebbi].cim}, {konyvek[legregebbi].szerzo}")

# 3. Feladat: Hány könyv jelent meg a bekért évszám óta?

evszam = int(input("Adj meg egy évszámot: "))
szamlalo = 0
for i in range(len(konyvek)):
    if konyvek[i].kiadas_eve >= evszam:
        szamlalo += 1
print(f"{evszam}-tól kezdve {szamlalo} könyv jelent meg.")


# 5. Feladat: regi-konyvek.txt-be a 2000 előtti könyvek

path = os.path.join(os.path.dirname(__file__), "regi-konyvek.txt")







with open(path, "w", encoding="utf-8") as f:
    for i in range(len(konyvek)):
        if konyvek[i].kiadas_eve <= 2000:
            f.write(f"{konyvek[i].cim} ({konyvek[i].hosszu()})\n")
