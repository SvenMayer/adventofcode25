#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 19:49:00 2026

@author: sven
"""
TEST_DATA = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

class Range:
    def __init__(self, x0, x1):
        if x0 > x1:
            x0, x1 = x1, x0
        self._x0 = x0
        self._x1 = x1

    def __contains__(self, x):
        return self._x0 <= x and x <= self._x1

    def overlaps(self, other):
        return self._x0 in other or self._x1 in other or other._x0 in self or other._x1 in self

    def merge(self, other):
        self._x0 = min(self._x0, other._x0)
        self._x1 = max(self._x1, other._x1)

    def __lt__(self, other):
        return self._x0 < other._x0

    def __len__(self):
        return self._x1 - self._x0 + 1

    def __repr__(self):
        return f"Range ({self._x0}, {self._x1})"


def parse_range(ln):
    str0, str1 = ln.split("-")
    return Range(int(str0), int(str1))


def parse_input(data):
    ranges_input, ids_input = data.split("\n\n")
    ranges = []
    for ln in ranges_input.split("\n"):
        if len(ln):
            ranges.append(parse_range(ln))
    ids = []
    for ln in ids_input.split("\n"):
        if len(ln):
            ids.append(int(ln))
    return ranges, ids


def find_valid_ids(ranges, ids):
    valid = []
    for i, id_ in enumerate(ids):
        for r in ranges:
            if id_ in r:
                valid.append(id_)
                break
    return valid


def reduce_ranges(ranges):
    new_ranges = ranges
    old_ranges = []
    while (len(new_ranges) != len(old_ranges)):
        old_ranges = new_ranges
        new_ranges = []
        for r in old_ranges:
            for nr in new_ranges:
                if nr.overlaps(r):
                    nr.merge(r)
                    break
            else:
                new_ranges.append(r)
    return new_ranges


with open("../../inputs/day5/input", "r") as fid:
    data = fid.read()
# data = TEST_DATA
ranges, ids = parse_input(data)
# ranges.sort()
print(len(find_valid_ids(ranges, ids)))

reduced_ranges = reduce_ranges(ranges)
print(sum((len(itm) for itm in reduced_ranges)))
