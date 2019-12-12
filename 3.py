#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Advent of Code 2019, Day 3

f = open('3.txt', 'r')
c = f.readlines()

wire1 = c[0].rstrip('\n').split(',')
wire2 = c[1].split(',')

def createPath(wire):
    path = []
    pos  = (0,0)

    for i in wire:
        direction = i[0]
        steps = int(i[1:])

        if direction == 'U':
            for j in range(steps):
                pos = (pos[0], pos[1]+1)
                path.append(pos)
        elif direction == 'D':
            for j in range(steps):
                pos = (pos[0], pos[1]-1)
                path.append(pos)
        elif direction == 'L':
            for j in range(steps):
                pos = (pos[0]-1, pos[1])
                path.append(pos)
        elif direction == 'R':
            for j in range(steps):
                pos = (pos[0]+1, pos[1])
                path.append(pos)

    return path

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def getClosestCross(crosses):
    minDist  = 0
    minCross = 0

    for cross in crosses:
        dist = abs(cross[0]) + abs(cross[1])

        if minDist == 0 or dist < minDist:
            minDist = dist
            minCross = cross

    return (minDist, minCross)

path1 = createPath(wire1)
path2 = createPath(wire2)

crosses = intersection(path1, path2)
minimal = getClosestCross(crosses)

print('Part 1', minimal[0])
# 352

def findPathLengths(crosses, path1, path2):
    minimum = 0

    for cross in crosses:
        steps1 = path1.index(cross) + 1
        steps2 = path2.index(cross) + 1
        steps  = steps1 + steps2

        if minimum == 0 or steps < minimum:
            minimum = steps

    return minimum

minimum = findPathLengths(crosses, path1, path2)
print('Part 2', minimum)
# 43848