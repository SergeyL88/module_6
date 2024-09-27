PI: float = 3.14


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = [*color] if self.__is_valid_color(color) else [0, 0, 0]
        if self.__is_valid_sides(sides):
            if len(sides) == self.sides_count:
                self.__sides = [*sides]
            elif len(sides) == 1:
                self.__sides = [*sides] * self.sides_count
            else:
                self.__sides = [1] * self.sides_count
            self.filled = True
        else:
            self.__sides = [1] * self.sides_count
        self.filled = False

    def __is_valid_color(self, check_color):
        for rgb in check_color:
            if 0 > rgb or rgb >= 256:
                print(False)
                return False
            else:
                return True

    def __is_valid_sides(self, check_sides):
        if all(isinstance(side, int) and side > 0 for side in check_sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def set_color(self, *new_color):
        if self.__is_valid_color(new_color):
            self.__color = [*new_color]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) and len(new_sides) == self.sides_count:
            self.__sides = [*new_sides]
        return self.__sides

    def __len__(self) -> float:
        if isinstance(self, Circle):
            return int((4 * self.get_square() * PI) ** (0.5))
        else:
            return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sum(self.get_sides()) / (2 * PI)

    def get_square(self):
        return (self.get_sides()[0] ** 2) / (4 * PI)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides) -> None:
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (sum(self.get_sides())) * 0.5
        return (p * ((p - a) * (p - b) * (p - c))) ** (0.5)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((255, 255, 255), 10)  # (Цвет, стороны)
circle1.get_square()
cube1 = Cube((222, 35, 130), 6)

# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(255, 70, 15)  # Не изменится
print(cube1.get_color())

# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())


# print(circle1.get_square())
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# # Проверка объёма (куба):
# print(cube1.get_volume())
triangle = Triangle((5, 5, 5), 3, 4, 5)
print(triangle.get_square())
