#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Advent of Code 2019, Day 4

input    = '347312-805915';
lowest   = int(input[0:6])
hightest = int(input[7:])
diff     = hightest - lowest

def isValidPassword(code):
    zero  = str(code)[0]
    one   = str(code)[1]
    two   = str(code)[2]
    three = str(code)[3]
    four  = str(code)[4]
    five  = str(code)[5]

    if (zero <= one and one <= two and two <= three and three <= four and four <= five):
        if (zero == one or one == two or two == three or three == four or four == five):
            return True
    
    return False

passwords = []
for i in [j+1 for j in range(diff)]:
    password = lowest + i
    if isValidPassword(password):
        passwords.append(password)

length = len(passwords)
print('Part 1', length)
# 594

def isValidPassword2(code):
    zero  = str(code)[0]
    one   = str(code)[1]
    two   = str(code)[2]
    three = str(code)[3]
    four  = str(code)[4]
    five  = str(code)[5]

    if (zero <= one and one <= two and two <= three and three <= four and four <= five):
        if ((zero == one and one != two) or 
            (one == two and zero != one and two != three) or
            (two == three and one != two and three != four) or
            (three == four and two != three and four != five) or
            (four == five and three != four)):
          return True
    
    return False

passwords = []
for i in [j+1 for j in range(diff)]:
    password = lowest + i
    if isValidPassword2(password):
        passwords.append(password)

length = len(passwords)
print('Part 2', length)
# 364