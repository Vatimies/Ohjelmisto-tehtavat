sukupuoli = input("Mikäs on biologinen sukupuolesi? ")
hemoglobiini = int(input("Ja mikäs on hemoglobiiniarvo? "))

if (sukupuoli == "nainen" or sukupuoli == "Nainen"):
    if hemoglobiini <= 175 and hemoglobiini >= 117:
        print("normaali")
    elif hemoglobiini > 175:
        print("korkea")
    else:
        print("alhainen")
if (sukupuoli == "mies" or sukupuoli == "Mies"):
    if hemoglobiini <= 195 and hemoglobiini >= 134:
        print("normaali")
    elif hemoglobiini > 175:
        print("korkea")
    else:
        print("alhainen")