# Задача:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def reverse_coins(coins):
    n1 = 0
    n2 = 0
    for coin in coins:
        if coin:
            n1 += 1
        else:
            n2 += 1
    return min(n1, n2)


print(reverse_coins([]) == 0)
print(reverse_coins([1, 0, 1, 1, 1]) == 1)
print(reverse_coins([1, 1, 1, 1, 1]) == 0)
print(reverse_coins([1, 0, 1, 0, 1]) == 2)


# Задача:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
def get_nums(sum_nums, p):
    n1 = 0
    n2 = 0
    for i in range(1, sum_nums):
        for j in range(1, sum_nums):
            if i * j == p and i + j == sum_nums:
                n1 = i
                n2 = j
                break
        if n1:
            break
    return n1, n2


print(get_nums(0, 0) == (0, 0))
print(get_nums(8, 15) == (3, 5))
print(get_nums(41, 390) == (15, 26))


# Задача:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def print_sqr_of_2(n):
    if n <= 0:
        print('Введите натуральное число')
    k = 0
    while True:
        current_n = 2 ** k
        if current_n <= n:
            print(current_n)
        else:
            break
        k += 1


print_sqr_of_2(50)