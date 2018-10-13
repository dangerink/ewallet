from cmd import Cmd

from models import Wallet, WalletError


class Cli(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '
        self.intro = 'Welcome to eWallet!\nEnter "help" to list available commands.'
        self.doc_header = 'Available commands: (type help <command>):'

    def do_create_wallet(self, line):
        """create_wallet owner limit"""
        owner, limit = line.split()
        w = Wallet(owner, float(limit))
        self.write('Done')
        self.write_table(w.SHOW_PROPS, [w.prop_list])

    def do_show_wallets(self, line):
        """show_accounts [wallet_id]"""
        if line:
            wallet_id = int(line)
            try:
                w = Wallet.get_obj(wallet_id)
                self.write_table(w.SHOW_PROPS, [w.prop_list])
            except WalletError as e:
                self.write('Error: {0}'.format(str(e)))
        elif not Wallet.objects:
            self.columnize([])
        else:
            self.write_table(
                Wallet.SHOW_PROPS,
                [w.prop_list for _, w in sorted(Wallet.objects.iteritems(), key=lambda (k, v): k)]
            )

    def do_put_money(self, line):
        """put_money wallet_id amount"""
        w_id, amount = line.split()
        w_id = int(w_id)
        try:
            w = Wallet.get_obj(w_id)
            w.put(float(amount))
            self.write('Done')
            self.write_table(w.SHOW_PROPS, [w.prop_list])
        except WalletError as e:
            self.write('Error: {0}'.format(str(e)))

    def do_draw_money(self, line):
        """draw_money wallet_id amount"""
        w_id, amount = line.split()
        w_id = int(w_id)
        try:
            w = Wallet.get_obj(w_id)
            w.draw(float(amount))
            self.write('Done')
            self.write_table(w.SHOW_PROPS, [w.prop_list])
        except WalletError as e:
            self.write('Error: {0}'.format(str(e)))

    def do_transfer_money(self, line):
        """transfer_money from_wallet_id to_wallet_id amount"""
        from_w_id, to_w_id, amount = line.split()
        from_w_id, to_w_id = int(from_w_id), int(to_w_id)
        try:
            from_w = Wallet.get_obj(from_w_id)
            to_w = Wallet.get_obj(to_w_id)
            from_w.transfer(to_w, float(amount))
            self.write('Done')
            self.write_table(
                Wallet.SHOW_PROPS,
                [from_w.prop_list, to_w.prop_list]
            )
        except WalletError as e:
            self.write('Error: {0}'.format(str(e)))

    def do_EOF(self, line):
        """EOF -- exit eWallet"""
        self.stdout.write('Exiting...')
        exit(0)

    def emptyline(self):
        pass

    def write(self, s):
        self.stdout.write(s)
        self.stdout.write('\n')

    def write_table(self, headers, rows):
        if not rows:
            self.columnize([])
        else:
            self.columnize(headers)
            for row in rows:
                self.columnize(row)


if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print 'Exiting...'
