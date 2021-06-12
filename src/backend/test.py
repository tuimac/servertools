#!/usr/bin/env python3

import pty

def test():
    pty.spawn('/bin/bash')

if __name__ == '__main__':
    test()
