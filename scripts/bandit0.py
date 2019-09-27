#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit0 exploit by SKane')

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)

sh = shell.run('sh')

sh.sendline('cat readme')

log.success("Password for bandit1: " + sh.recvline())
