# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

from msilib import sequence

n = int(input('Введите какое-то число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 3) 
        for x 
            in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 3))