# modules, naqmespaces and importing - modulok, névterek és importálás

import math  # beiomportálja ebbe a file-ba a már pycharmban megírt feli-okat

print(math.sin(16))
print(math.tan(16))

import szotarak  # az előtö órán írt file-t is be tudom importálni

szotarak.name_age2
print(szotarak.name_age)
print(szotarak.degrees)

# ha külső mappából akarunk hívni függvény, akkor azt így kell

# import.kulsoMappa.szotarak
# kolsoMappa.szotarak.name_age

# de ezt lehet röviditeni is úgy, hogy alias-t adok neki
# import.kulsoMappa.szotarak as vmi

# és akkor csak úgy kell hivatkozni, hogy
# vmi.name_age

#from tuple import tup1
import tuple


def tup1():
    print(' ez a tuple-ban van...')

tup1()
# tuple.tup1()  ez valamiért hibát ír ki!!! 25-ös film


