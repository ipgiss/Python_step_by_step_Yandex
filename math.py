# Функция для проверки, является ли число простым

# n = int(input('Введите число: '))
#
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# print(is_prime(n))

# Нахождения НОД и НОК двух чисел
import math

num1, num2 = int(input()), int(input())

# nok = abs(num1 * num2) // math.gcd(num1, num2)
#
# print(f'НОД({num1},{num2}) = {math.gcd(num1, num2)}')
# print(f'НОК({num1},{num2}) = {nok}')

'''Вариант через вызов функции'''


def NOK(a, b):  # 1. Определение функции
    return abs(a * b) // math.gcd(a, b)


result_nok = NOK(num1, num2)  # 2. Вызов функции с аргументами!

print(f'НОД({num1}, {num2}) = {math.gcd(num1, num2)}')
print(f'НОК({num1}, {num2}) = {result_nok}')
