"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

#1ый вариант решения - O(N) - квадратичная сложность
comp_dict = {'Samsung': 3000000, 'Apple':  4500000, 'Nokia': 1000000, 'Xiomi': 3300000, 'Motorola': 500000}
while len(comp_dict) != 3:
    check_amount = 100000000
    check_word = []
    for el in comp_dict:
        if check_amount > comp_dict[el]:
            check_amount = comp_dict[el]
            check_word.append(el)
    del comp_dict[check_word[-1]]
    check_word.clear()
print(comp_dict)

#2ой вариант решения   - 0(N) - кубическая сложность
comp_list = [['Samsung', 3000000], ['Apple', 4500000], ['Nokia', 1000000], ['Xiomi', 3300000], ['Motorola', 500000]]
lst_word = {}
while len(lst_word) != 3:
    max_value = 0
    for i in range(len(comp_list)):
        if max_value < comp_list[i][1]:
            max_value = comp_list[i][1]

    for i in range(len(comp_list)):
        if max_value == comp_list[i][1]:
            lst_word[comp_list[i][0]] = comp_list[i][1]
            comp_list.pop(i)
            break

print(lst_word)

#Вывод: использование варианта первого с квадратической сложностью является более эффективным методом, чем 2го варианта
# с кубической сложностью, т.к. для исполнения кубической сложности затрачивается больше времени на исполнение.