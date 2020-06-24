#!/usr/bin/env python3

from subprocess import Popen, PIPE, DEVNULL, run
import socket
import sys
import traceback
import argparse
import time
import os

def startProcess(command, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostbyname(socket.gethostname()), int(port)))
        sock.close()
        popen = Popen(command, stdout=DEVNULL, stderr=PIPE)
        time.sleep(3)
        print("Start httptracker is sucess.")
    except OSError as e:
        raise e
    except Exception as e:
        raise e

def stopProcess(command):
    try:
        killCommand = ['pkill', '-f', ' '.join(command)]
        run(killCommand)
        time.sleep(2)
        print("Stop httptracker is sucess.")
    except OSError as e:
        raise e
    except Exception as e:
        raise e

class CustomArgparse(argparse.ArgumentParser):
    def error(self, message):
        if message == "":
            print("[Error] Argument is wrong...<(^^;)\n", file=sys.stderr)
        else:
            print("[Error] " + message + "\n", file=sys.stderr)
        self.print_help()
        sys.exit(2)

def main():
    try:
        parser = CustomArgparse(
            prog = "httptracker",
            description = "Track HTTP request to the end of the host.\nex) httptracker --mode start -p 80",
            add_help = True
        )
        parser.add_argument(
            "-m",
            "--mode",
            dest = "mode",
            nargs = 1,
            required = True,
            help = "[Required]Select modes which are 'start', 'restart', 'stop' to execute httptracker.",
        )
        parser.add_argument(
            "-p",
            "--port",
            dest = "port",
            nargs = 1,
            type = int,
            default = 8000,
            required = False,
            help = "[Optional]Direct port which httptracker process use. Default is 8000/tcp."
        )
        parser.add_argument(
            "-i",
            "--ipaddress",
            dest = "ipaddress",
            nargs = 1,
            type = str,
            default = "0.0.0.0",
            required = False,
            help = "[Optional]Direct listen ip address which httptracker process use. Default is 0.0.0.0 .",
        )
        args = parser.parse_args()

        ipaddress = ""
        port = ""

        if args.ipaddress != "0.0.0.0": ipaddress= args.ipaddress[0]
        else: ipaddress = args.ipaddress
        if args.port != 8000: port = str(args.port[0])
        else: port = str(args.port)

        command = ["python3", "manage.py", "runserver", ipaddress + ":" + port]

        if args.mode:
            mode = args.mode[0]
            if mode == "start":
                startProcess(command, port)
            elif mode == "restart":
                stopProcess(command)
                startProcess(command, port)
            elif mode == "stop":
                stopProcess(command)
            else:
                parser.error('Argument "--mode" need only "start", "restart", "stop".')
    except SystemExit:
        pass
    except:
        print("[Error] " + traceback.format_exc().splitlines()[-1], file=sys.stderr)

if __name__ == '__main__':
    main()
