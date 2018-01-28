#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2017 - Limber Cheng <cheng@limberence.com> 
# @Author : Limber Cheng
# @File : Acyclicity.py
# @Software: PyCharm

import sys

visited = []
markvisit = []
cycle = 0


def explore(v, cycle):
    visited.append(v)
    markvisit[v] = 1  # 1 means vertex is under exploration, that is, its neighbour vertex are being visited
    for w in adj[v]:
        if markvisit[w] == 1:
            cycle = 1
            break
        if w not in visited:
            cycle = explore(w, cycle)
    markvisit[v] = 2  # 2 means vertex has been visited
    return cycle


def dfs(adj, n, cycle):
    for v in range(n):
        if markvisit[v] == 1:
            cycle = 1
            break
        if v not in visited:
            cycle = explore(v, cycle)
    return cycle


def acyclic(adj, n, cycle):
    for v in range(n):
        markvisit.append(0)  # 0 means vertex has not been visited yet
    cycle = dfs(adj, n, cycle)
    return cycle


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n, cycle))
