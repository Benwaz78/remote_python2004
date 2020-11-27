num1 = 5
num2 = 7
add = num1 + num2
print(add)
def add(para1, para2):
    add = para1 + para2
    print(add)

add(10, 5)
add(3, 5)

# Create a function that will take name, age, color as parameters
# and use it to form a sentence. Call this new funtion three times
# with different arguments

def person(name, age, color):
    print(f'My name is {name} and my age is {age} and color is {color}')

person('Benedict', 45, 'Fair')
person('Alabi', 29, 'Dark')
person('Joshua', 20, 'Chocolate')

# while x in range(1, 13):
#     result = number * x
#     print(f'{number} X {x} = {result}')
#     x += 1


def multiplication(number, start, stop):
    while start in range(start, stop):
        result = number * start
        print(f'{number} X {start} = {result}')
        start += 1


multiplication(4, 3, 15)
multiplication(3, 1, 10)

numbers = [10, 20, 30, 40, 70, 200, 300]
total = 0
for num in numbers:
    total += num
print(f'The total is {total}')
avg = total/len(numbers)
print(f'The average is {avg}')

def my_avg(benedict_num):
    '''
    This function expects a list
    as an argument
    '''
    total = 0
    for num in benedict_num:
        total += num
    avg = total/len(benedict_num)
    print(avg)

my_avg([5, 10, 15, 20, 25, 30])
list_nums = [2, 4, 6, 8, 10, 12]
my_avg(list_nums)

# num = [5, 10, 15, 20, 25, 30]
# for n in num:
#     print(n)


# area = 0.5 * base * height
# area_of_circle = 3.142 * r^2
# perimetrer of rectangle = 2(L + W)

def area(base, height):
    area = 0.5 * base * height
    print(area)

area(100, 50)

def area_circle(r):
    area = 3.142 * r*r
    print(area)

def perimetrer_rectangle(length, width):
    perimeter = 2*(length + width)
    print(perimeter)

area_circle(5)
area_circle(7)

perimetrer_rectangle(100, 25)
perimetrer_rectangle(50, 25)
