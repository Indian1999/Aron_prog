# Adott egy lista ami egy osztály (25 fő) dolgozatainak az eredményét
# tartalmazza (0-100). 
# 1. feladat: Mennyi az eredmények átlaga (Egész értékre kerekítve)?

# 2. feladat: Hány tanuló szerzett 5-ös osztályzatot (minimum 91 pont)?

# 3. feladat: A lista hanyadik indexén található a legjobb eredmény?

import random
eredmények = [random.randint(0, 100) for i in range(25)]