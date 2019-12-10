#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Advent of Code 2019, Day 2

f = open('2.txt', 'r')
c = f.read()

def initList(codes):
	codes[1] = 12
	codes[2] = 2
	return codes

def processBlock(codes, pos):
	block  = codes[pos:pos+4];
	opcode = block[0]

	if opcode == 1:
		result = codes[block[1]] + codes[block[2]]
		codes[block[3]] = result
		return codes

	elif opcode == 2:
		result = codes[block[1]] * codes[block[2]]
		codes[block[3]] = result
		return codes

	elif opcode == 99:
		return False

	else:
		raise Exception('No recognized opcode code')

codes = c.split(',')
codes = [ int(x) for x in codes]
pos   = 0

# Set initial values straight
codes = initList(codes)

result = True
while result:
	result = processBlock(codes, pos)
	if result:
		codes = result
		pos  += 4

print("Part 1", codes[0])
# 5534943
