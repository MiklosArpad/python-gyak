
print(abs(-124)) # egy szám abszolut értékét írja ki

nevek = ['Babi', 'Leni', 'Panni', 'Bozsi', 'Kati', 'Nuni', 'Zseni']

print(list(reversed(nevek)))
# tömbben lévő nevek listáját megfordítva iratja ki

for index, nev in enumerate(nevek):
    print(index, nev)
print(len(nevek))

print(float('147.879')) # egy string számnak a lebegőpontos értékét írja ki

print(hex(125)) # egy szám hexadecimális értékét írja ki

print(len('Ennek a szövegnek a betű karaktereinek számát írja ki'))

print(max(1, 10, 25, 444, 891, 1001))
print(min(1, 10, 25, 444, 891, 1001))

print(2**10)
print(pow(2, 10))
# ez mind a kettő hatványozás 2 a 10-ediken

print(range(100))
# kiírja a számok halmazának kezdő értékét és db számát
print(list(range(100)))
# kiírja a számok listáját 0-99 ig

print(list(range(50, 100, 2)))
# 50 -100 -ig írja ki a számokat és kettesével számol felfelé

print(round(12.8765439, 3))
# ez egy tizedes vcesszős számot kerekít fel vagy le, a második szám azt mondja meg, hogy mennyi szám legyen a tizedes vessző mögött


print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# a számok összegét írjaq ki
# vagy máshogy

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(sum(szamok))