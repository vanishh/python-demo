# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:55:07 2018

@author: geyang
"""
' a test module'

__author__ = "Gavin Ge"

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello, %s" % args[1])
    else:
        print("too many argumengts!")

if __name__ == '__main__':
    test()
