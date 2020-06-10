#!/usr/bin/env python3

from ec2 import EC2

if __name__ == "__main__":
    ec2 = EC2()
    print(ec2.query("InstanceType"))
    print(ec2.query("InstanceIDDocument"))
    print(ec2.query())
