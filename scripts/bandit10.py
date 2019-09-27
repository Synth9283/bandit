#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit10 exploit by SKane')

shell = ssh('bandit10', 'bandit.labs.overthewire.org', password='truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk', port=2220)

sh = shell.run('sh')

sh.sendline("cat data.txt | base64 --decode | awk '{print $4}'")

log.success("Password for bandit11: " + sh.recvline())
