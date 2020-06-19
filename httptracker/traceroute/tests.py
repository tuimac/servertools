#!/usr/bin/env python3

from traceroute import Traceroute

if __name__ == "__main__":
    traceroute = Traceroute("8.8.8.8")
    traceroute.traceroute()
