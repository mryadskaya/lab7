lst = [-3.5, 2.7, -1.8, 4.2, -5.9, 0.1, -2.4]

count_negative = len([x for x in lst if x < 0])
print("Количество отрицательных элементов списка:", count_negative)

min_absolute = min(lst, key=abs)
sum_after_min = sum([abs(x) for x in lst[lst.index(min_absolute)+1:]])
print("Сумма модулей элементов списка, расположенных после минимального по модулю элемента:", sum_after_min)

square_lst = [x2 if x < 0 else x for x in lst]
sorted_lst = sorted(square_lst)
print("Список после замены отрицательных элементов на их квадраты и упорядочивания по возрастанию:")
print(sorted_lst)