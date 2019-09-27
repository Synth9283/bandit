#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit7 exploit by SKane')

shell = ssh('bandit7', 'bandit.labs.overthewire.org', password='HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs', port=2220)

sh = shell.run('sh')

sh.sendline("cat data.txt | grep millionth | awk '{print $2}'")

log.success("Password for bandit8: " + sh.recvline())
