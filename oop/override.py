class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __mul__(self, p):
        return Point(self.x * p.x, self.y * p.y)

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()
             
    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.length() == p.length()

    
    def move(self, x, y):
        self.x += x
        self.y += y
    
p1 = Point(3, 4)

p2 = Point(3, 2)

p3 = Point(3, 3)

p4 = Point(7, -1)

print(p1 + p4, p3*p2)

print(p1 > p2, p1 < p2, p3 == p3, p4 >= p4, p3 <= p3)

