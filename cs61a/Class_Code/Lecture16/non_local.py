def make_withdraw(balance):
    def withdraw(number):
        nonlocal balance
        balance = balance - number
        return balance
    return withdraw