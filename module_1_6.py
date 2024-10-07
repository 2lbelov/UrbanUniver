my_dict = {'Denis': 1978, 'Max': 1979, 'Anton': 1980}
print(my_dict)
print(my_dict.get('Denis'))
print(my_dict.get('Kamila', 'Такого имени нет'))
my_dict.update({'Sasha': 1981,
				'Alex':1982})
print(my_dict)
a = my_dict.pop('Max')
#print(my_dict)
print(a)
print(my_dict)
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', (1, 2, 3)}
print(my_set)
print(my_set.add(6))
print(my_set.add('Max'))
print(my_set)
print(my_set.discard(2))
print(my_set)