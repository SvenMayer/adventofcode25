#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 00:10:21 2025

@author: sven
"""
with open ("../../inputs/day1/input", "r") as fid:
    data = fid.read()

res = 0
val = 50
for ln in data.split("\n"):
    if len(ln) == 0:
        continue
    n = int(ln[1:])
    if ln[0] == "L":
        n *= -1
    if n == 0:
        continue
    val0 = val
    val = (val + n)
    res0 = res
    if val0 > 0 and val < 0:
        res += 1
    res += abs(val) // 100
    if val == 0:
        res += 1
    print(f"{val0:3d} {val:3d} {ln:4s} {res-res0:d}")
    val %= 100



print (res)