# ewallet
```commandline
python cli.py
Welcome to eWallet!
Enter "help" to list available commands.
> ?

Available commands: (type help <command>):
==========================================
EOF  create_wallet  draw_money  help  put_money  show_wallets  transfer_money

> create_wallet test1 10
Done
pk  owner  balance  limit
0  test1  0.0  10.0
> create_wallet test2 20
Done
pk  owner  balance  limit
1  test2  0.0  20.0
> put_money 1 19
Done
pk  owner  balance  limit
1  test2  19.0  20.0
> transfer_money 1 2 20
Error: wallet is not found.
> show_wallets
pk  owner  balance  limit
0  test1  0.0  10.0
1  test2  19.0  20.0
> transfer_money 1 0 20
Error: not enough funds in account.
> transfer_money 1 0 19
Error: account limit is reached.
> transfer_money 1 0 9.5
Done
pk  owner  balance  limit
1  test2  9.5  20.0
0  test1  9.5  10.0
```

## TODO
* add table output
* add argparse