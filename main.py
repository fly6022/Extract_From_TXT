# !/usr/bin/python
# -*- coding: utf-8 -*-
# @name   : Extract_From_TXT/main.py
# @author : fly6022
# @date   : 2022/5/29
# @Email  : i@fly6022.fun
# @license: MIT

import linecache

filename,p,q,loop=input().split(' ');

p = int(p);

q = int(q);

loop = int(loop);

def main(p,q,loop):

    PRINT_OR_LIST = "n"

    count = len(open(filename, encoding='UTF-8').readlines())

    if int(loop) > count:
        count,loop = loop,count

    for i in range(p, loop, q):
        with open(filename, encoding="UTF-8") as f:
            for num, line in enumerate(f):
                if num == i-1:
                    if PRINT_OR_LIST == "Y":
                        line=line.strip("\n")
                        list=[]
                        list.append(line)
                        print(list)
                    else:
                        print(line)
    print("内容共计" + str(loop) + "行.")

main(p,q,loop)