
# string format

# régi string format

szoveg1 = "A te neved %s, és %d éves vagy" % ('Árpi', 48)
# ez a % - placeholder, az s a stringet jeleniti, a d a digit, azaz az integer
print(szoveg1)

# nem olyan régi mód

szoveg2 =  "A te neved {}, és {} éves vagy".format ('Árpi',11)
print(szoveg2)

# az új formázás

nev = 'Valaki'
kor = 33
szoveg3 = f'A te neved {nev}, és  {kor} 111 éves vagy'
print(szoveg3)

nevek_szotar = {'Betti': 33, 'Zsuzsi': 32, 'Fruzsi': 29, 'Bözsi': 37, 'Mazsi': 35}
for nev, kor in nevek_szotar.items():
    print(f'A te neved {nev}, és  {kor+5} 111 éves vagy')