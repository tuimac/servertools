#!/usr/bin/env python3

from ec2 import EC2

if __name__ == "__main__":
    ec2 = EC2()
    ec2.query("InstanceType")
