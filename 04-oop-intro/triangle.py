import random,math
class Triangle:
    default_color = "blue"
    default_line_thickness = 1

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.color = Triangle.default_color
        self.lineThickness = Triangle.default_line_thickness
    def __str__(self):
        return f'({self.a}, {self.b}, {self.c})'
    def __eq__ (self,other):
        return self.a == other.a and self.b == other.b and self.c == other.c
    def __gt__(self, other):
        return self.__sub__(Triangle.zero()) > other.__sub__(Triangle.zero())          
    def __add__(self, other):
        return Triangle(self.a + other.a, self.b + other.b, self.c + other.c)
    def __sub__(self, other):
        return (abs(self.a - other.a) ** 2 + abs(self.b - other.b) ** 2 + abs(self.c - other.c) ** 2) ** 0.5   
    @staticmethod 
    def random_line_thickness():
        return random.randint(1,10)
    @classmethod
    def zero(cls):
        return cls(0,0,0)
    @classmethod
    def random (cls, min=0, max=10):
        return cls(random.randrange(min, max), random.randrange(min, max), random.randrange(min, max))        
    def obsah(self):
        s = (self.a + self.b + self.c) / 2
        print(f"{math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))}cm2 ")

    def obvod(self):
        print(f"{(self.a + self.b + self.c)}cm")
        
    def draw(self):
        print(f"Trojuhelnik (a = {self.a}, b = {self.b}, c = {self.c}), color: {self.color}, line thickness = {self.lineThickness}")

class Triangle_height(Triangle):
    def __init__(self,a,b,c,v):
        super().__init__(a,b,c)
        self.v = v
    def __str__(self):
        return f'({self.a}, {self.b},{self.c}, {self.v})'     
    def draw(self):
        super().draw()
        print(f"v = {self.v}")    


triangle1 = Triangle(5,6,10)
print(triangle1)



triangle2 = Triangle_height(5,6,10,12)
print(triangle2)

Triangle.default_color = "red"

triangle2 = Triangle.zero()
print(triangle2)

print(type(triangle1))
print(isinstance(triangle2, Triangle))
triangle2.lineThickness = Triangle.random_line_thickness()
triangle2.draw()

print(f'{"*".ljust(80,"*")}\nOvěř fungování všech magických metod na příkladech objektů bod1 a bod2')
print(str(triangle1))
print(str(triangle2))
print(triangle1 - triangle2)
print(triangle1 + triangle2)
print(triangle1 == triangle2)
print(triangle1 > triangle2)
print(f'{"*".ljust(80,"*")}\nVytvoř do proměnné body seznam 5 objektů na náhodných pozicích v rozmezí -10 až 10')

triangles = [Triangle.random(-10,10) for i in range(5)]
print(f'{"*".ljust(80,"*")}\nPro každý objekt seznamu body proveď jeho symbolické vykreslení metodou draw()')
for i in triangles:
    i.draw()


triangle1.obsah()
triangle1.obvod()