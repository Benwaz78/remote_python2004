
def office(name, color='Yellow'):
    print(f'The name of this office is {name} and the color is {color}')

office('MTN')
office('Alabian', 'Sky Blue')


def multiplication(number, start=1, stop=12):
    while start in range(start, stop+1):
        result = number * start
        print(f'{number} X {start} = {result}')
        start += 1

multiplication(2)
multiplication(3, 5, 15)
multiplication(4, 3)

def greeting():
    print('Hello people!!')

greeting()
