
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. Balance is only ${balance:.2f}."
        )

class NegativeAmountError(Exception):
    """Raised when a negative amount is provided."""
    pass

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = balance
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Deposit amount must be positive.")
        self._balance += amount
        self._transactions.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= amount
        self._transactions.append(("withdrawal", amount))
        return self._balance

    def get_history(self):
        return self._transactions.copy()

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"


if __name__ == "__main__":
    acc = BankAccount("Alice", 1000)
    print(acc)

    acc.deposit(500)
    print(f"After deposit: ${acc.balance:.2f}")

    acc.withdraw(200)
    print(f"After withdrawal: ${acc.balance:.2f}")

    try:
        acc.withdraw(9999)
    except InsufficientFundsError as e:
        print(f"Error: {e}")

    try:
        acc.deposit(-100)
    except NegativeAmountError as e:
        print(f"Error: {e}")

    print("Transaction history:", acc.get_history())