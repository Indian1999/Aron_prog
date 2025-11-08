

file = open("autok_feladat/autok.txt", "r", encoding="utf-8")

autok = []
for line in file:
    line = line.strip()  # Leszedi a whitespace karaktereket elejéről, végéről
    line = line.split(";") # ['PQN-434', 'Lamborghini', '650']
    auto = {
        "rendszam": line[0],
        "marka": line[1],
        "ar": int(line[2])
    }
    autok.append(auto)

file.close()

# Hány kocsi adatait tartalmazza az autok.csv?
print(f"Beolvastam {len(autok)} auto adatát.")

# Mennyibe kerül a legdrágább autó?
max_index = 0
for i in range(1, len(autok)):
    if autok[max_index]["ar"] < autok[i]["ar"]:
        max_index = i
print("A legdrágább auto:")
print(autok[max_index])

# Hány Tesla-t tartalmaz a fájl?
szamlalo = 0
for i in range(len(autok)):
    if autok[i]["marka"] == "Tesla":
        szamlalo += 1
print(f"{szamlalo} db Tesla van a kocsik között.")

# Írja ki, hogy milyen márkájú a 'TUW-976' rendszámú autó, ha nincs ilyen rendszam,
# írd ki hogy nincs ilyen rendszámú auto

rendszam = "TUW-976"
auto_index = -1
for i in range(len(autok)):
    if autok[i]["rendszam"] == rendszam:
        auto_index = i
        break # Kilép a ciklusból

if auto_index == -1:
    print(f"Nincs {rendszam} rendszámú auto.")
else:
    marka = autok[auto_index]["marka"]
    print(f"A {rendszam} rendszámú auto márkája: {marka}")
