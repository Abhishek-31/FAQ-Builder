#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:43:19 2019

@author: abhishek
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:01:06 2019

@author: abhishek
"""
import json
import re
import wptools
    
def convertunits(_):
    d=_.split()
#    for i,v in enumerate(d):
#        try:
#            d[i]=float(v)
#        except:
#            pass
#    for l in d:
#        if (isinstance(l, float)):
#            print("float" + str(l))
#    for i,v in enumerate(d):
#        if (isinstance(d[i], float)):
#            print("float" + str(v))
    for i,v in enumerate(d):
#        print(v+str(type(v)))
        if i!=0: 
            try:
                d[i-1]=float(d[i-1])
            except:
                pass
        if("million" in v):
            if(isinstance(d[i-1],float)):
                d[i-1]=str(d[i-1]*1000000)
        if("billion" in v):
            if(isinstance(d[i-1],float)):
                d[i-1]=str(d[i-1]*1000000000)

        if("thousand" in v):
            if(isinstance(d[i-1],float)):
                d[i-1]=str(d[i-1]*1000)
        if("lakh" in v):
            if(isinstance(d[i-1],float)):
                d[i-1]=str(d[i-1]*100000)
        if("lac" in v):
            if(isinstance(d[i-1],float)):
                d[i-1]=str(d[i-1]*100000)
        if("lakhs" in v):
            if(isinstance(d[i-1],float)):
                d[i-1]=str(d[i-1]*100000)
        if("lacs" in v):
            if(isinstance(d[i-1],float)):
                d[i-1]=str(d[i-1]*100000)
    for i in range(len(d)):
        if(isinstance(d[i],float)):
            d[i]=str(d[i])
        elif(isinstance(d[i],int)):
            d[i]=str(d[i])
        else:
            try:
                d[i]=d[i].encode('ascii', 'ignore').decode('ascii')
            except:
                d[i]="a"
    _=" ".join(d)
    return _

with open("/home/abhishek/Downloads/Part-1-City.txt","r+") as l:
    data=l.read()
    datad=json.loads(data)
    print(len(datad))
    ma={}
    for each in datad:
        try:
            lapa=[]
            dela=wptools.page(each).get_parse()
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
                ma[each]=lar
        except:    
            data=datad[each]["content"]
            data=data.replace("\n"," ")
            b=data.split(". ")
            #    print(len(b))
            #    print(b)
            for _ in b:
                d=""
                if "population" in _:
        
                    print(">>")
                    _=convertunits(_)
                    print(_)
                    while ',' in _:
                        _=_.replace(',',"") #For removing commas from between the population figures.
        #               print(_)
                    array = re.findall(r"[-+]?\d*\.\d+|\d+", _)
                    print(array)
                    z=_.split()
                    md=0
                    for i in range(len(z)-1):
                        if(z[i]=="population" and z[i+1]=="in"):
                            md=1
        #               print(array)
        #               d=[_.find(k) for k in array]
        #               print(d)
                    if(array):
                        for k in array:
                            if(_.find("population")<_.find(" "+k)):  #Sometimes year figure is given before population word and most probably the number coming after population keyword is desired output.
                                if(md==1):
                                    continue
                                else:
                                    d=k     # space is added because the same number can be [resent in anmy figure in the sentence and hemnce could create confusion.
                                    break
                        else:
                            continue
                    else:
                        continue
                if(d!=""):
                    print(each +" "+ d)
                    break
            ma[each]=d
            print(ma[each])

for key,val in ma.items():
    print("key is" + key)
    print("value is"+val)
with open("population-final.txt","w+") as f:
    f.write(json.dumps(ma))
#import re
#city=["/home/abhishek/Documents/FAQ-Builder/Delhi.txt","/home/abhishek/Documents/FAQ-Builder/East York.txt",'/home/abhishek/Documents/FAQ-Builder/Yatomi.txt']
#for each in city:
#    for each in datad:
#        a=datad[each]["content"]
#        d=a.split("")
#        for i,v in enumerate(d):
#            if v == ".":
#                if(isNumber(d[i-1]) and isNumber(d[i+1])):
#                    d[i]="len234"
#        while "len234" in d:
#            d.remove("len234")
#        a="".join(d)
#        b=a.split(". ")
#        zoom=0
#    #    print(len(b))
#    #    print(b)
#        for _ in b:
#            t=0
#            b=b.replace(".","")
#            if "population" in _:
#                print(">>")
#                print(_)
#                _=convertunits(_)
#                while ',' in _:
#                    _=_.replace(',',"") #For removing commas from between the population figures.
##                print(_)
#                array = re.findall(r'[0-9]+', _)
##                print(array)
##                d=[_.find(k) for k in array]
##                print(d)
#                for k in array:
#                    if(_.find("population")<_.find(" "+k)):  #Sometimes year figure is given before population word and most probably the number coming after population keyword is desired output.
#                        print(each)
#                        print(k)     # space is added because the same number can be [resent in anmy figure in the sentence and hemnce could create confusion.
#                        break
#                break
#            if zoom == 1:
#                break