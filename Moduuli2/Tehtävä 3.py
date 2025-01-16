import math

Kanta = int(input("Voisitko antaa minulle suorakulmion kannan pituuden?: "))
Korkeus = int(input("Sitten vielä korkeus: "))

Piiri = Kanta + Korkeus + Kanta + Korkeus
PintaAla = Kanta * Korkeus

print(f"Eli, piiri on {Piiri} ja pinta-ala on {PintaAla}")