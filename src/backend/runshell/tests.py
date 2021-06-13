#!/usr/bin/env python3

import os
import subprocess
import socket
import pty
import traceback
from threading import Thread
import time

if __name__ == "__main__":
    master, slave = os.openpty()
    cmd = '/bin/bash ' + os.ttyname(slave)
    p = subprocess.Popen(
        cmd.split(),
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    p.stdin.write('cd /\n'.encode())
    p.stdin.close()
    print(p.stdout.readline())
    p.stdin.write('ls\n'.encode())
    print(p.stdout.readline())
    print(p.stderr.readline())
