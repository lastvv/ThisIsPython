#2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

from itertools import accumulate
import operator

N = int(input('Введите любое число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))

print(get_prods(N))

