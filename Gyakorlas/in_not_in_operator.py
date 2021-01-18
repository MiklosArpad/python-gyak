
# in me,bership operator - in tagsági operátor

mondas = "Bagoly mondja verébnek, hogy nagyfejű."

#for betu in mondas:
#    print(betu)

print('Bagoly' in mondas)
# ha szó vagy szótag egyezeés van a mondás szavaival, akkor true, ha nem akkor false

if 'veréb' in mondas:
    print('találat')

nevek_lista = ['Betti', 'Zsuzsi', 'Fruzsi', 'Bözsi', 'Mazsi']
if 'Fruzsi' in nevek_lista:
    print('találat')

if 'Móni' not in nevek_lista:   # Móni nincs a listában ezért találat
    print('nincs találat')

# csak a kulcsok szerint keres, az érték pár szerint nem

nevek_szotar = {'Betti': 33, 'Zsuzsi': 32, 'Fruzsi': 29, 'Bözsi': 37, 'Mazsi': 35}
if 'Zsuzsi' in nevek_szotar:
    print('találat')

szamok1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
szamok2 = [0, 2, 4, 6, 8, 10]

azonos_szamok = []
egyedi_szamok = []

for szam in szamok1:
    if szam in szamok2:
        azonos_szamok.append(szam)  # append - hozzáadja a új listához
    else:
        egyedi_szamok.append(szam)

print(azonos_szamok, egyedi_szamok)

for szam in szamok1:
    if szam not in szamok2:
        egyedi_szamok.append(szam)
print(egyedi_szamok)