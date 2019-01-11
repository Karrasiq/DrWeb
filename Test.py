# Написать функцию, возвращающую четные элементы последовательности фиббоначи
# f(4) вернет 0,2,8,34


def f(count):
    f_list = []
    num1, num2 = 0, 1
    while count:
        if num1 % 2 == 0:
            f_list.append(num1)
            count -= 1
        num1, num2 = num2, num1 + num2
    else:
        return f_list


print(f(4))
