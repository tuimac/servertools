#!/usr/bin/env python3

import subprocess
import sys
import traceback

PORT = '8000'

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
            subprocess.run(['python3', 'manage.py', 'runserver', '0.0.0.0:' + PORT])
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
