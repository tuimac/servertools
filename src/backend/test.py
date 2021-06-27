#!/usr/bin/env python3

import subprocess
import traceback
import threading

def stdout(p):
    stdout = p.stdout.read()
    print('hello')
    print(stdout)

def stderr(p):
    stderr = p.stderr.read()
    print('stderr')
    print(stderr)
       
def stdin(p, command):
    p.stdin.write(command.encode())

if __name__ == '__main__':
    try:
        p = subprocess.Popen(
            ['chroot', '/'],
            shell=False,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdoutThread = threading.Thread(target=stdout, args=(p, ))
        stderrThread = threading.Thread(target=stderr, args=(p, ))
        stdoutThread.daemon = True
        stderrThread.daemon = True
        stdoutThread.start()
        stderrThread.start()
        stdin(p, 'ls')
        stdoutThread.join()
        stderrThread.join()
    except:
        traceback.print_exc()

