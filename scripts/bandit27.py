#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit27 exploit by SKane')

shell = ssh('bandit27', 'bandit.labs.overthewire.org', password='3ba3118a22e93127a4ed485be72ef5ea', port=2220)

sh = shell.run('sh')

sh.sendline("cat /tmp/git12345/repo/README | awk '{print $8}'")

log.success("Password for bandit28: " + sh.recvline())
