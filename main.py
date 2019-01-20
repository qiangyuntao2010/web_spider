#!/usr/bin/env python
# coding=utf-8

import requests
import re
from linkqueue import linkqueue
from spider import spider
import sys
from os import system



def url_get():
    system("uname -a")
    _url=raw_input("Please input the url you want to process: ")
    try:
        requests.get(_url)
        return _url
    except:
        print '\033[5;31;40m'
        print "ERROR: Can not connct the address!"
        print '\033[0m'
        a=int(raw_input("Next step number you need to select:([1]repeat input. [2]Exit):"))
        if a==1:
            return url_get()
        if a==2:
            sys.exit(0)
        if a!=1 and a!=2:
            print '\033[1;31;40m'
            print 'Invalid opeartion!'
            print '\033[0m'
            sys.exit(0)

def spiderpage(_url):
   # kv={}
    req=requests.get(_url)
    req.encoding=req.apparent_encoding
    pagetext=req.text
    pagelinks=re.findall(r'(?<=<a href=\").*?(?=\")|(?<=href=\').*?(?=\')',pagetext)
    return pagelinks

def url_filtrate(pagelinks):
    same_target=[]
    for l in pagelinks:
 #       if re.findall(,l):
 #           pass
 #       elif re.findall(,l):
 #           pass
 #       elif re.findall(,l):
        same_target.append(l)
    unique_target=[]
    for l in same_target:
        if l not in unique_target:
            unique_target.append(l)
    return unique_target

def write_file(list):
    x=1
    for url in list[1:]:
        file=open('./urls.txt','a',encoding='utf8')
        file.write(url+"\n")
        x+=1
   # file.close()
    print 'Write finished, total number of url is %d\n'%(x-1)

if __name__=='__main__':
    url=url_get()
    _spider=spider(url)
    urllist=_spider.crawler(100)
    write_file(urllist)












