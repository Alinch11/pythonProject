def input_list():
    while True:
        try:
            my_list = input('Введите последовательность чисел через пробел: ')
            list1 = list(map(int, my_list.split()))
            for a in list1:
                if len(list1) >= 2:
                    return list1
                else:
                    raise ValueError
        except ValueError:
            print('В введенной последовательности есть элементы, которые не являются числами или вы ввели одно число.')


list2 = input_list()
min_num = min(list2)
max_num = max(list2)


def input_number_in_range(start, end):
    while True:
        try:
            my_number = int(input(f'Введите число в диапазоне от {min_num} до {max_num}: '))
            if start < my_number < end:
                return my_number
                # print('OK')
                break
            else:
                raise ValueError
        except ValueError:
            print("Вы ввели не число или число не входит в указанный диапазон. Попробуйте еще раз.")


checked_number = input_number_in_range(min_num, max_num)


def sorting_list(list2):
    for i in range(len(list2)):
        for j in range(len(list2) - i - 1):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]
    return list2


sorted_list = sorting_list(list2)
print(sorted_list)


#
def binary_search_first(sorted_list, checked_number):
    first = 0
    last = len(sorted_list)
    while first < last - 1:
        mid = (first + last) // 2
        if checked_number > sorted_list[mid]:
            first = mid
        else:
            last = mid
    d = dict();
    d['Индекс элемента, который меньше введенного числа'] = first
    d['Индекс элемента, который больше или равен введенного числа'] = last
    return d


from pprint import pprint


pprint(binary_search_first(sorted_list, checked_number))