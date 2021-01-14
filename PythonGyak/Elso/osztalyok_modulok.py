

# classes and object oriented programing - osztályok és az OOP
# user defined types - felhasználó által definiált tipusok

class Person:
    # member variables/fields - tag változók/osztályok
    name = ''
    age = None
    gender = ''

pers1 = Person
pers1.name = 'Juci'
pers1.age = 29
pers1.gender = 'female'

print(pers1.name, pers1.age, pers1.gender)

pers2 = Person
pers1.name = 'Laci'
pers1.age = 39
pers1.gender = 'male'

print(pers2.name, pers2.age, pers2.gender)

pers3 = Person
pers3.name = 'Buci'
pers3.age = 36
pers3.gender = 'male'

print(pers3.name, pers3.age, pers3.gender)