#!/usr/bin/env python
# coding=utf-8

import requests
import re
from linkqueue import linkqueue
from spider import spider

def url_get():
    _url=input("Please input the url you want to process:")
    try:
        kv={}
        requests.get(_url,headers=kv)
        return _url
    except:
        print '\033[1;31;40m'
        print "ERROR:Can not connct the address!"
        print '\033[0m'
    return url_get()

def spiderpage(_url):
    kv={}
    req=requests.get(_url,headers=kv)
    req.encoding=req.apparent_encoding
    pagetext=req.text
    pagelinks=re.findall(r'(?<=<a href=\").*?(?=\")|(?<=href=\').*?(?=\')',pagetext)
    return pagelinks

def url_filtrate(pagelinks):
    same_target=[]
    for l in pagelinks:
        if re.findall(,l):
            if re.findall(,l):
                pass
            elif re.findall(,l):
                pass
            elif re.findall(,l):
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
        file=write(f'{url}\n')
        x+=1
    file.close()
    print 'Write finished, total number of url is %d\n'%(x-1)

if __name__=='__main__':
    url=url_get()
    _spider=spider(url)
    urllist=spider.crawler(100)
    write_file(urllist)












