class Wallet(object):
    """ Digital wallet that allows an individual to make electronic transactions. """

    def __init__(self, owner, limit):
        self._owner = owner
        self.limit = limit
        self.balance = 0.0

    def transfer(self, other, amount):
        """ Transfer money to another account. """
        if self.balance - amount < 0 or other.balance + amount > other.limit:
            return False
        else:
            self.balance -= amount
            other.balance += amount
            return True
