

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
    def __init__(self, name, age, gender, nation, religion, experience, reliability, education):
        super().__init__(name, age, gender, nation, religion)
        self.experience = experience
        self.reliability = reliability
        self.education = education

    # experience - tapasztalat
    # reliability - megbizhatóság
    # végzettség = könyvelő

Eni = Employee('Enikő', 24, "nő", 'Magyar', 'atheist', 4, 8, 'accountant')
Agi = Employee('Ágnes', 33, 'nő', 'Magyar', 'reformed', 6, 9, 'economist')

print(Eni.name, Eni.religion)
print(Eni.education, Eni.reliability, Eni.religion)

print(Agi.name, Agi.age, Agi.nation, Agi.education, Agi.religion)
