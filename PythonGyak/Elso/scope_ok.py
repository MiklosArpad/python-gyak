
# module scope-ok az az egész file-ban megjeleníthetők
# declarálása már az elején megtörténik

# global a
a = 33
b = 44

# function scope-ok csak a függvényen belül élnek, tovább nincs funkciójuk

def test():
    global a, b    # ez a függvény hívás megváltoztatta az a értékét ami 33 volt, most 10, szintén a b-ét is
    a = 10
    b = 20
    print(a, b)
test()
print(a, b)


# ha for, while ciklusban deklarálunk egy változót akkor az a function scope-ból átmegy a module scope-ba

def test2():
    for i in range(5):
        b = 66
        pass

    print(i)
    print(b)

test2()  # ezzel hívom a második függvényt