#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit29 exploit by SKane')

shell = ssh('bandit29', 'bandit.labs.overthewire.org', password='bbc96594b4e001778eee9975372716b2', port=2220)

sh = shell.run('sh')

sh.sendline('cat /tmp/gitclone1/repo/password.txt')

log.success("Password for bandit30: " + sh.recvline())
