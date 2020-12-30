#!/usr/local/bin/python3

import os, time
def checkfile():
    if not os.path.exists('videos.txt'):
        command = 'touch videos.txt'
        os.popen(command)
        time.sleep(.5)

checkfile()
filepath = 'videos.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    os.chdir("{Your Downloads Dir}")
    
    while line:
#        print("line {}: {}".format(cnt, line.strip()))
        os.system("youtube-dl " + line)
        line = fp.readline()
        cnt += 1