import math


kuhanpituus = int(input("heissan, minkäs senttisen kuhan kaappasit? "))
#alla ensimmäinen yritys, missä "kuhaehto" toimi if lausekkeen jälkeisenä
#kuhaehto = kuhanpituus >= 37
loput = 37 - kuhanpituus

if kuhanpituus >=37:
    print("Oikein muikea kuha")
else:
    print(f"Ei kelpaa, laske kuule se surkimus takaisin vetteen. Hommaa {loput} senttiä suurempi")