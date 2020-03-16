#! python3
# -*- coding: utf-8 -*-

"""

-------------------------------------------------

File Name： move_dirs

Description :

Author : MingDee

date： 2019/11/10

-------------------------------------------------

Change Activity:

2019/11/10:

-------------------------------------------------

"""

import os
import shutil


def main():
    path = "D:/Comics/咳咳咳/"
    for dirs in os.listdir(path):
        pic_list = os.listdir(path + dirs)
        pic_list.sort(key=lambda x: int(x.split('.')[0]))
        Len = len(pic_list)
        if Len <= 8:
            continue
        if Len == int(pic_list[-1].split('.')[0]):
            shutil.copytree(path + dirs, 'D:/Comics/新建文件夹/' + dirs)


main()