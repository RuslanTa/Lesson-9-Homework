a = int(input("Введите число А: "))
b = int(input("Введите число B: "))


def recursive(a, b):
    if a > b:
        if a == b:
            print(a)
        else:
            print(a)
            recursive(a-1, b)
    else:
        if a < b:
            if a == b:
                print(a)
            else:
                recursive(a, b-1)
                print(b)


recursive(a, b)
