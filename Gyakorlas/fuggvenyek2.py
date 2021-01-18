
a = 10
b = 20

def osszeadas1():
    print(a+b)

def osszeadas2(a, b, c=4):
    return a+b+c

def osszeadas3(*args):    
    return sum(args)

def udvozlesek(*args):
    koszones = 'Lazább üdvözlési formák: '
    for k in args:
        koszones += k
        koszones += ', '
    print(koszones[0:len(koszones)-2])  #a minusz 2 azért kell, hogy a kiiratásnál ne legyen a végén vessző

udvozlesek('szia', 'hello', 'szevasz', 'csövi', 'üdv')


#osszeadas1()
#osszeg = osszeadas2(45, 25)
#print(osszeg)

#print(osszeadas3(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))