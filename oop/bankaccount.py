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
        self.balance = 500

    def deposit(self, deposit):
        """Returns the current  balance"""
        if deposit > 0:
            self.balance += deposit
            return self.balance
        else:
            return "Invalid deposit amount"
    def withdraw(self, withdraw):
        if((self.balance - withdraw) > 0) and ((self.balance - withdraw) < 500): 
            return "Cannot withdraw beyond the minimum account balance"
        elif (self.balance - withdraw) < 0:
            return "Cannot withdraw beyond the current account balance"
        elif withdraw < 0:
            return "Invalid withdraw amount"
        else:
        	self.balance -= withdraw
        	return self.balance
            
class CurrentAccount(BankAccount):
    """Implementing class Current account"""
    def __init__(self):
        self.balance = 0
    def deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit
            return self.balance
        else:
            return "Invalid deposit amount."
    def withdraw(self, withdraw):
        if withdraw > 0:
            if withdraw > self.balance:
                return "Cannot withdraw beyond the current account balance"
            else:
            	self.balance -= withdraw
            	return self.balance
        else:
            return "Invalid withdraw amount"
    
    



