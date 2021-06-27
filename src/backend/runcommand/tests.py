#!/usr/bin/env python3

import subprocess
import time

if __name__ == '__main__':
    process = subprocess.Popen(['chroot', '/'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate(input='cd'.encode())
    print(out.decode())
    print(err.decode())
    out, err = process.communicate(input='ls'.encode())
    print(out.decode())
    print(err.decode())