ido=int(input("Az idő másodpercben: "))

ora=ido//3600
print("Óra: ", ora)

perc=(ido%3600)//60
print("Perc: ", perc)

masodperc=(ido%3600)%60
print("Másodperc: ", masodperc)