class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0]) #первый аргумент
        return super().__new__(cls) #создание через базовый Класс

    def __init__(self, name, number_of_floors: int):
        self.name = name
        if not isinstance(number_of_floors, int):
            raise TypeError("Кол-во этаже должно быть целым числом")
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}.'

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history, h1, sep='\n')
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)