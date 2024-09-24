class Info:
    def __init__(self, brand, name, horsepower, year):
        self.brand = brand
        self.name = name
        self.horsepower = horsepower
        self.year = year

    def m1(self):
        return {
            "brand": self.brand,
            "name": self.name,
            "horsepower": self.horsepower,
            "year": self.year
        }

    def __m2__(self):
        return f"Марка: {self.brand}\n Прозвище{self.name}\n Лошадиные силы: {self.horsepower}\n Год выпуска: {self.year}\n"


class Busses(Info):
    def __init__(self, brand, name, horsepower, year, sits):
        super().__init__(brand, name, horsepower, year)
        self.sits = sits

    def m1(self):
        Busses.m1 = super().m1()
        Busses.m1.update({"sits": self.sits})
        return Busses.m1

    def __m2__(self):
        return f"Марка: {self.brand}\n Прозвище{self.name}\n Лошадиные силы: {self.horsepower}\n Год выпуска: {self.year}\n Места: {self.sits}"


class Cars(Info):
    def __init__(self, brand, name, horsepower, year, equipment):
        super().__init__(brand, name, horsepower, year)
        self.equipment = equipment

    def m1(self):
        Cars.m1 = super().m1()
        Cars.m1.update({"equipment": self.equipment})
        return Cars.m1

    def __m2__(self):
        return f"Марка: {self.brand}\n Прозвище{self.name}\n Лошадиные силы: {self.horsepower}\n Год выпуска: {self.year}\n Комплектация: {self.equipment}"


class Trucks(Info):
    def __init__(self, brand, name, horsepower, year, load_capacity):
        super().__init__(brand, name, horsepower, year)
        self.load_capacity = load_capacity

    def m1(self):
        Trucks.m1 = super().m1()
        Trucks.m1.update({"equipment": self.load_capacity})
        return Trucks.m1

    def __m2__(self):
        return f"Марка: {self.brand}\n Прозвище{self.name}\n Лошадиные силы: {self.horsepower}\n Год выпуска: {self.year}\n Грузоподъемность: {self.load_capacity} т"
