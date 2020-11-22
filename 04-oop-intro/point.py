import random

'''
Příklad jednoduché třídy Point umožňující vytvářet symbolické grafické objekty - body
'''
class Point:
    # Atribut na úrovni třídy
    default_color = 'red'
    # Konstanty na úrovni třídy
    # Privátní konstanta, vně třídy nepřístupná
    __MAX_X = 1000
    # Veřejná konstanta, vně třídy přístupná
    MAX_Y = 1000

    # Metoda pro inicializaci objektu (konstruktor)
    def __init__(self, x, y):
        # self zastupuje samotný objekt
        # Atributy na úrovni objektu
        self.x = x
        self.y = y
        #? Vytvořte atribut objektu color a přiřaďte mu výchozí barvu podle výchozího atributu třídy
        self.color = Point.default_color

    # Magická metoda pro výpis textové informace o objektu
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Magická metoda pro porovnávání objektů
    def __eq__(self, other):
        # Zjistí totožně umístěné objekty
        return self.x == other.x and self.y == other.y

    # Magická metoda pro zjištění, zda je objekt větší (je dál od středu) než druhý
    def __gt__(self, other):
        return self.__sub__(Point.zero()) > other.__sub__(Point.zero())

    # Magická metoda pro součet dvou objektů
    def __add__(self, other):
        # Provede sečtení obou souřadnic a vrátí nový objekt
        return Point(self.x + other.x, self.y + other.y)

    #? Vytvoř magickou metodu, která umožní rozdílem dvou objektů-bodů (jejich odečtením) zjistit jejich vzdálenost
    def __sub__(self, other):
        # Provede zjištění vzdálenosti dvou objektů
        return (abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2) ** 0.5

    #? Tady bude statická (třídní) metoda random_color(), která vygeneruje náhodou barvu rgb zapsanou hexadecimálně
    @staticmethod
    def random_color():
        return '#' + ''.join([str(hex(random.randint(0,255)))[2:] for i in range(3)])

    # Metoda třídy, která vytvoří nový objekt-bod na nulových pozicích
    @classmethod
    def zero(cls):
        #? Jaký význam má argument cls ?
        return cls(0, 0)

    #? Tady bude metoda třídy random_pos(), která bude na základě zadaných argumentů určujících platný rozsah hodnot
    #? vytvářet náhodně umístěné body
    @classmethod
    def random_pos(cls, min=0, max=10):
        return cls(random.randrange(min, max), random.randrange(min, max))

    # Metoda objektu, která (symbolicky v podobě textu) "vykreslí" daný objekt
    def draw(self):
        # Argument self zastupuje samotný objekt
        print(f'Bod (x:{self.x}, y:{self.y}), barva: {self.color}')

    #? Tady bude metoda objektu change_color(), která bude na základě zadaného argumentu nastavovat barvu objektu
    # def change_color(self, color):
    #    self.color = color

    # Vlastnosti (properties) třídy zprostředkující přístup k zapouzdřeným atributům self.__x, self.__y a self.__color
    # Getter pro získání hodnoty atributu self.__x
    @property
    def x(self):
        return self.__x

    # Setter pro nastavení hodnoty atributu self.__x
    @x.setter
    def x(self, value):
        # Ošetření zadání hodnoty do property pomocí bloku výjimky (try - except [- finally])
        # V bloku try se má provést (nejistý) sled příkazů
        try:
            value = int(value)
            if value > Point.__MAX_X:
                # Příkazem raise se vyvolá určitá výjimka - v tomto případě nejobecnější - Exception()
                raise Exception(f'The value of a variable x is greater than {Point.__MAX_X}')
            self.__x = value
        # Když v bloku try nastane nějaká chyba (výjimka), řeší se v části except
        except ValueError:
            # V tomto případě příkaz raise vyvolá specifickou výjimku - ValueError()
            raise ValueError('The value of a variable x is not a number')


    # Getter pro získání hodnoty atributu self.__y
    @property
    def y(self):
        return self.__y

    # Setter pro nastavení hodnoty atributu self.__y
    @y.setter
    def y(self, value):
        try:
            value = int(value)
            if value > Point.MAX_Y:
                raise Exception(f'The value of a variable y {value} is greater than {Point.MAX_Y}')
            self.__y = value
        except ValueError:
            raise ValueError('The value of a variable y is not a number')

    # Getter pro získání hodnoty atributu self.__color
    @property
    def color(self):
        return self.__color

    # Setter pro nastavení hodnoty atributu self.__color
    @color.setter
    def color(self, value):
        self.__color = value


