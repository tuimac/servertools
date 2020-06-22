#!/usr/bin/env python3

import subprocess
import sys

def usage():
    print('usage: httptracker [help | start | restart | stop]\n')
    print('start       Start httptracker process')
    print('restart     Restart httptracker process')
    print('stop        Stop httptracker process\n')

def main():
    if len(sys.argv) != 1:
        usage()
        sys.exit(1)
    arg = sys.argv[1]
    if arg == 'start':
    
    elif arg == 'restart':
    elif arg == 'stop':
    else:


if __name__ == '__main__':
    main()
