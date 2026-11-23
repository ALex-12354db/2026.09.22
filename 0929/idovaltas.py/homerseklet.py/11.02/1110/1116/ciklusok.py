#Írd ki 1 és 30 között a 7-tel osztható számokat!
# jelezd csillaggal a párosakat!

'''for i in range(1, 31):
    if i % 7 == 0:
        print(i, end='')'''

'''for i in range(7,31,7):
    if i % 2 == 0:
        print(i, end="* ")
    else:
        print(i, end="   ")
    '''
'''szam = int(input("Adj meg 1-10 közötti számot: "))

if (szam < 1 or szam > 10):
    print("Hibás számot adtál meg!")
else:
    for i in range(1, 11):
        print(szam, "x", i, "=", szam * i*szam)'''

szoveg = input("Adj meg egy szöveget: ")
db=0
for betu in szoveg:
    if betu == 'a' or betu == 'A':
        db=db+1
print("Az 'a' betű darabszáma:", db)