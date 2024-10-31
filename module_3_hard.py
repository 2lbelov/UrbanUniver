data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    total_sum = 0
    for elem in data_structure:
        if isinstance(elem, int):
            total_sum += elem
        elif isinstance(elem, dict):
            total_sum += calculate_structure_sum(list(elem.keys()))
            total_sum += calculate_structure_sum(list(elem.values()))
        elif isinstance(elem, list) or isinstance(elem, tuple):
            total_sum += calculate_structure_sum(elem)
        elif isinstance(elem, str):
            total_sum += len(elem)
        elif isinstance(elem, set):
            total_sum += calculate_structure_sum(elem)
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)
