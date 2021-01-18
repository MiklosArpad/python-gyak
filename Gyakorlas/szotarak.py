
# Dictioneries, key-value pairs, Szótárak, kulcs-érték párosok (java: hash-maps)

name_age = {'Ildi':22, 'Árpi':28, 'Ári':13}
name_age['Szuszi'] = 43
print(name_age)

name_age.pop('Árpi')   # ez kitörli a megjelenítendő listából
print(name_age)

name_age.get('Árpi')    # az a kulcs értékét írja ki


for key in name_age.keys():
    print(key)

for value in name_age.values():
    print(value)

for key, value in name_age.items():   # itt az items metódus arra jó, hogy mindkét változót kikérja a szótárból
    print(key, value)

#dict1 = ['adat1':[1,2,3,4,5], 'adat2':77, 'adat3':(12,13,14)]

# ebben a szótárban több érték van hozzárnedelve a kulcshoz!!

name_age2 = {'Árpi':{'age':47, 'hair':'braun'},
             'Ildi':{'age':43, 'hair':'braun'},
             'Ári':{'age':13, 'hair':'braun'}}
print(name_age2)

degrees = {0:'east', 45:'north', 34: 'south', 90: 'west'}

