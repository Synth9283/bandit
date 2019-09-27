#!/usr/bin/env python
from pwn import *

log.info('overthewire.org -bandit17 exploit by SKane')

shell = ssh('bandit17', 'bandit.labs.overthewire.org', keyfile='../sshkey/sshkey2.private', port=2220)

sh = shell.run('sh')

sh.sendline("diff passwords.old passwords.new | awk '{print $2}'")

sh.recvline()
sh.recvline()
sh.recvline()

log.success("Password for bandit18: " + sh.recvline())
