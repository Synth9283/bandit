#!/usr/bin/env python
from pwn import *

log.info('ovetherwire.org - bandit15 exploit by SKane')

shell = ssh('bandit15', 'bandit.labs.overthewire.org', password='BfMYroe26WYalil77FoDi9qh59eK5xNr', port=2220)

sh = shell.run('sh')

sh.sendline('cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -quiet')

sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()

log.success("Password for bandit16: " + sh.recvline())
