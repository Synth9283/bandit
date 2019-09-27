#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit22 exploit by SKane')

shell = ssh('bandit22', 'bandit.labs.overthewire.org', password='Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI', port=2220)

sh = shell.run('sh')

sh.sendline('cat /tmp/8ca319486bfbbc3663ea0fbe81326349')

log.success("Password for bandit23: " + sh.recvline())
