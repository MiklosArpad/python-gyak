
# tuple - azaz nem módosítható adathalmazok

# módosítható adatok []
lista = ['Juli', 'Lili', 'Nani', 'Panni', 'Babi']


# nem mődosítható adatok ()
tup1 = ('Bori', 'Betti', 'Kati', 'Móni', 'Böbe')


print(tup1.index('Kati'))  # ez megmondja, hogy a Kati hanyadik indexen található
print(tup1.count('kati'))  # ez megmondja, hogy a listában hány Kati szerepel

tup3 = ('Árpi')
print(tup3.upper())   # ez a formátum stringként kezeli a tuple listát  és minden betűt nagybetűvé szerkeszt

#tup3 = ('Árpi',)  # ha már van vessző az első név után, akkor már listaként kezeli


#lista.append('Bözsi')
#print(lista)
#lista[-1] = 'Bori'
#print(lista)

print(tup1[2])

tup2 = tuple(lista)    # ez listából tuple-t csinál
print(tup2)

lista2 = list(tup2)    # ez tuple-ból listát csinál
print(lista2)


