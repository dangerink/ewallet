# ewallet
CLI Example
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

Log example
```log
2018-10-14 15:02:48,898 INFO  Create new account test1 with 10.0 limit
2018-10-14 15:02:56,446 INFO  Starting 344a383d4c984fc8ab74d8f30b46e05a put args=(Wallet <0>, 20.0), kwargs={}
2018-10-14 15:02:56,446 ERROR Account 0 has reached the limit
2018-10-14 15:02:56,446 INFO  Finishing 344a383d4c984fc8ab74d8f30b46e05a
2018-10-14 15:03:13,289 INFO  Create new account test2 with 20.0 limit
2018-10-14 15:03:24,016 ERROR Account 2 is not found
2018-10-14 15:03:35,298 INFO  Starting 9e2ec9b471304438800749200f7d6f16 transfer args=(Wallet <0>, Wallet <1>, 20.0), kwargs={}
2018-10-14 15:03:35,298 INFO  Starting 648de257d7ff44dca1073e131c060b29 draw args=(Wallet <0>, 20.0), kwargs={}
2018-10-14 15:03:35,298 ERROR Account 0 has not enough funds
2018-10-14 15:03:35,299 INFO  Finishing 648de257d7ff44dca1073e131c060b29
2018-10-14 15:03:35,301 INFO  Finishing 9e2ec9b471304438800749200f7d6f16
2018-10-14 15:03:43,904 INFO  Starting 1d335b9694f6449aa3c2dafee01189c3 transfer args=(Wallet <0>, Wallet <1>, 9.5), kwargs={}
2018-10-14 15:03:43,904 INFO  Starting 151f53aa77ea4b51b6f38d889b6d8f56 draw args=(Wallet <0>, 9.5), kwargs={}
2018-10-14 15:03:43,904 ERROR Account 0 has not enough funds
2018-10-14 15:03:43,904 INFO  Finishing 151f53aa77ea4b51b6f38d889b6d8f56
2018-10-14 15:03:43,904 INFO  Finishing 1d335b9694f6449aa3c2dafee01189c3
2018-10-14 15:03:52,588 INFO  Starting 4b497442b37641a2a6135af12dd0fdf6 transfer args=(Wallet <1>, Wallet <0>, 9.5), kwargs={}
2018-10-14 15:03:52,588 INFO  Starting 7a5522c74283477ab0e79062352385ba draw args=(Wallet <1>, 9.5), kwargs={}
2018-10-14 15:03:52,588 ERROR Account 1 has not enough funds
2018-10-14 15:03:52,588 INFO  Finishing 7a5522c74283477ab0e79062352385ba
2018-10-14 15:03:52,588 INFO  Finishing 4b497442b37641a2a6135af12dd0fdf6
2018-10-14 15:04:08,283 INFO  Starting 06a4e98ce0da49c1b198c356a4a27d32 put args=(Wallet <1>, 19.0), kwargs={}
2018-10-14 15:04:08,283 INFO  Finishing 06a4e98ce0da49c1b198c356a4a27d32
2018-10-14 15:04:16,622 INFO  Starting 52a4dcf6a0a647f19366f03c2b6e7f3d transfer args=(Wallet <1>, Wallet <0>, 9.5), kwargs={}
2018-10-14 15:04:16,622 INFO  Starting ad3e990b39d64ce69e8c4ab09e61507c draw args=(Wallet <1>, 9.5), kwargs={}
2018-10-14 15:04:16,622 INFO  Finishing ad3e990b39d64ce69e8c4ab09e61507c
2018-10-14 15:04:16,622 INFO  Starting 29be9545c8274f99a6619d0ee4f6df74 put args=(Wallet <0>, 9.5), kwargs={}
2018-10-14 15:04:16,624 INFO  Finishing 29be9545c8274f99a6619d0ee4f6df74
2018-10-14 15:04:16,624 INFO  Finishing 52a4dcf6a0a647f19366f03c2b6e7f3d
2018-10-14 15:05:50,319 INFO  Starting 0edebbd79fd34cffa1beb4c700f40815 transfer args=(Wallet <1>, Wallet <0>, 9.0), kwargs={}
2018-10-14 15:05:50,319 INFO  Starting ca6dc2e4e85e466c967442a0512d5796 draw args=(Wallet <1>, 9.0), kwargs={}
2018-10-14 15:05:50,319 INFO  Finishing ca6dc2e4e85e466c967442a0512d5796
2018-10-14 15:05:50,319 INFO  Starting c30d982b4cff4959a833703ebfe44ce5 put args=(Wallet <0>, 9.0), kwargs={}
2018-10-14 15:05:50,319 ERROR Account 0 has reached the limit
2018-10-14 15:05:50,319 INFO  Finishing c30d982b4cff4959a833703ebfe44ce5
2018-10-14 15:05:50,319 INFO  Starting cc2c1a84a57140ad8ef35b2dc253ed3e _rollback args=(Wallet <1>, 9.0), kwargs={}
2018-10-14 15:05:50,319 INFO  Finishing cc2c1a84a57140ad8ef35b2dc253ed3e
2018-10-14 15:05:50,319 INFO  Finishing 0edebbd79fd34cffa1beb4c700f40815
```

## TODO
* add table output
* add argparse