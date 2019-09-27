#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit30 exploit by SKane')

shell = ssh('bandit30', 'bandit.labs.overthewire.org', password='5b90576bedb2cc04c86a9e924ce42faf', port=2220)

sh = shell.run('sh')

sh.sendline('cat /tmp/gitclone12/repo/password.txt')

log.success("Password for bandit31: " + sh.recvline())
