#!/usr/bin/env python3

from subprocess import Popen, PIPE, DEVNULL, run
import socket
import sys
import traceback
import time
import os

PORT = '8000'

def startProcess(command):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostbyname(socket.gethostname()), int(PORT)))
        sock.close()
        popen = Popen(command, stdout=DEVNULL, stderr=PIPE)
        time.sleep(3)
    except OSError as e:
        raise e
    except Exception as e:
        raise e

def stopProcess(command):
    try:
        killCommand = ['pkill', '-f', ' '.join(command)]
        print(killCommand)
        run(killCommand)
        time.sleep(2)
    except OSError as e:
        raise e
    except Exception as e:
        raise e

def usage():
    print('usage: httptracker [help | start | restart | stop]\n')
    print('start       Start httptracker process')
    print('restart     Restart httptracker process')
    print('stop        Stop httptracker process\n')

def main():
    command = ['python3', 'manage.py', 'runserver', '0.0.0.0:' + PORT]
    try:
        parser = argparse.ArgumentParser(
            prog = 'cfnclient',
            description = 'Automate to create and delete stacks.',
            add_help = True
    	)
        parser.add_argument(
            '--start',
            action = 'store_true',
            dest = 'start',
            help = 'Start httptracker process.',
        )
        parser.add_argument(
            '--restart',
            action = 'store_true',
            dest = 'restart',
            help = 'Restart httptracker process.'
        )
        parser.add_argument(
            '--stop',
            action = 'store_true',
            dest = 'stop',
            help = 'Stop httptracker process.',
        )
        args = parser.parse_args()
    except SystemExit:
        pass
    except OSError:
        message = traceback.format_exc().splitlines()[-1]
        print(message, file=sys.stderr)
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()
