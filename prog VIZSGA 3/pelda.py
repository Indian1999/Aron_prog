import os

path = __file__
print(path) # c:\Users\Meggyecske\Desktop\Áron_prog\prog VIZSGA 3\pelda.py
path = os.path.dirname(__file__)
print(path) # c:\Users\Meggyecske\Desktop\Áron_prog\prog VIZSGA 3
path = os.path.join(os.path.dirname(__file__), "konyvek-adatok.txt")