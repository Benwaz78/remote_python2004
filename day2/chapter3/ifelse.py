
# a = 5
# b = 3

# if a < b:
#     print('b is greater than a')
# else:
#     print('a is greater than b')

# name = input('Enter name: ')
# age = int(input('Enter age: '))
# age_limit = 18

# if age >= age_limit:
#     print(f'{name} is allowed to watch this kind of movie')
# else:
#     print(f'Hey! {name} your age is {age} and hence you are under age')

# write a progam that will check if a username and password matches
# a specified username and password, and prints "Welcome to site dashboard"
# if the condition is true and also print "Username and Password do not match" 


username = input('Enter Username: ')
password = input('Enter Password: ')

check_username = 'benedict'
check_pasword = 'pass1234567'

if username.lower() == check_username and password.lower() == check_pasword:
    print('Welcome to site dashboard')
else:
    print('Username and Password do not match')

