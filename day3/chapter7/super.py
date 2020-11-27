class Employee():
    pay_raise = 0.5

    def __init__(self, first_name, last_name, pay):
        self.p = pay
        self.name = first_name
        self.last = last_name
        self.mail = self.name+'.'+self.last+'@alabian.com'
        self.email = self.mail.lower()

    def salary(self):
        increase = self.p * self.pay_raise
        salary = self.p + increase
        return salary

class Developer(Employee):
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog = prog_lang

    def details(self):
        return f'{self.name} {self.last} {self.email}, {self.prog}'


d1 = Developer('Benedict', 'Uwazie', 1200, 'Python')
print(d1.email)
print(d1.salary())
print(d1.details())





