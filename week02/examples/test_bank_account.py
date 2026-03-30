import unittest
from bank_account import BankAccount, InsufficientFundsError, NegativeAmountError


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice", balance=1000.0)

    def test_deposit_increases_balance(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500.0)

    def test_deposit_returns_new_balance(self):
        result = self.account.deposit(250)
        self.assertEqual(result, 1250.0)

    def test_deposit_negative_raises_error(self):
        with self.assertRaises(NegativeAmountError):
            self.account.deposit(-100)

    def test_deposit_zero_raises_error(self):
        with self.assertRaises(NegativeAmountError):
            self.account.deposit(0)

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800.0)

    def test_withdraw_returns_new_balance(self):
        result = self.account.withdraw(100)
        self.assertEqual(result, 900.0)

    def test_withdraw_exact_balance(self):
        result = self.account.withdraw(1000)
        self.assertEqual(result, 0.0)

    def test_withdraw_insufficient_funds_raises_error(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(9999)

    def test_withdraw_negative_raises_error(self):
        with self.assertRaises(NegativeAmountError):
            self.account.withdraw(-50)

    def test_initial_balance(self):
        acc = BankAccount("Bob", balance=500)
        self.assertEqual(acc.balance, 500)

    def test_default_balance_is_zero(self):
        acc = BankAccount("Bob")
        self.assertEqual(acc.balance, 0.0)

    def test_history_records_deposit(self):
        self.account.deposit(300)
        history = self.account.get_history()
        self.assertIn(("deposit", 300), history)

    def test_history_records_withdrawal(self):
        self.account.withdraw(100)
        history = self.account.get_history()
        self.assertIn(("withdrawal", 100), history)

    def test_history_is_empty_initially(self):
        acc = BankAccount("New")
        self.assertEqual(acc.get_history(), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)