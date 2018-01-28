#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2017 - Limber Cheng <cheng@limberence.com> 
# @Author : Limber Cheng
# @File : StronglyConnected.py
# @Software: PyCharm

import sys

sys.setrecursionlimit(200000)
visited = []
post = []
Visited = []


def Explore(v):
    Visited.append(v)
    post.remove(post[v])
    for w in adj[v]:
        if w not in Visited:
            Explore(w)


def explore(v, postcount):
    visited.append(v)
    postcount += 1
    for w in adj[v]:
        if w not in visited:
            explore(w, postcount)
    postcount = postcount + 1
    post[v] = postcount


def dfs(adj, n):
    for v in range(n):
        if v not in visited:
            explore(v, 0)


def number_of_strongly_connected_components(adj, adjreverse, n):
    dfs(adjreverse, n)  # aim for dfs is to calculate post of reverse graph
    scc = 0
    while len(post) > 0:
        sink_in_graph = post.index(max(post))
        Explore(sink_in_graph)
        scc = scc + 1

    return scc


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adjreverse = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    for (a, b) in edges:
        adjreverse[b - 1].append(a - 1)
    for _ in range(n):
        post.append(0)
    print(number_of_strongly_connected_components(adj, adjreverse, n))
