class account:
    """
    >>> a = account('John')
    >>> a.deposit(100)
    100
    >>> a.withdraw(50)
    50
    >>> a.withdraw(100)
    'Insufficient balance'
    """
    def __init__(self, account_holder):#Is the constctor in python
        self.balance = 0
        self.holder = account_holder
        #balance and holder are the data in the class
    def deposit(self, amount):
        self.balance = self.balace + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        else:
            self.balance = self.balance - amount
            return self.balance
