#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(3, 'строка 2')
print_params(b = 25)
print_params(c = [1,2,3])

#2
values_list = [5, 'Фасоль', True]
values_dict = {'a': 1, 'b': 'Флейта', 'c': False}

print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [5, 'Фагот']
print_params(*values_list_2, 42)