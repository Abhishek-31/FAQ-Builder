#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:01:06 2019

@author: abhishek
"""

def convertunits(_):
    while ' billion' in _:
        _=_.replace(' billion',"000000000")
    while ' million' in _:
        _=_.replace(' million',"000000")
    while ' thousand' in _:
        _=_.replace(' thousand',"000")
    while ' lac' in _:
        _=_.replace(' lac',"00000")
    while ' lakh' in _:
        _=_.replace(' lakhs',"00000")
    while ' lacs' in _:
        _=_.replace(' lacs',"00000")
    while ' lakhs' in _:
        _=_.replace(' lakhs',"00000")
    return _
    
import re
city=["/home/abhishek/Documents/FAQ-Builder/Delhi.txt","/home/abhishek/Documents/FAQ-Builder/East York.txt",'/home/abhishek/Documents/FAQ-Builder/Yatomi.txt']
for each in city:
    with open(each,"r+") as f:
        a=f.read()
        b=a.split(".")
    
    #    print(len(b))
    #    print(b)
        for _ in b:
            if "population" in _:
                print(_)
                _=convertunits(_)
                while ',' in _:
                    _=_.replace(',',"") #For removing commas from between the population figures.
#                print(_)
                array = re.findall(r'[0-9]+', _)
#                print(array)
#                d=[_.find(k) for k in array]
#                print(d)
                for k in array:
                    if(_.find("population")<_.find(" "+k)):  #Sometimes year figure is given before population word and most probably the number coming after population keyword is desired output.
                        print(k)     # space is added because the same number can be [resent in anmy figure in the sentence and hemnce could create confusion.
                        break
                break