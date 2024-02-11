from math import pi as PI

import scipy

class Planets:
    """
    Документация на класс.
    Базовый класс "Планеты".
    """
    def __init__(self, name: str, radius: int, weight: int, numberofsatellites: int):
        """Инициализация  и подготовка объекта к работе.


        :param name: Назначение планеты
        :param radius: радиус [км]
        :param weight: масса [кг]
        :param numberofsatellites: число спутников

        Примеры:
        >> planet_1 = Planets('Меркурий', 2439, 3 * (10**23), 0)
        """
        self.name = name
        self.radius = radius
        self.weight = weight
        self.numberofsatellites = numberofsatellites

    def __str__(self):
        """
        Метод представляющий объекты класса в виде строки, которые удобно читать.
        """
        return f"Имя планеты: {self.name}. Радиус: {self.radius}. Масса: {self.weight}. Число спутников: {self.numberofsatellites}"

    def __repr__(self):
        """
        Метод представляющий объекты класса в виде строки в "официальном" виде.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, numberofsatellites={self.numberofsatellites!r})"

    def surfacearea(self):
        """
        Метод возвращающий площадь поверхности планеты.

        Данный метод наследуется для всех дочерних классов, так как
        для любой планеты можно расчитать приблизительную площадь поверхности.

        Допущение : ПРИНИМАЕМ ФОРМУ ПЛАНЕТ ИДЕАЛЬНОЙ, О ЕСТЬ ШАР.
        """
        return 4 * PI * ((self.radius * 1000)**2)


    def volume(self):
        """
        Метод возвращающий объём планеты.
        """
        return (4/3) * PI * ((self.radius * 1000)**3)

    def gravitacceleration(self):
        """
        Метод возвращающий ускорение свободного падения планеты.
        """
        return (self.weight / ((self.radius * 1000)**2)) * scipy.constants.gravitational_constant

    def __getattr__(self, item):
        """
        Метод возвращающий ошибку при введение не существующих атрибутов.
        """
        return f"Атрибут {item} не существует"
class TheEarthGroup(Planets):
    """
    Дочерний класс "Планеты земной группы".
    """
    def __init__(self, name: str, radius: int, weight: int, numberofsatellites: int, habitability: bool):
        """Инициализация экземпляра класса."""
        super().__init__(name=name, radius=radius, weight=weight, numberofsatellites=numberofsatellites)
        """Вызов конструктора базового класса."""
        self.habitability = habitability

    def dictat(self):
        """
        Метод возвращающий словарь, где ключ имя атрибута,а значение - значение атрибута.
        """
        return print(dict(self.__class__.__name__))

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, numberofsatellites={self.numberofsatellites!r})"

    def habit(self, habitability: bool) -> bool:
        """
        Метод определяющий обитаемость планеты.
        """
        if habitability == True:
            return print('Планета обитаемая.')
        else:
            return print('Планета не обитаемая.')


class Giants(Planets):
    """
    Дочерний класс "Планеты-гиганты".
    """
    def __init__(self, name: str, radius: int, weight: int, numberofsatellites: int):
        """Инициализация экземпляра класса."""
        super().__init__(name=name, radius=radius, weight=weight, numberofsatellites=numberofsatellites)
        """Вызов конструктора базового класса."""

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, numberofsatellites={self.numberofsatellites!r})"

if __name__ == "__main__":
    earth = TheEarthGroup("Earth", 6738, 5.9 * 10**24, 1, True)
    print(earth.rrr)
    print(earth.gravitacceleration())
    pass
