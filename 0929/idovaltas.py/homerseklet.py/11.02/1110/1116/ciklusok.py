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

for i in range(1, 10, 3):
    if i % 2 == 0:
        print(i, end="* ")
    else:
        print(i, end="   ")