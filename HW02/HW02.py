# # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# # Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# # вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# import random

# number_of_coins = int(input("Введите количество монет: "))

# heads = 0
# tails = 0
# min_amount = 0
# for i in range(number_of_coins):
#     coins = random.randint(0, 1)
#     print(coins)
#     if coins == 0:
#         heads += 1
#     elif coins == 1:
#         tails += 1
# if heads < tails:
#     min_amount = heads
# elif tails < heads:
#     min_amount = tails
# elif tails == heads:
#     print("Нет минимального значения")
# print("Минимальное количество монет, которые нужно перевернуть", min_amount)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
# чисел S и их произведение P.Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму загаданных чисел: "))
p = int(input("Введите произведение загаданных чисел: "))
for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == s and x * y == p:
            print(x, y)