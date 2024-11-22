# Создайте класс Angle, который хранит значение угла в градусах.
# Реализуйте __add__ и __sub__, чтобы складывать и вычитать углы.

# Angle(130) + Angle(50) = Angle(0)
# Angle(50) - Angle(130) = Angle(80)

class Angle:
    def __init__(self, degree):
        self.degree = degree

    def __add__(self, other_degree):
        if isinstance(other_degree, Angle):
            degree_result = (self.degree + other_degree.degree) % 180
            return Angle(degree_result)
        return NotImplemented

    def __sub__(self, other_degree):
        if isinstance(other_degree, Angle):
            degree_result = abs(self.degree - other_degree.degree) % 180
            return Angle(degree_result)
        return NotImplemented

    def __str__(self):
        return f'Angle({self.degree})'


degree_1 = Angle(30)
degree_2 = Angle(150)

result = degree_1 - degree_2
print(f'{degree_1} - {degree_2} = {result}')