'''
Příklad dědičnosti - třída InfoPoint je dědicem (potomkem - child) třídy předka (parent) Point
'''
class InfoPoint(Point):
    # Metoda konstruktoru - v této třídě potomka doplněna o atribut url
    def __init__(self, x, y, url):
        # Metoda super() zpřístupňuje atributy a metody předka - v tomto případě konstruktor
        super().__init__(x, y)
        self.url = url

    # Přepsaná (override) magická metoda pro výpis textové informace o objektu - využití polymorfismu
    def __str__(self):
        return f'({self.x}, {self.y}, {self.url})'

    # Přepsaná metoda objektu, která (symbolicky v podobě textu) "vykreslí" daný objekt - další příklad polymorfismu
    def draw(self):
        super().draw()
        # Argument self zastupuje samotný objekt
        print(f'URL: {self.url}')


#? Vytvoř objekt bod1 na pozici x: 8, y: 5
Point.__MAX_X = 500
Point.MAX_Y = 500
bod1 = Point(8, 5)
print(bod1)

#? Vytvoř objekt bod2 na pozici x: 4, y: 10
bod2 = InfoPoint(4, 10, 'https://www.sspu-opava.cz')
print(bod2)

#? Změň výchozí barvu na modrou
Point.default_color = 'blue'

#? Vytvoř objekt bod3 pomocí metody zero()
bod3 = Point.zero()
bod1.draw()
bod2.color = Point.random_color()
bod2.draw()
bod3.draw()

#? Ověř datový typ objektu bod1
print(type(bod1))
print(type(bod2))

#? Ověř zda je objekt bod2 instancí třídy Point
print(isinstance(bod2, Point))
print(isinstance(bod2, object))

#? Proveď změnu barvy objektu bod2 na náhodnou barvu vygenerovanou statickou metodou random_color()
bod2.color = Point.random_color()
bod2.draw()

#? Ověř fungování všech magických metod na příkladech objektů bod1 a bod2
print(f'{"*".ljust(80,"*")}\nOvěř fungování všech magických metod na příkladech objektů bod1 a bod2')
print(str(bod1))
print(str(bod2))
print(bod1 - bod2)
print(bod1 + bod2)
print(bod1 == bod2)
print(bod1 > bod2)

#? Vytvoř do proměnné body seznam 5 objektů na náhodných pozicích v rozmezí -10 až 10
print(f'{"*".ljust(80,"*")}\nVytvoř do proměnné body seznam 5 objektů na náhodných pozicích v rozmezí -10 až 10')
body = [Point.random_pos(-10,10) for i in range(5)]

#? Pro každý objekt seznamu body proveď jeho symbolické vykreslení metodou draw()
print(f'{"*".ljust(80,"*")}\nPro každý objekt seznamu body proveď jeho symbolické vykreslení metodou draw()')
for b in body:
    b.draw()

#? Zjisti, který objekt v seznamu body má největší vzdálenost od počátku
print(f'{"*".ljust(80,"*")}\nZjisti, který objekt v seznamu body má největší vzdálenost od počátku')
max = body[0]
for i in range(1, len(body)):
    max = body[i] if body[i] > max else max
max.draw()

#? Zjisti, mezi kterými objekty v seznamu body je nejkratší vzdálenost
print(f'{"*".ljust(80,"*")}\nZjisti, mezi kterými objekty v seznamu body je nejkratší vzdálenost')
min = [body[0] - body[1], (body[0], body[1])]
for x in range(0, len(body) - 1):
    for y in range(x + 1, len(body)):
        min = [body[x] - body[y], (body[x], body[y])] if body[x] - body[y] < min[0] else min
print(min[0], str(min[1][0]), str(min[1][1]))