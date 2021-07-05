import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in self.__color:
            print(i)
            if i == "Красный":
                time.sleep(7)
            elif i == "Желтый":
                time.sleep(2)
            elif i == "Красный":
                time.sleep(7)


traffic = TrafficLight()
traffic.running()
