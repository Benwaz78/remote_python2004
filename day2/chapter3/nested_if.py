
name = input('Enter name: ')
gender = input('Enter gender: ')
lowercase_gender = gender.capitalize()

if len(name) > 5:
    if lowercase_gender == 'Male':
        print(f'Welcome {name} your gender is {lowercase_gender}')
    else:
        print(f'Welcome {name} you are a Female')
else:
    print(f'Your name is less than 5')
