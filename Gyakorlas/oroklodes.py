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


class Employee(Person):
    experience = 4  # experience - tapasztalat
    reliability = 8  # reliability - megbizhatóság
    education = 'accountant'  # végzettség = könyvelő


Eni = Employee('Enikő', 24, "nő", 'Magyar', 'atheist')
Agi = Employee('Ágnes', 33, 'nő', 'Magyar', 'reformed')

print(Eni.name, Eni.religion)
print(Eni.education, Eni.reliability)

Agi.education = 'economist'
print(Agi.name, Agi.age, Agi.nation, Agi.education, Agi.religion)
