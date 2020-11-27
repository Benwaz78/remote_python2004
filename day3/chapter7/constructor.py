class Man():
    eyes = 2
    hand = 2
    leg = 2

    def __init__(self):
        print('This is a constructor')

    def details(self, name, color):
        return f'My name is {name} I am {color} with {self.eyes} eyes and {self.hand} hands'

m1 = Man()
print(m1.details('Benedict', 'Fair'))

