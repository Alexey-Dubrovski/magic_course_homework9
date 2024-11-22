# Класс для работы с векторами на плоскости.
# Создайте класс Vector2D для двумерных векторов
# с методами сложения, вычитания и умножения на скаляр.
# Реализуйте магические методы __add__, __sub__ и __mul__,
# чтобы перегрузить операторы +, -, и *.

# Vector2D(1, 2) + Vector2D(2, 3) = Vector2D(3, 5)
# Vector2D(2, 3) * 3 = Vector2D(6, 9)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_vector):
        if isinstance(other_vector, Vector2D):
            return Vector2D(self.x + other_vector.x, self.y + other_vector.y)
        return NotImplemented

    def __sub__(self, other_vector):
        if isinstance(other_vector, Vector2D):
            return Vector2D(self.x - other_vector.x, self.y - other_vector.y)
        return NotImplemented

    def __mul__(self, num):
        if isinstance(num, (int, float)):
            return Vector2D(self.x * num, self.y * num)
        return NotImplemented

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


vector_1 = Vector2D(1, 2)
vector_2 = Vector2D(2, 3)

result = vector_1 + vector_2
print(f'{vector_1} + {vector_2} = {result}')
