immutable_var = (1, 2, 'A')
print(immutable_var)
#immutable_var[0] = 3
#print(immutable_var)
# кортеж не поддерживает обращение по элементам. Эелементы кортежа являются неизменяемыми за исключением списков в нутри картежа. Элемент списка внутри картежа можно изменить.
mutable_list = ([1, 2, 3], 1, 'F')
print(mutable_list)
mutable_list [0] [0] = 150
mutable_list [0] [1] = 250
mutable_list [0] [2] = 350
print(mutable_list)