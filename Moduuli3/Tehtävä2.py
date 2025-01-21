hyttiluokka = input("Mikäs on teikäläisen hyttiluokka? Lux, A, B, vai C? ")

#alla on ensimmäinen testini luoda or lauseke
if (hyttiluokka == "Lux") or (hyttiluokka == "lux"):
    print("LUX on parvekkeellinen hytti yläkannella.")
#alla on toinen testini luoda or lauseke
elif (hyttiluokka == "A" or hyttiluokka == "a"):
    print("A on ikkunallinen hytti autokannen yläpuolella.")
#tästä eteenpäin on siistitty versio or lausekkeesta
elif hyttiluokka == "B" or hyttiluokka == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C" or hyttiluokka == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Eipä ole hyttiluokka")