# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Найтии и вывести сумму элементов
    s = sum([a for a in A if a > 3 and a < 8 and i % 10 == 0] )
    print(s)