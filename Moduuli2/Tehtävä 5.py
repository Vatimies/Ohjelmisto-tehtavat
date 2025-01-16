import math

leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

lei = leiviskat * 20
nau = (naulat + lei) * 32
luo = (luodit + nau) * 13.3

Kg = int(luo / 1000)
g = luo % 1000

print(f"Paino nykymittojen mukaan: {Kg} kilogrammaa ja {g:.2f} grammaa.")