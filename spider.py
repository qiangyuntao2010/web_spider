#!/usr/bin/env python
# coding=utf-8
from linkqueue import linkqueue

class spider:
    def __init__(self,url):
        self.linkqueue=linkqueue()
        self.linkqueue.add_url_unvisited(url)

    def crawler(self,urlcount):
        x=1
        while x<=urlcount:
            if x>=1:
                print 'Process no.%d url,start!\n'%(x-1)
            visitedurl=self.linkqueue.pop_from_unvisited()
            if visitedurl is None or visitedurl=='':
                break
            initial_links=spiderpage(visitedurl)
            right_links=url_filtrate(initial_links)
            self.linkqueue.add_url_visited(visitedurl)
            for link in right_links:
                self.linkqueue.add_url_unvisited(link)
            x+=1
        print 'Finished and total number of url is %d\n'%(x-2)
        return self.linkqueue.visited
