#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
        lst = [-5, 3, -2, 7, -8, 10, -4]
        # количество отрицательных элементов списка
        negative_count = len(list(filter(lambda x: x < 0, lst)))

        # находим индекс минимального по модулю элемента
        min_abs_index = lst.index(min(lst, key=abs))

        # сумма модулей элементов списка, расположенных после минимального по модулю элемента
        sum_after_min_abs = sum(
            map(abs, filter(lambda x: lst.index(x) > min_abs_index, lst)))

        # заменяем отрицательные элементы списка их квадратами
        lst = [x ** 2 if x < 0 else x for x in lst]

        # упорядочиваем элементы списка по возрастанию
        lst.sort()



    # пример использования

        print("Количество отрицательных элементов:", negative_count)
        print("Сумма модулей элементов после минимального по модулю элемента:",
           sum_after_min_abs)
        print("Упорядоченный список с квадратами отрицательных элементов:",
          lst)