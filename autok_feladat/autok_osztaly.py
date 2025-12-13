class Auto:
    def __init__(self, rendszam, marka, loero):
        self.rendszam = rendszam # "ABC-123"
        self.marka = marka
        self.loero = loero

    def __str__(self):
        return f"{self.rendszam} {self.marka} {self.loero}"
    
    def rendszam_nagyobb_e(self):
        rendszam_szam = int(self.rendszam[4:])
        if rendszam_szam > self.loero:
            return True
        else:
            return False

autok = []
with open("autok_feladat/autok.csv", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip().split(";") # ['PQN-434', 'Lamborghini', '650']
        auto = Auto(line[0], line[1], int(line[2]))
        autok.append(auto)

# Írjuk ki az autok átlagos lóerejét!

összeg = 0
for item in autok:
    összeg = összeg + item.loero
atlag = összeg / len(autok)
print(f"Az autók átlagos lóereje: {round(atlag ,2)}")

# Hány lamborghini szerepel az adathalmazban?
lambo_szamlalo = 0
for item in autok:
    if item.marka == "Lamborghini":
        lambo_szamlalo += 1

print(f"Lambok száma: {lambo_szamlalo}")

# Hány olyan auto van aminek a rendszámtábláján lévő szám, nagyobb, mint a lóereje
szamlalo = 0
for item in autok:
    if item.rendszam_nagyobb_e():
        szamlalo += 1
print(f"{szamlalo} olyan auto van, aminek a rendszáma nagyobb, mint a lóereje.")

# Hány darab 1000 lóerőtől nagyobb teljesítményű Ferrari van?
ferrari_szamlalo = 0
for item in autok:
    if item.loero > 1000 and item.marka == "Ferrari":
        ferrari_szamlalo += 1
print(f"{ferrari_szamlalo} db 1000 lóerőtől jobb Ferrari van.")