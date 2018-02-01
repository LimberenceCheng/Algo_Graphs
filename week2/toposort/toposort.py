#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2017 - Limber Cheng <cheng@limberence.com> 
# @Author : Limber Cheng
# @File : toposort.py
# @Software: PyCharm

import sys
postorder=[]
visited = []
def explore(v):
    visited.append(v)
    for w in adj[v]:
        if not w in visited:
            explore(w)
    postorder.append(v)
def dfs(adj,n):
    for v in range(n):
        if not v in visited:
            explore(v)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    dfs(adj,n)
    for i in range(len(postorder)):
        print(postorder[len(postorder)-i-1]+1,end=' ')
    print()
