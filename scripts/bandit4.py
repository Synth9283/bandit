#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit4 exploit by SKane')

shell = ssh('bandit4', 'bandit.labs.overthewire.org', password='pIwrPrtPN36QITSp3EQaw936yaFoFgAB', port=2220)

sh = shell.run('sh')

sh.sendline('cd inhere; strings ./*')

sh.recvline()

sh.recvline()

log.success("Password for bandit5: " + sh.recvline())
