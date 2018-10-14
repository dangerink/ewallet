from logger import logger


class WalletError(Exception):
    """Base wallet error."""

    log_message_template = ''

    def __init__(self, wallet_id, *args, **kwargs):
        super(WalletError, self).__init__(self.__doc__.lower(), *args, **kwargs)
        if self.log_message_template:
            logger.error(self.log_message_template.format(wallet_id))


class NotEnoughFundsError(WalletError):
    """Not enough funds in account."""
    log_message_template = 'Account {0} has not enough funds'


class AccountLimitError(WalletError):
    """Account limit is reached."""
    log_message_template = 'Account {0} has reached the limit'


class WalletNotFoundError(WalletError):
    """Wallet is not found."""
    log_message_template = 'Account {0} is not found'


class ModelMeta(type):
    """Provides simple object manager and set object PK counter to class."""

    def __init__(cls, *args, **kwargs):
        super(ModelMeta, cls).__init__(*args, **kwargs)
        cls.objects = {}
        cls._pk_counter = 0


class Model(object):
    """Base model."""

    __metaclass__ = ModelMeta

    PK_PROP = 'id'
    SHOW_PROPS = ()

    def __new__(cls, *args, **kwargs):
        # Add a newly created object to object manager
        obj = super(Model, cls).__new__(cls, *args, **kwargs)
        setattr(obj, cls.PK_PROP, cls._pk_counter)
        cls.objects[cls._pk_counter] = obj
        cls._pk_counter += 1
        return obj

    @property
    def pk(self):
        return getattr(self, self.PK_PROP)

    @property
    def prop_list(self):
        return [str(getattr(self, prop)) for prop in self.SHOW_PROPS]

    @classmethod
    def get_obj(cls, obj_pk):
        obj = cls.objects.get(obj_pk)
        if obj is None:
            raise WalletNotFoundError(obj_pk)
        return obj


class Wallet(Model):
    """Digital wallet that allows an individual to make electronic transactions."""
    SHOW_PROPS = ('pk', 'owner', 'balance', 'limit')

    def __init__(self, owner, limit):
        self._owner = owner
        self._limit = limit
        self._balance = 0.0
        logger.info('Create new account {0} with {1} limit'.format(owner, limit))

    def put(self, amount):
        """ Put money into account. """
        if self._balance + amount > self._limit:
            raise AccountLimitError(self.pk)
        else:
            self._balance += amount
        logger.info('Put {0} into account {1}'.format(amount, self.pk))

    def draw(self, amount):
        """ Draw money from account. """
        if self._balance - amount < 0:
            raise NotEnoughFundsError(self.pk)
        else:
            self._balance -= amount
        logger.info('Draw {0} into account {1}'.format(amount, self.pk))

    def transfer(self, other, amount):
        """ Transfer money to another account. """
        try:
            self.draw(amount)
            other.put(amount)
            logger.info('Transfer {0} from {1} into account {2}'.format(amount, self.pk, other.pk))
        except AccountLimitError as e:
            self._rollback(amount)
            raise e

    def _rollback(self, amount):
        """ Rollback draw in case of error. """
        self._balance += amount
        logger.info('Rollback {0} to account {1}'.format(amount, self.pk))

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @property
    def limit(self):
        return self._limit
