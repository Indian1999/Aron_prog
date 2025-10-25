tábla = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board():
    for row in tábla:
        print(row)

def valid_position(sor, oszlop):
    if sor < 0 or sor > 2:
        return False
    if oszlop < 0 or oszlop > 2:
        return False
    if tábla[sor][oszlop] != "-":
        return False
    return True
    
def check_for_winner():
    # Oszlopok ellenőrzése
    for i in range(0, 3): # i = 0, 1, 2
        if tábla[0][i] == tábla[1][i] and tábla[2][i] == tábla[0][i]:
            if tábla[0][i] == "O":
                return "O nyerte a játékot!"
            if tábla[0][i] == "X":
                return "X nyerte a játékot!"
            
    # Sorok ellenőrzése
    for i in range(0, 3):
        if tábla[i][0] == tábla[i][1] and tábla[i][2] == tábla[i][0]:
            if tábla[i][0] == "O":
                return "O nyerte a játékot!"
            if tábla[i][0] == "X":
                return "X nyerte a játékot!"

    # Átlók ellenőrzése (Házi feladat)

    # Döntetlen ellenőrzése
    for i in range(0, 3):
        for j in range(0,3):
            if tábla[i][j] == "-":
                return None
    return "Döntetlen!"

print_board()

turn_of_player_x = True # x játékos jön-e
winner = None

while winner == None:
    # 0. Jelenítsük meg a játéktáblát
    print_board()

    # 1. A soron lévő játékos lerakja a jelét
    sor = int(input("Add meg a sor számát! (0-2): "))
    oszlop = int(input("Add meg az oszlop számát! (0-2): "))
    while not valid_position(sor, oszlop): 
        print("Érvénytelen pozíció!")   
        sor = int(input("Add meg a sor számát! (0-2): "))
        oszlop = int(input("Add meg az oszlop számát! (0-2): "))

    if turn_of_player_x:
        tábla[sor][oszlop] = "X"
        turn_of_player_x = False
    else:
        tábla[sor][oszlop] = "O"
        turn_of_player_x = True
    
    # 2. Ellenőrizzük, hogy vége-e a játéknak
    winner = check_for_winner()

print(winner)
print_board()