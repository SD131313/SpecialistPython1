# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

n = int(input('n:'))
m = int(input('m:'))
k = int(input('k:'))
if k != (n * m):
    print('Да')
else:
    print('Нет')
