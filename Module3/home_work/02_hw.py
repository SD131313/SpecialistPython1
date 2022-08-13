# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
n = int(input())
for i in range(n):
    numbers.append(random.randint(-100, 100))
print(numbers)
# Второй вариант
m = int(input())
numbers = []
h = [(numbers.append(random.randint(-100, 100))) for i in range(m)]
print (numbers)
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
