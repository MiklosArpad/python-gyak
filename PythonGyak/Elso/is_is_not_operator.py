
# is is-not identity operator - azonossági operator

szam1 = 4
szam2 = 4

print(szam1 == szam2)  # ez igaz választ ad

szam1 = 4
szam2 = 5

print(szam1 == szam2)  # ez hamis választ ad

szam3 = 8
if type(szam3) is int:
    print('integer típus')

szam4 = '8'
if type(szam4) is not int:
    print('nem integer típus')

szam5 = 8
if type(szam5) is not str:
    print('nem string tipus')

    #------------------------------------

class Szemely:
    pass
sz1 = Szemely()
sz2 = sz1

if type(sz1) is Szemely():
    print('személy típus')
else:
    print(type(sz1))

sz3 = Szemely()
sz4 = Szemely()

print(sz3 is not sz3)

if isinstance(sz1, Szemely):
    print('személy típus')
