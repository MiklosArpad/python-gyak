
jelszo = 'nivea'
bemenet = input('Mi a jelszo? ')

proba = 0
while bemenet != jelszo:
    proba += 1
    if proba ==3:
        print('Nincs tobb probalkozasi lehetoseg')
        break
    print('Rossz jelszo, osszesen 3 próba lehetseges!')
    bemenet = input('Mi a jelszo? ')

if bemenet == jelszo:
    print('Sikeres belepes!')

