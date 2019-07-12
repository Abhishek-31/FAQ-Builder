#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:01:06 2019

@author: abhishek
"""



import re
with open("/home/abhishek/Documents/FAQ-Builder/Delhi.txt","r+") as f:
    a=f.read()
    b=a.split(".")
#    print(len(b))
#    print(b)
    for _ in b:
        if "population" in _:
            while ',' in _:
                _=_.replace(',',"") #For removing commas from between the population figures.
            print(_)
            array = re.findall(r'[0-9]+', _)
            for k in array:
                if(_.find("population")<_.find(k)):  #Sometimes year figure is given before population word and most probably the number coming after population keyword is desired output.
                    print(k)
                    break
            break