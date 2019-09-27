#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit9 exploit by SKane')

shell = ssh('bandit9','bandit.labs.overthewire.org', password='UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR', port=2220)

sh = shell.run('sh')

sh.sendline("strings data.txt | grep = | awk '{print $2}'")

sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()
sh.recvline()

log.success("Password for bandit10: " + sh.recvline())
