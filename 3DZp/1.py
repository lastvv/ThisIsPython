# Задайте список из нескольких чисел.
# Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции

def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [1, 2, 3, 4, 5]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)