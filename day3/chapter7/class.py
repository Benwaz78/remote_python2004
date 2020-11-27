class Man():
    eyes = 2
    hand = 2
    leg = 2

    def details(self, name, color):
        return f'My name is {name} I am {color} with {self.eyes} eyes and {self.hand} hands'


m1 = Man()
print(m1.eyes)
print(m1.hand)
print(m1.details('Benedict', 'Fair'))
m2 = Man()
print(m2.eyes)
print(m2.hand)
print(m2.details('Alabi', 'Dark'))



    