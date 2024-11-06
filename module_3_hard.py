def calculate_structure_sum(data_structure):
    count = 0
    if isinstance(data_structure, int):
        count += data_structure
    if isinstance(data_structure, str):
        count += len(data_structure)

    if isinstance(data_structure, list):
        for i in data_structure:
            count += calculate_structure_sum(i)
    if isinstance(data_structure, tuple):
        for i in data_structure:
            count += calculate_structure_sum(i)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            count += calculate_structure_sum(key)
            count += calculate_structure_sum(value)
    if isinstance(data_structure, set):
        for i in data_structure:
            count += calculate_structure_sum(i)
    return count


data_structure1 = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure1)
print(result)
