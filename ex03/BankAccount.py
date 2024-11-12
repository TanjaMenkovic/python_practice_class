class BankAccount:
    def __init__(self, initial_balance: float = 0.0) -> None:
        self.__balance: float = initial_balance
    
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Invalid amount to withdraw.")
        elif amount > self.__balance:
            print("Not enough money on account.")
        else:
            self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance

account = BankAccount(100)
print("Current balance is: ", account.get_balance())
account.deposit(50)
print("After deposit 50, balance is: ", account.get_balance())
account.withdraw(30)
print("After withdrawing 30, balance is: ", account.get_balance())
account.withdraw(200)  # Output: "Insufficient balance."
print("After withrowing 200, balance is: ", account.get_balance())