#!/usr/bin/env python3

import os
import subprocess
import socket
import pty
import traceback
from threading import Thread
import time

def stderr(process):
    while True:
        print(p.stderr.readline())

def stdout(process):
    while True:
        print(p.stdout.readline())

if __name__ == "__main__":
    p = subprocess.Popen(
        ['/bin/bash'],
        shell = False,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out = Thread(target=stdout, args=(p, ))
    out.setDaemon(True)
    out.start
    err = Thread(target=stderr, args=(p, ))
    err.setDaemon(True)
    err.start
    time.sleep(2)
    p.stdin.write('cd /\n'.encode())
    p.stdin.write('ls\n'.encode())
