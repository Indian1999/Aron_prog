class Film:
    def __init__(self, cim, mufaj, hossz, jegyar, telepules):
        self.cim = cim
        self.mufaj = mufaj
        self.hossz = hossz
        self.jegyar = jegyar
        self.telepules = telepules

    def aremeles(self):
        return self.jegyar*1.2

filmek = []

with open("mozi-adatok.txt", "r", encoding="utf-8") as f:
    sorok = f.readlines()
    for sor in sorok[1:]:
        cim, mufaj, hossz, jegyar, telepules = sor.strip().split(";")
        filmek.append(Film(cim, mufaj, int(hossz), int(jegyar), telepules))

# 1. feladat: Filmhosszok összege

osszeg = 0
for film in filmek:
    osszeg += film.hossz

print(f"A filmek teljes hossza: {osszeg} perc")


# 4. feladat:

film_cim = input("Add meg egy film címét: ")
talalat = False
for film in filmek:
    if film.cim == film_cim:
        talalat = True
        print("Ennél a filmnél az áremelés után a jegyár: ", film.aremeles())

if talalat == False:
    print("Nincs ilyen című film!")