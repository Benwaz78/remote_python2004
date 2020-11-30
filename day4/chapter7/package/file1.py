def my_range(start, stop):
    total = 0
    for x in range(start, stop+1):
        total += x
    print(total)


def smallest_number(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        print(f'{num1} is less than {num2} and {num3}')
    elif num2 < num1 and num2 < num3:
        print(f'{num2} is less than {num1} and {num3}')
    elif num3 < num1 and num3 < num2:
        print(f'{num3} is less than {num1} and {num2}')
