# Assignment 1
# 1. Using any of the conditional statement learnt to write a simple 
# Python program that will output the score 
# and remark eg “Your score is 76 and this is Excellence” 
# using the algorithm below. Make sure that invalid score such 
# value greater than 100 or less than 1 are detected and reported
# 0 – 34 = Fail
# 35 – 44 = Pass
# 45 – 49 = Fair
# 50 – 59 = Good
# 60 – 69 = Very Good
# 70 – 100 = Excellence

score = 85

if score >= 0 and score < 35:
    grade = 'F'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 35 and score < 40:
    grade = 'E'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 40 and score < 45:
    grade = 'D'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 45 and score < 60:
    grade = 'C'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 60 and score < 70:
    grade = 'B'
    print(f'Your score is {score} and your grade is {grade}')
elif score >= 70 and score <= 100:
    grade = 'A'
    print(f'Your score is {score} and your grade is {grade}')
else:
    print(f'This score {score} is invalid')

# 2. Write a program in python that will print 
# the lowest number among three numbers supplied

num1 = 15
num2 = 25
num3 = 30

if num1 < num2 and num1 < num3:
    print(f'{num1} is less than {num2} and {num3}')
elif num2 < num1 and num2 < num3:
    print(f'{num2} is less than {num1} and {num3}')
elif num3 < num1 and num3 < num2:
    print(f'{num3} is less than {num1} and {num2}')

# Assignment 2
# 1. Create a multiplication table program using while loop, 
# this will be done in such a way that when a user supplies 
# any number the multiplication table of that number will be created.
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
number = 4

x = 1

while x in range(1, 13):
    result = number * x
    print(f'{number} X {x} = {result}')
    x += 1

    # 2. Write a program in python that tells if the name you supplied 
    # is in a list or the name is not in a list.

past_president = ['Jonathan', 'Buhari', 'Obasanjo', 'Babangida', 'Abacha']

name = 'jonathan'
president = name.capitalize()
if president in past_president:
    print(f'{president} was once the President of Nigeria')
else:
    print(f'{president} has not ruled Nigeria before')
    print('Here are the list of past Presidents')
    for p in past_president:
        print(p)

# 4. Write a program that sums all the numbers 
# in a list 10, 20, 30, 40, 70, 200, 300 and also determine the average.

numbers = [10, 20, 30, 40, 70, 200, 300]
total = 0
for num in numbers:
    total += num
print(f'The total is {total}')
avg = total/len(numbers)
print(f'The average is {avg}')


