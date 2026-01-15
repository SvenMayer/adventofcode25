#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 23:14:33 2026

@author: sven
"""
N = 12

res = 0
with open("../../inputs/day3/input", "r") as fid:
    data = fid.read()

for ln in data.split("\n"):
    if len(ln) == 0:
        continue
    arr = [int(itm) for itm in ln]
    pos = 0
    for i in range(N):
        v = max(arr[pos:len(ln)-N+1+i])
        pos = arr.index(v, pos) + 1
        res += v * 10 ** (N-1-i)
print(res)
