class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        self.a = a
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')

    def get_area_square(self):
        return self.a ** 2


square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(), square_2.get_area_square())
