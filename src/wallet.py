class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
        print(self.balance)

A = Wallet()
# A.spend_cash(0)
# A.add_cash(10)

def f1():
    x = 1
    y = 2
    print('Okay')
    return x + y

f1()

