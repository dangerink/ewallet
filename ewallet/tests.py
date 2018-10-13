import unittest

from .models import Wallet, NotEnoughFundsError, AccountLimitError


class TestWallet(unittest.TestCase):
    LIMIT = 100
    LIMIT_2 = 50
    DEFAULT_AMOUNT = 60

    def setUp(self):
        self.w1 = Wallet('Jim Beam', self.LIMIT)
        self.w2 = Wallet('John Galt', self.LIMIT_2)
        self.w1.put(self.DEFAULT_AMOUNT)

    def test_put(self):
        self.assertEqual(self.w1.balance, self.DEFAULT_AMOUNT)
        with self.assertRaises(AccountLimitError):
            self.w1.put(self.DEFAULT_AMOUNT)

    def test_draw(self):
        self.w1.draw(self.DEFAULT_AMOUNT)
        self.assertEqual(self.w1.balance, 0)
        with self.assertRaises(NotEnoughFundsError):
            self.w1.draw(self.DEFAULT_AMOUNT)

    def test_successful_transfer(self):
        amount = 20
        self.w1.transfer(self.w2, amount)
        self.assertEqual(self.w2.balance, amount)
        self.assertEqual(self.w1.balance, self.DEFAULT_AMOUNT - amount)

    def test_transfer_not_enough_funds(self):
        with self.assertRaises(NotEnoughFundsError):
            self.w1.transfer(self.w2, self.LIMIT)

    def test_transfer_rollback(self):
        with self.assertRaises(AccountLimitError):
            self.w1.transfer(self.w2, self.DEFAULT_AMOUNT)
        self.assertEqual(self.w1.balance, self.DEFAULT_AMOUNT)
        self.assertEqual(self.w2.balance, 0)
