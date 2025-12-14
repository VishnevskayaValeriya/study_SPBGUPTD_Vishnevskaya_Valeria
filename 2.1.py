# 2.1
a = int(input("Введите номер месяца: "))
if a < 1 or a > 12:
    print("err")
elif a > 2 and a < 6:
    print("Весна")
elif a > 5 and a < 9:
    print("Лето")
elif a > 8 and a < 12:
    print("Осень")
else:
    print("Зима")