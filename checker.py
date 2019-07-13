##!/usr/bin/env python2
## -*- coding: utf-8 -*-
#"""
#Created on Sat Jul 13 15:48:24 2019
#
#@author: abhishek
#"""
#import re
#def convertunits(_):
#    d=_.split()
##    for i,v in enumerate(d):
##        try:
##            d[i]=float(v)
##        except:
##            pass
##    for l in d:
##        if (isinstance(l, float)):
##            print("float" + str(l))
##    for i,v in enumerate(d):
##        if (isinstance(d[i], float)):
##            print("float" + str(v))
#    for i,v in enumerate(d):
##        print(v+str(type(v)))
#        if i!=0: 
#            try:
#                d[i-1]=float(d[i-1])
#            except:
#                pass
#        if("million" in v):
#            if(isinstance(d[i-1],float)):
#                d[i-1]=str(d[i-1]*1000000)
#        if("billion" in v):
#            if(isinstance(d[i-1],float)):
#                d[i-1]=str(d[i-1]*1000000000)
#
#        if("thousand" in v):
#            if(isinstance(d[i-1],float)):
#                d[i-1]=str(d[i-1]*1000)
#        if("lakh" in v):
#            if(isinstance(d[i-1],float)):
#                d[i-1]=str(d[i-1]*100000)
#        if("lac" in v):
#            if(isinstance(d[i-1],float)):
#                d[i-1]=str(d[i-1]*100000)
#        if("lakhs" in v):
#            if(isinstance(d[i-1],float)):
#                d[i-1]=str(d[i-1]*100000)
#        if("lacs" in v):
#            if(isinstance(d[i-1],float)):
#                d[i-1]=str(d[i-1]*100000)
#    d = [i.encode('ascii', 'ignore').decode('ascii') for i in d]
#    _=" ".join(d)
#    return _
#
#
#with open("/home/abhishek/Documents/FAQ-Builder/Delhi.txt","r+") as f:
#    data=f.read()
#    ma={}
#    data=data.replace("\n"," ")
#    b=data.split(". ")
#    #    print(len(b))
#    #    print(b)
#    for _ in b:
#        t=0
#        d=""
#        if "population" in _:
#
#            print(">>")
#            _=convertunits(_)
#            print(_)
#            while ',' in _:
#                _=_.replace(',',"") #For removing commas from between the population figures.
##               print(_)
#            array = re.findall(r"[-+]?\d*\.\d+|\d+", _)
#            print(array)
#            z=_.split()
#            md=0
#            for i in range(len(z)):
#                if(z[i]=="population" and z[i+1]=="in"):
#                    md=1
##               print(array)
##               d=[_.find(k) for k in array]
##               print(d)
#            if(array):
#                for k in array:
#                    if(_.find("population")<_.find(" "+k)):  #Sometimes year figure is given before population word and most probably the number coming after population keyword is desired output.
#                        if(md==1):
#                            continue
#                        else:
#                            d=k     # space is added because the same number can be [resent in anmy figure in the sentence and hemnce could create confusion.
#                            break
#                else:
#                    break
#            else:
#                continue
#        if(d!=""):
#            break
import wptools
            
lapa=[]
ma={}
dela=wptools.page("Mumbai").get_parse()
for _ in dela.infobox:
    if("population" in _.lower()):
        lapa.append(dela.infobox[_])
    lar=0
    for _ in lapa:
        dis=_.split()
        for i in range(len(dis)):
            dis[i]=dis[i].replace(",","")
            try:
                dis[i]=int(dis[i])
            except:
                dis[i]=0
        for i in dis:
            if(i>lar):
                lar=i
        ma["Delhi"]=lar
print(ma["Delhi"])