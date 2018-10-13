class NotEnoughFundsError(Exception):
    """ Not enough funds in account. """


class AccountLimitError(Exception):
    """ Account limit is reached. """


class ModelMeta(type):
    """ Provides simple object manager and set object PK counter to class. """

    def __init__(cls, *args, **kwargs):
        super(ModelMeta, cls).__init__(*args, **kwargs)
        cls.objects = {}
        cls._pk_counter = 0


class Model(object):
    """ Base model. Sets primary key, increase it and add new instance to object manager. """

    __metaclass__ = ModelMeta

    PK_NAME = 'pk'

    def __new__(cls, *args, **kwargs):
        obj = super(Model, cls).__new__(cls, *args, **kwargs)
        setattr(obj, cls.PK_NAME, cls._pk_counter)
        cls.objects[cls._pk_counter] = obj
        cls._pk_counter += 1
        return obj


class Wallet(Model):
    """ Digital wallet that allows an individual to make electronic transactions. """

    def __init__(self, owner, limit):
        self._owner = owner
        self._limit = limit
        self._balance = 0

    def put(self, amount):
        """ Put money into account. """
        if self._balance + amount > self._limit:
            raise AccountLimitError()
        else:
            self._balance += amount

    def draw(self, amount):
        """ Draw money from account. """
        if self._balance - amount < 0:
            raise NotEnoughFundsError
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
        except AccountLimitError as e:
            self._rollback(amount)
            raise e

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @property
    def limit(self):
        return self._limit
