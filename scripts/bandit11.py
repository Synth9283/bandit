#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit11 exploit by SKane')

shell = ssh('bandit11', 'bandit.labs.overthewire.org', password='IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR', port=2220)

sh = shell.run('sh')

sh.sendline("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | awk '{print $4}'")

log.success("Password for bandit12: " + sh.recvline())
