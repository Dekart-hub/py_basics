class Vector:
    def __init__(self, x: int, y: int):
        self.x = x;
        self.y = y;

    def __add__(self, other):
        new_vect = Vector(self.x + other.x, self.y + other.y)
        return new_vect;

    def __sub__(self, other):
        new_vect = self + Vector(-other.x, -other.y)
        return new_vect;

    def __mul__(self, num: int):
        self.x *= num
        self.y *= num
        return self

    def __str__(self):
        return f"Vector: x({self.x}), y({self.y})"


a = Vector(10, 5)
b = Vector(5, 5)
print(a)
print(a + b)
print(a - b)
print(a * 2)