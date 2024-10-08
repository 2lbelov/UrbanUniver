grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades [0] = sum(grades[0]) / len(grades[0]) #находим среднее значение каждого элемента списка
grades [1] = sum(grades[1]) / len(grades[1])
grades [2] = sum(grades[2]) / len(grades[2])
grades [3] = sum(grades[3]) / len(grades[3])
grades [4] = sum(grades[4]) / len(grades[4])
#print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students) # преобразовываем множество в список
students.sort() # сортируем полученный список
#print(students)
avarege_score = dict(zip(students, grades)) # zip создаем кортеж (пару ключ и значение), dict преобразовываем кортеж в словарь
print(avarege_score)