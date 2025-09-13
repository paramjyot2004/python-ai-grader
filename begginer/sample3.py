class BankAccount:
    """Bank account class with basic operations"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance  # Should be private
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history.copy()

# Usage example
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")

# Issues to identify:
# 1. Balance should be private (_balance)
# 2. No input validation for account_number
# 3. No error handling or custom exceptions
# 4. Transaction history could be more detailed (timestamps, etc.)
# 5. No string representation methods (__str__, __repr__)
# 6. Could benefit from property decorators
