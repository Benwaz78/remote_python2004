class Employee():
    pay_raise = 0.1

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

staff1 = Employee('Benedict', 'Uwazie', 1000)
print(staff1.name)
print(staff1.email)
print(staff1.salary())
staff2 = Employee('Alabi', 'Adebayo', 2000)
print(staff2.email)
print(staff2.salary())


