
#  exception handlig (error handling) - kivételkezelés (hibakezelés)

lista = [1,2,3]

try:
   # print(bla)
   # print(lista[5])
     print(1/0)

except NameError as e:
    print(e, '- Nem létező változó')
except IndexError as e:
    print(e, '- Tartományon kívűl')
except ZeroDivisionError as e:
    print(e, '- Nullával osztás')

print('A program lefutott.')

lista2 = ['1', '2', '3', None, '4', '', '5', True, 'Lili', '12.78']

for i in  lista2:
    try:
        print(int(i)*2)
    except:
        continue

print(True==1)

try:
    print(bla)     # Ha a bla változó macska körömbe teszem, akkor belfut az else ágba
except:
    print('Nem jó változó név')
else:
    print('Belefutott az else ágba')
finally:
    print('A try blokk vége')  # de minden estben belefut a finally ágba