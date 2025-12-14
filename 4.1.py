# 4.1
A = int(input("Число A: "))
B = int(input("Число B: "))

if A < B:
    for i in range(A, B + 1):
        print(i, " ")
else:
    for i in range(A, B - 1, -1):
        print(i, " ")
