"""
Exercise 3: The Digital Bank Account
 Your Task
       Create a BankAccount class:
          Attributes: account_holder (public) and __balance (make this private using double underscores).
          Initialize the balance to 0.0.
       Create Safe Methods:
          deposit(amount) — Only allow it if the amount is greater than 0.
          withdraw(amount) — Only allow it if the amount is greater than 0 and doesn't exceed the current balance. Otherwise, print an error.
       Create a Getter Method:
          Since __balance is private, create a method get_balance() that securely returns the current balance.
"""


class BankAccount:

    def __init__(self, account_holder, __balance=0.0):
        self.account_holder = account_holder
        self.__balance = __balance

    def deposits(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print(
                "Withdrawal amount must be greater than 0 and not exceed the current balance."
            )

    def getbalance(self):
        return self.__balance


b1 = BankAccount("Varun", 0.0)
b1.deposits(10.000)
b1.withdraw(2.000)

print(b1.getbalance())

b2 = BankAccount("Pranav", 0.0)
b2.deposits(5.000)

print(b2.getbalance())
