from cmd import Cmd

from models import Wallet


class Cli(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '
        self.intro = 'Welcome to eWallet!\nEnter "help" to list available commands.'
        self.doc_header = 'Available commands: (type help <command>):'

    def do_create_account(self, line):
        """create_account owner limit\nCreate a new account in eWallet."""
        owner, limit = line.split()
        w = Wallet(owner, limit)
        self.stdout.write(
            'Account created: {0}: limit = {1}'.format(w.owner, w.limit)
        )
        self.stdout.write('\n')

    def do_show_accounts(self, line):
        """show_accounts\nDisplay all existing eWallet accounts."""
        if not Wallet.objects:
            self.columnize([])
        else:
            self.columnize(Wallet.SHOW_KEYS)
            for _, wal in sorted(Wallet.objects.iteritems(), key=lambda (k, v): k):
                self.columnize([str(getattr(wal, key)) for key in Wallet.SHOW_KEYS])

    def do_EOF(self, line):
        self.stdout.write('Exiting...')
        exit(0)

    def emptyline(self):
        pass


if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print 'Exiting...'
