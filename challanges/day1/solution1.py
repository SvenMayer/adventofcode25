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
    val = (val + n) % 100
    if val == 0:
        res += 1

print (res)