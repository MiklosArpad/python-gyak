
def hello():
    print(f'Hello! {__name__} modulból!')

szam = 2021

class Szemely:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor
    def show_fields(self):
        print(self.nev, self.kor)

if __name__ == 'main':
    hello()
    print(szam)
    Juli = Szemely('Jancsika', 111)
    Juli.show_fields()
