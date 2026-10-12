hom=float(input("Add meg a hőmérsékletet (°C): "))

if( hom<0):
    print("Fagy!")

if(hom>0):
    print("Nem fagy!")

if(hom < 0):
    print("szilárd halmazállapotú!")
elif(hom > 100):
    print("gáz halmazállapotú!")
else:
    print("folyékony halmazállapotú!")