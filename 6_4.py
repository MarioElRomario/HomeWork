import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.my_list = [int(speed), color, name, is_police]

    def go(self):
        print(f'Машина {self.my_list[2]} поехала')

    def stop(self):
        print(f'Машина {self.my_list[2]} остановилась')

    def turn(self, direcrion):
        print(f'Машина {self.my_list[2]} повернула в сторону {random.choice(direcrion)}')

    def show_speed(self):
        print(f'Скорость машины {self.my_list[2]} {self.my_list[0]}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость машины {self.my_list[2]} больше 60' if self.my_list[
                                                                 0] > 60 else f'Скорость машины меньше 60')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость машины больше 40' if self.my_list[
                                                                 0] > 40 else f'Скорость машины меньше 40')


class PoliceCar(Car):
    pass


direcrion = ['Направо', 'Налево']
audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(70, 'White', 'Oka', False)
lada = WorkCar(30, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
car_list = [audi.go(), audi.show_speed(), audi.turn(direcrion), audi.stop(), oka.go(), oka.show_speed(),
            oka.turn(direcrion), oka.stop(), lada.go(), lada.show_speed(), lada.turn(direcrion), lada.stop(), ford.go(),
            ford.show_speed(), ford.turn(direcrion), ford.stop()]
test = list(map(str, car_list))
