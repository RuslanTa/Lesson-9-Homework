a = int(input("Введите число А: "))
b = int(input("Введите число B: "))


def recursive(a, b):
    if a > b:
        print(a)
        recursive(a-1, b)
    elif a < b:
        print(b)
        recursive(a, b-1)
    else:
        print(a)

recursive(a, b)
