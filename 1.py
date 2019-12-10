#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Advent of Code 2019, Day 1

from math import floor

f = open('1.txt', 'r')
l = f.readlines()

def calcFuel(input):
    result = floor (int(input) / 3) - 2
    return int(result) if result >=0 else 0

fuel = 0
for line in l:
    fuel += calcFuel(line)

print("Part 1", fuel)
# 3178783

fuel = 0
for line in l:
    result = calcFuel(line)
    while result > 0:
        fuel += result
        result = calcFuel(result)

print("Part 2", fuel)
# 4765294