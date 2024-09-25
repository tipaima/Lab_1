class Info:
    def __init__(self, name):
        self.name = name

    def m1(self):
        return {
            "name": self.name,
        }

    def __m2__(self):
        return f"Название: {self.name}\n"


class Classic(Info):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

    def m1(self):
        Classic.m1 = super().m1()
        Classic.m1.update({"genre": self.genre})
        return Classic.m1

    def __m2__(self):
        return f"Название: {self.name}\n Жанр: {self.genre}\n"


class Pop(Info):
    def __init__(self, name, genre, long):
        super().__init__(name)
        self.genre = genre
        self.long = long

    def m1(self):
        Pop.m1 = super().m1()
        Pop.m1.update({"genre": self.genre})
        Pop.m1.update({"long": self.long})
        return Pop.m1

    def __m2__(self):
        return f"Название: {self.name}\n Жанр: {self.genre}\n Длительность: {self.long} сек\n"


class Rep(Info):
    def __init__(self, name, genre, long, pip):
        super().__init__(name)
        self.genre = genre
        self.long = long
        self.pip = pip

    def m1(self):
        Rep.m1 = super().m1()
        Rep.m1.update({"genre": self.genre})
        Rep.m1.update({"long": self.long})
        Rep.m1.update({"long": self.pip})
        return Rep.m1

    def __m2__(self):
        return f"Название: {self.name}\n Жанр: {self.genre}\n Длительность: {self.long} сек\n Исполнитель:{self.pip}"
