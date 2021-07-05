class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self,method):
        print(f'Запуск отрисовки {method}')
class Pen(Stationery):
    pass
class Pencil(Stationery):
    pass

class Handle(Stationery):
    pass

p = Pen("Непонятное для чего название 1")
pencil = Pencil("Непонятное для чего название 2")
h = Handle("Непонятное для чего название 3")
p.draw("Ручка")
pencil.draw("Карандаш")
h.draw("Маркер")