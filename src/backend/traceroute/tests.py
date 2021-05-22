#!/usr/bin/env python3

from traceroute import Traceroute

if __name__ == "__main__":
    #traceroute = Traceroute("9.9.9.9")
    traceroute = Traceroute("10.0.222.6")
    response = traceroute.traceroute()
    print(response)
