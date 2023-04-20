import math
list = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
list.sort()
X = sum(list) / len(list)
displist = []
for i in range(len(list)):
    disp = (list[i] - X)**2
    displist.append(disp)
s = math.sqrt(sum(displist) / len(list))
S = sum(displist) / (len(list) - 1)
D = sum(displist) / len(list)
print(*list, sep = ', ')
print(f'Среднее арифметическое равно: {round(X, 2)}')
print(f'Среднее квадратичное отклонение равно: {round(s, 2)}')
print(f'Несмещенная дисперсия равна: {round(S, 2)}')
print(f'Смещенная дисперсия равна: {round(D, 2)}')