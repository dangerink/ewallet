class NotEnoughFundsException(Exception):
    """ Not enough funds in account. """


class AccountLimitException(Exception):
    """ Account limit is reached. """


class Wallet(object):
    """ Digital wallet that allows an individual to make electronic transactions. """

    def __init__(self, owner, limit):
        self._owner = owner
        self._limit = limit
        self._balance = 0

    def put(self, amount):
        """ Put money into account. """
        if self._balance + amount > self._limit:
            raise AccountLimitException()
        else:
            self._balance += amount

    def draw(self, amount):
        """ Draw money from account. """
        if self._balance - amount < 0:
            raise NotEnoughFundsException
        else:
            self._balance -= amount

    def _rollback(self, amount):
        """ Rollback draw in case of error. """
        self._balance += amount

    def transfer(self, other, amount):
        """ Transfer money to another account. """
        try:
            self.draw(amount)
            other.put(amount)
        except AccountLimitException as e:
            self._rollback(amount)
            raise e

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner
