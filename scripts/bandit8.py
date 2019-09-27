#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit8 exploit by SKane')

shell = ssh('bandit8', 'bandit.labs.overthewire.org', password='cvX2JJa4CFALtqS87jk27qwqGhBM9plV', port=2220)

sh = shell.run('sh')

sh.sendline('sort data.txt | uniq -u')

log.success("Password fr bandit9: " + sh.recvline())
