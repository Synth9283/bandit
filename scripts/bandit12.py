#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit12 exploit by SKane')

shell = ssh('bandit12', 'bandit.labs.overthewire.org', password='5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu', port=2220)

sh = shell.run('sh')

sh.sendline("cat /tmp/hackdose/data8 | awk '{print $4}'")

log.success("Password for bandit13: " + sh.recvline())
