nevek1 = ['Babi', 'Leni', 'Panni', 'Bozsi', 'Kati', 'Nuni', 'Zseni', 10, True]
nevek2 = ['Pali', 'Lali', 'Lolo', 'Pisti', 'Cucu']


# for nev in nevek1:
#    print(nev)
# for nev in nevek2:
#    print(nev)

def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev, str):
            print(nev.upper())
        else:
            print('Nem string tipus, hanem, ' + str(type(nev)))


nev_printer(nevek1)
nev_printer(nevek2)
