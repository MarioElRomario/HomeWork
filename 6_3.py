class Worker:
    def __init__(self, name, surname, position, _income, wage, bonus):
        self._income = {'wage': int(wage), 'bonus': int(bonus)}
        self.my_list = [name, surname, position, _income]


class Position(Worker):
    def get_full_name(self):
        return f'{self.my_list[0]} {self.my_list[1]}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите должность: '), input('Введите доход: '),
             input('Введите оклад: '), input('Введите премию: '))
print(f'{p.get_full_name()}, {p.get_total_income()}')
