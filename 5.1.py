# 5.1
import sys

def calc():
    a = 0
    while True:
        b = int(input("Введите число: "))
        if b == -1: 
            print(f"Итоговая сумма: {a}")
            sys.exit(0)
        else:
            a += b
            print(f"Текущая сумма: {a}")

calc()