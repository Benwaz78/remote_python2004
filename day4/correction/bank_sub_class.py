from back_account_class import BankAccount

class SubBankAccount(BankAccount):

    def __init__(self, firstname, lastname, principal, time, rate):
        super().__init__(firstname, lastname)
        self.principal = principal
        self.time = time
        self.rate = rate
    

    def interest(self):
        interest = (self.principal * (self.time/12) * self.rate)/100
        return interest


s1 = SubBankAccount('Chinonso', 'Uwazie', 200000, 6, 0.1)
print(s1.interest())

