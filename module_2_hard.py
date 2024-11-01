def result(number):
    pass_result = []
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pair = [i, j]
                pass_result.append(pair)
    return pass_result

n = int(input("Введите число n (от 3 до 20): "))
if n < 3:
    print('Неверное число')
else:
    print(result(n))