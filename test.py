#!/usr/local/bin/python3

import os
os.system('ls')
path = os.getcwd()
print(path)
os.chdir("/Users/kenswain/Movies")
path = os.getcwd()
print(path)