megtett_ut=float(input("A megtett út (km): "))
uzemanyag=float(input("Tankolt mennyiség (L): "))
átlagfogyasztas=uzemanyag/megtett_ut*100
print("Az átlagfogyasztás: ", átlagfogyasztas, "L/100km")
print("Az átlagfogyasztás: ", round(átlagfogyasztas, 1), "L/100km")