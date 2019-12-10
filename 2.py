#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Advent of Code 2019, Day 2

f = open('2.txt', 'r')
c = f.read()

def initList(codes, noun, verb):
	codes[1] = noun
	codes[2] = verb
	return codes[:]

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

def processIntcode(input):
	pos    = 0
	result = True
	while result:
		result = processBlock(input, pos)
		if result:
			input = result
			pos  += 4

	return input[0]

codes = c.split(',')
codes = [ int(x) for x in codes]

# Set initial values straight
codes = initList(codes, 12, 2)
result = processIntcode(codes)

print("Part 1", result)
# 5534943

codes = c.split(',')
codes = [ int(x) for x in codes]

for noun in range(0,100):
	stop = False
	for verb in range(0,100):
		testCode = initList(codes, noun, verb)
		result   = processIntcode(testCode)

		if result == 19690720:
			stop = True
			break

	if stop:
		break

print(testCode[0])
print("Part 2", noun*100+verb)