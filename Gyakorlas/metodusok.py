
# metodusok

class Person:
    # member variables/fields - tag változók/osztályok
    name = ''
    age = None
    gender = ''

    # metodusok

    def set_age(self, value):
        self.age = value    # ez az age- nem a Person üres age-je
                            # self.age = value ezzel tudom beállítani végleges évszámra

    def set_name(self, value):
        self.name = value

    def set_gender(self, value):
        self.gender = value


# object instance - obkektum példány

pers1 = Person()
pers1.set_age(44)
pers1.set_name('Jusuf')
pers1.set_gender('male')

print(pers1.name, pers1.age, pers1.gender)