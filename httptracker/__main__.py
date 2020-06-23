#!/usr/bin/env python3

from subprocess import DEVNULL, PIPE, Popen
import sys
import traceback
import time
import os

PORT = '8000'
PIDFILE = 'httptracker.pid'

def usage():
    print('usage: httptracker [help | start | restart | stop]\n')
    print('start       Start httptracker process')
    print('restart     Restart httptracker process')
    print('stop        Stop httptracker process\n')

def main():
    try:
        if len(sys.argv) != 2:
            usage()
            sys.exit(1)
        arg = sys.argv[1]
        if arg == 'start':
            try:
                command = ['python3', 'manage.py', 'runserver', '0.0.0.0:' + PORT]

                with Popen(command, stdout=PIPE, stderr=PIPE) as popen:
                    time.sleep(3)
                    popen.stdout.readline()
                '''
                if stderr != b'':
                    popen.kill()
                    print(stderr)
                else:
                    with open(PIDFILE, 'w') as f:
                        f.write(str(popen.pid))
                    print('Start success.')
                '''
            except Exception as e:
                raise e
        elif arg == 'restart':
            pass
        elif arg == 'stop':
            pass
        elif arg == 'help':
            usage()
        else:
            usage()
    except SystemExit:
        pass
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()
