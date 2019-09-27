#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit0 exploit by SKane')

shell = ssh('bandit2', 'bandit.labs.overthewire.org', password='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9', port=2220)

sh = shell.run('sh')

sh.sendline('cat "spaces in this filename"')

log.success("Password for bandit3: " + sh.recvline())
