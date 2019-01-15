#!/usr/bin/env python
# coding=utf-8

class linkqueue:
    def _init_(self):
        self.visited=[]
        self.unvisited=[]

    def get_visited_url(self):
        return self.visited

    def get_unvisitd_url(self):
        return self.unvisited

    def add_url_visited(self,url):
        return self.visited.append(url)

    def add_url_unvisited(self,url):
        if url!="" and url not in self.visited and not in self.unvisited:
            return self.unvisited.insert(0,url)

    def remove_url_visited(self,url):
        return self.visited.remove(url)

    def pop_from_unvisitd(self):
        try:
            return self.visited.pop()
        except:
            return None

    def get_num_visited(self):
        return len(self.visited)

    def get_num_unvisited(self):
        return len(self.unvisited)
    
    def is_unvisited_empty(self):
        return len(self.unvisited)==0


