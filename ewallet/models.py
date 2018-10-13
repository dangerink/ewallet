class WalletError(Exception):
    """Base wallet error."""

    def __init__(self, *args, **kwargs):
        super(WalletError, self).__init__(self.__doc__.lower(), *args, **kwargs)


class NotEnoughFundsError(WalletError):
    """Not enough funds in account."""


class AccountLimitError(WalletError):
    """Account limit is reached."""


class WalletNotFoundError(WalletError):
    """Wallet is not found."""


class ModelMeta(type):
    """Provides simple object manager and set object PK counter to class."""

    def __init__(cls, *args, **kwargs):
        super(ModelMeta, cls).__init__(*args, **kwargs)
        cls.objects = {}
        cls._pk_counter = 0


class Model(object):
    """Base model."""

    __metaclass__ = ModelMeta

    PK_NAME = 'pk'
    SHOW_PROPS = ()

    def __new__(cls, *args, **kwargs):
        # Add a newly created object to object manager
        obj = super(Model, cls).__new__(cls, *args, **kwargs)
        setattr(obj, cls.PK_NAME, cls._pk_counter)
        cls.objects[cls._pk_counter] = obj
        cls._pk_counter += 1
        return obj

    @property
    def prop_list(self):
        return [str(getattr(self, prop)) for prop in self.SHOW_PROPS]

    @classmethod
    def get_obj(cls, obj_pk):
        w = cls.objects.get(obj_pk)
        if w is None:
            raise WalletNotFoundError
        return w


class Wallet(Model):
    """Digital wallet that allows an individual to make electronic transactions."""
    SHOW_PROPS = ('pk', 'owner', 'balance', 'limit')

    def __init__(self, owner, limit):
        self._owner = owner
        self._limit = limit
        self._balance = 0.0

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
