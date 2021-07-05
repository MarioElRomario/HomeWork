class Road:
    def __init__(self, length, width):
        try:
            self._length = int(length)
            self._width = int(width)
            self.mass = 25
            self.cm = 5
        except:
            print("Ошибочные данные")
            quit()

    def сalc(self):
        result = self._length * self._width * self.mass * self.cm
        return f'{result / 1000}т'


r = Road(input('Введите длину: '), input('Введите ширину: '))
print(r.сalc())
