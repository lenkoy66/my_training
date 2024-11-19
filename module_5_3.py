class House:
    def __init__(self, name, number_of_floors: int):
        self.name = name
        if not isinstance(number_of_floors, int):
            raise TypeError("Кол-во этаже должно быть целым числом")  #степик
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
        return f'Название {self.name}, количество этажей: {self.number_of_floors}.'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self  #или return House(self.name, self.number_of_floors + value)
        if isinstance(value, House): #возможность суммировать этажи разных экземпляров
            self.number_of_floors = self.number_of_floors + value.number_of_floors  #если это экземпляр класса, то берем значение
            return self

    def __radd__(self, value):
        return self.__add__(value) #или

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__ --> h1.number_of_floors = h2.number_of_floors

h1 = h1 + 10 # __add__ --> h1.__add__(10)
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__ --> h1.__iadd__(10)
print(h1)

h2 = 10 + h2 # __radd__ --> h2.__radd__(10)
print(h2)

print(h1 > h2) # __gt__ --> h1.number_of_floors > h2.number_of_floors
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

#проверка add (сумма этажей экземпляров Класса)
floors = len(h1) + len(h2) #len - кол-во этажей в экземпляре
h3 = h1 + h2
print(floors, h3, sep='\n') #хе-хе

#проверка кол-во этажей на int:
# h3 = House('ЖК Эльбрус 2', '10')
# print(h3)

#сравнение кол-ва этажей с произвольным числом:
print(h1 == 10) #--> none. добавила условие

#для себя:
print(h1 > h2)
print(h1.number_of_floors > h2.number_of_floors)
