
# az __init__ metódus más C nyelvekben a Konstruktor

class Person:
    def __init__(self, name, age, gender, nation, religion='hindu'):
        self.name = name
        self.age = age
        self.gender = gender
        self.nation = nation
        self.religion = religion
        # ha több név van a bázisban, akkor célszerű ide is inicializálni a hellot
        self.hello()


    def hello(self):
        print('hello ' + self.name)

# object instance - objektum példány

Zsani = Person('Zsanci', 19, 'female', 'hungarian', 'buddhist')
Pubi = Person('Puber', 22, 'male', 'english')

print(Zsani.religion)
print(Pubi.religion)

Zsani.hello()
Pubi.hello()

print(type(Zsani))
print(type(Pubi))
