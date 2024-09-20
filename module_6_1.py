class Animal:

    alive: bool = True
    fed: bool = False

    def eat(self, food):
        if isinstance(food, (Flower, Fruit)):
            if food.edible == False:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
            else:
                print(f'{self.name} съел {food.name}')
                self.fed = True
        else:
            print('Похоже что-то не съедобное')

    def __repr__(self) -> str:
        return self.name


class Plant:

    edible: bool = False

    def __init__(self) -> None:
        self.name

    def __repr__(self) -> str:
        return self.name, self.edible

    def __str__(self):
        return self.name


class Mammal(Animal):

    def __init__(self, name) -> None:
        self.name = name


class Predator(Animal):

    def __init__(self, name) -> None:
        self.name = name


class Flower(Plant):

    def __init__(self, name) -> None:
        self.name = name


class Fruit(Plant):
    edible = True

    def __init__(self, name) -> None:
        self.name = name


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
