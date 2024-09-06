# Функция для нахождения НОД с использованием алгоритма Евклида
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ввод двух целых чисел
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Вычисление НОД
result = gcd(num1, num2)

# Вывод результата
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}.")