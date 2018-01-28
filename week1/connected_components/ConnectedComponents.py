#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2017 - Limber Cheng <cheng@limberence.com> 
# @Author : Limber Cheng
# @File : ConnectedComponents

import sys

visited = []
isin = []  # list of all those vertices which are reachable from x


def explore(v):
    visited.append(v)
    for w in adj[v]:
        if not w in visited:
            explore(w)


def dfs(adj, n):
    cc = 0
    for v in range(n):
        if not v in visited:
            explore(v)
            cc = cc + 1
    return cc


def number_of_components(adj, n):
    result = dfs(adj, n)
    return result


def reach(adj, x, y, n):
    isin.append(x)
    visited.append(x)
    dfs(adj, n)
    if y in isin:  # checking whether y is reachable from x or not
        print("Yes")
    else:
        print("no")


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj, n))
