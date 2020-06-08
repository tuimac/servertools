#!/bin/bash

echo -en "Password: "
read -s password
echo

base64 $password > password.txt

cat password.txt | base64 -d
