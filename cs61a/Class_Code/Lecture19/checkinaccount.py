class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self ,amount):#If you have self in the function, then it bound method, which indepent in object
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"
        
class CheckingAccount(Account):
    interest = 0.01
    bank_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.bank_fee)
    
class bank:
    """ A example to differ compostition from inheritance
        Inheritance is "is-a" property
        Composition is "has-a" property
        Bank "has" accounts

        >>> bank = Bank()
        >>> john = bank.open_account('John', 10)
        >>> jack = bank.open_account('Jack', 5, CheckingAccount)
        >>> john.interest
        0.02
        >>> jack.interest
        0.01
        >>> bank.pay_interest()
        >>> john.balance
        10.2
    """
    
    def __init__(self):
        self.accounts = []#To store the accounts
    def open_account(self, holder, amount, type = Account):
        account = type(holder)
        #avoid not to directly change the data in the constructor instead of using the bound fuction
        account.deposit(amount)
        self.accounts.append(account)
        return self.accounts
    def pay_interest(self):
        #This function is to loop through all the account and give them the interest according to their's interest_rate
        for i in self.accounts:
            interest = i.balance * i.interest
            i.deposit(interest)