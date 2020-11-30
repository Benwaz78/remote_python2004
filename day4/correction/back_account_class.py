class BankAccount: 
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.email = lastname+'.'+firstname+'@company.com'
        self.form_email = self.email.lower()
        self.balance=[]
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 

    # def deposit_amount(self, amount):
    #     self.balance.append(amount)

    # def total_balance():
    #     for a in self.balance:
    #         self.balance += a
    #     print(self.balance)
         
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount, 'your balance is', self.balance) 
        else: 
            print("\n Insufficient balance  ") 

    def account_detail(self):
        return 'Users Detail \n Firstname: {} \n Lastname: {} \n Email: {} \n Balance: {}'.format(self.firstname,self.lastname,self.email, self.balance)

  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 

# http://purcellconsult.com/bank-account-class-example-in-python/

b = BankAccount('Benedict', 'Uwazie')
# print(b.deposit())
# print(b.deposit())
# print(b.deposit())
# print(b.deposit())

