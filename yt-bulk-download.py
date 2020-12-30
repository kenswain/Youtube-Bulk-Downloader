#!/usr/local/bin/python3

import os, time
def video_download():
    filepath = 'videos.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        os.chdir("{Your Downloads Dir}")

        while line:
            #print("line {}: {}".format(cnt, line.strip()))
            os.system("youtube-dl " + line)
            line = fp.readline()
            cnt += 1
def checkfile():
    if not os.path.exists('videos.txt'):
        print("videos.txt did not exist....")
        print("Creating videos.txt for you.....")
        os.system('touch videos.txt')
        print("This file is empty so nothing will be downlaoded.")
        print("Please populate videos.txt with the urls you would like to be downloaded.")
        print("Rerun program")
    elif os.stat('videos.txt').st_size == 0:
        print("video.txt file is empty so nothing will be downlaoded.")
        print("Please populate videos.txt with the urls you would like to be downloaded.")
        print("Rerun program")
    else:
        video_download()




checkfile()
