# num1 = 10
# num2 = 0
# divide = num1/num2
# print(divide)

# try:
#     num1 = 10
#     num2 = 0
#     divide = num1/num2
#     print(divide)
# except ZeroDivisionError as z_error:
#     error = open('error.txt', 'a')
#     error.write('\n'+ f'An error occured which is {z_error}')
#     print(f'An error occured which is {z_error}')

# try:
#     file = open('file.txt', 'r')
#     file.read()
# except FileNotFoundError as f:
#     print(f'file does not exist {f}')

try:
    num1 = 10
    num2 = 2
    divide = num1/num2
    print(divide)

    file = open('file.txt', 'r')
    file.read()
except ZeroDivisionError as z_error:
    error = open('error.txt', 'a')
    error.write('\n' + f'An error occured which is {z_error}')
    print(f'An error occured which is {z_error}')
except FileNotFoundError as f:
    print(f'file does not exist {f}')
