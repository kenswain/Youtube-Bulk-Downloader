#!/usr/local/bin/python3

import os
filepath = 'ken.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    os.chdir("/Users/kenswain/Movies/")
    while line:
#        print("line {}: {}".format(cnt, line.strip()))
        os.system("youtube-dl " + line)
        line = fp.readline()
        cnt += 1