"""OBJECT ORIENTED LAB"""
class BankAccount(object):
    """Bankaccount class with methods withdraw and deposit"""
    def __init__(self):
        pass
    def withdraw():
        pass
    def deposit():
        pass
class SavingsAccount(BankAccount):
    """Class saving account that inherits from bank account"""
    def __init__(self):
        balance = 500
    def deposit(self, deposit):
        if deposit > 0:
            balance += deposit
            return balance
        else:
            return "Invalid deposit amount"

    



