#dolgozat kiértékelése

max=int(input("Add meg a dolgozat maximális pontszámát: "))
elert=float(input("Add meg az elért pontszámot: "))

if (elert>max or elert<0):
    print("Hibás adat.")
else:
    szazalek=elert/max*100
    if (szazalek<40):
        print("Elégtelen.")
    elif (szazalek<55):
        print("Elégséges.")
    elif (szazalek<70):
        print("Közepes.") 
    elif (szazalek<85):
        print("Jó.")
    else:
        print("Jeles.")
