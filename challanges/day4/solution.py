#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 23:33:03 2026

@author: sven
"""
ITERATE = True

with open("../../inputs/day4/input", "r") as fid:
    data = fid.read()

LEN_ROW = data.index("\n") + 1

data = (LEN_ROW) * "\n"  + data + (LEN_ROW) * "\n"

def count_adc(data, idx):
    res = 0
    for i in [-LEN_ROW-1, -LEN_ROW, -LEN_ROW+1, -1, 1, LEN_ROW-1, LEN_ROW, LEN_ROW+1]:
        if data[idx+i] == "@":
            res += 1
    return res


res = 0
updated = True
while updated:
    updated = 0
    for idx in range(LEN_ROW, len(data) - LEN_ROW):
        if data[idx] == "@" and count_adc(data, idx) < 4:
            res += 1
            if ITERATE:
                data = data[:idx] + "x" + data[idx+1:]
                updated = True
print(res)
