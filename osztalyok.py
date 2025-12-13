class Kutya:
    # Konstruktór függvény:
    def __init__(self, nev, eletkor, fajta, kaja, szin):
        self.nev = nev
        self.eletkor = eletkor
        self.fajta = fajta
        self.kedvenc_kaja = kaja
        self.szin = szin

    # Hogyan konvertáljunk stringgé kutyát str()
    def __str__(self):
        return f"{self.nev} {self.eletkor}, {self.fajta}, kedvenc kaja: {self.kedvenc_kaja}, színe: {self.szin}"
    
    def ember_ev(self):
        return self.eletkor * 7

buksi = Kutya("Buksi", 5, "Dobberman", "hal", "barna")
frakk = Kutya("Frakk", 11, "Vizsla", "Lukrécia", "barna")
coco = Kutya("Coco", 4, "Keverék", "Csirke", "fekete" )
print(frakk)
print(buksi)
print(coco)

print(coco.ember_ev())


