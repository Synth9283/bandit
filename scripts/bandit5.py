#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit5 exploit by SKane')

shell = ssh('bandit5', 'bandit.labs.overthewire.org', password='koReBOKuIDDepwhWk7jZC0RTdopnAYKh', port=2220)

sh = shell.run('sh')

sh.sendline('strings inhere/maybehere07/.file2')

log.success("Password for bandit6: " + sh.recvline())
