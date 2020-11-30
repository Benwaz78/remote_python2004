# Create three variables and call them firstname, lastname, surname
# supply data to this variables using input and enter the data inside
# a file class classwork.txt

firstname = input('Enter firstname: ')
lastname = input('Enter lastname: ')
middlename = input('Enter middlename: ')

file = open('muda.txt', 'a')
# result = f'{firstname} {lastname} {middlename}'
# file.write('\n' + result)
file.write('\n'+ 'Firstname: '+firstname)
file.write('\n' + 'Lastname: '+lastname)
file.write('\n' + 'Middlename: '+ middlename)

