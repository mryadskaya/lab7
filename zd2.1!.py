def main():
    a = list(map(float, input('Введите список чисел через пробел: ').split()))

negatives = sum([x < 0 for x in a])
min_index = min([i for i, x in enumerate(a , start=1) if abs(x) == min(abs(y) for y in a )])
sum_after_min = sum([abs(x) for i, x in enumerate(reversed(a), start=min_index) if i < len(a)])

new_list = [x ** 2 if x < 0 else x for x in a]
new_list.sort()

print("Количество отрицательных элементов: ", negatives)
print("Сумма модулей после минимального элемента: ", sum_after_min)
print('Замененные квадратами отрицательные элементы и упорядоченные по возрастанию: ')