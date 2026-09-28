ahossz=float(input("Add meg a tégla hosszát (cm): "))
aszelesseg=float(input("Add meg a tégla szélességét (cm): "))
amagassag=float(input("Add meg a tégla magasságát (cm): "))

A=2*(ahossz*aszelesseg+ahossz*amagassag+aszelesseg*amagassag)
V=ahossz*aszelesseg*amagassag

print("A tégla felszíne: ",A," cm²")
print("A tégla térfogata: ",V," cm³")
