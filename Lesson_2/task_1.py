"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def calcul_method():
    system_check = input('Введите +, -, *, / или 0 для выхода: ')
    if system_check not in ['+', '-', '*', '/', '0']:
        print('Введите другой знак, не подходит')
        return calcul_method()

    if system_check == '0':
        return f'Вы вышли из проги.'

    try:
        num_1 = float(input('Введите первое число: '))
        num_2 = float(input('Введите второе число: '))
    except ValueError:
        print(f'Алерт! Не число')
        return calcul_method()

    if system_check == '+':
        print(f'Answer: {num_1 + num_2}')
        return calcul_method()
    if system_check == '-':
        print(f'Answer: {num_1 - num_2}')
        return calcul_method()
    if system_check == '*':
        print(f'Answer: {num_1 * num_2}')
        return calcul_method()
    if system_check == '/':
        try:
            print(f'Answer: {num_1 / num_2}')
            return calcul_method()
        except ZeroDivisionError:
            print('Деление на ноль, исправьте ситуацию')
            return calcul_method()

print(calcul_method())
