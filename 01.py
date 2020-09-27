
# Session 1

# arrays:

distanceRun = [[9,10,15,6],[10,12,14,8],[8,15,13,9],[12,15,16,10],[0,0,0,12],[6,0,8,12],[9,10,9,0]]

# a)
# add brackets for python3
# just say need brackets, don't complicate with python2
print(distanceRun[4][3])


# b)

'''
Pseudocode:

FUNCTION total(runner):
    miles <- 0
    FOR day <- 0 TO 6
        miles <- miles + distanceRun[day][runner]
    ENDFOR
    RETURN miles
ENDFUNCTION
'''

# python

def total(runner):
    miles = 0
    for day in range(7):
        miles = miles + distanceRun[day][runner]
    return miles

print(total(1))


# c)

'''
FUNCTION milesConvert(miles):
    kilometres <- miles * 8/5
    RETURN kilometres
ENDFUNCTION
'''


def milesConvert(miles):
    return miles * 8/5

'''
Pseudocode:

define function convert():
    FOR day <- 0 TO 6
        FOR runner <- 0 TO 3
            miles <- distanceRun[day][runner]
            distanceRun[day][runner] <- milesConvert(miles)
        ENDFOR
    ENDFOR
ENDFUNCTION
'''

def convert():
    for day in range(7):
        for runner in range(4):
            miles = distanceRun[day][runner]
            distanceRun[day][runner] = milesConvert(miles)
convert()
print(distanceRun)


# subroutines:

# 1.

'''
SUBROUTINE difference(x)
    cube <- x^3
    square <- x^2
    result <- cube - square
    RETURN result
ENDSUBROUTINE
'''

def difference(x):
    cube = x**3
    square = x**2
    return cube - square
    #return x**3 - x**2

print(difference(2))

# 2.
# it makes naming variables easier
# they cannot be accessed from outside the subroutine

# b)

import random
def rollTwo(n):
    return [random.randint(1,n),random.randint(1,n)]

def roll(sides):
    score = 0
    dice = [1,2]
    while dice[0] != dice[1]:
        dice = rollTwo(sides)
        score += 1
    return score
print(roll(6))

# c)

# can easily reuse a block of code rather than writing it out again
# can paramaterise the subroutines, so only require changes to parameters to compute different event
# makes application more readable for anybody else


# 3.
# a)
#  i) a variable passed to a function / subroutine
#  ii) the area of code in which it can be accessed

# b)
#  i) takes a user input of their weight, divides it by 6 and returns this number
#  ii) variable weight is being used outside of its scope

# c)

def adjust(difficulty,heartRate):
    if heartRate < 90:
        difficulty += 1
    elif 140 < heartRate < 160:
        difficulty -= 1
    elif heartRate > 160:
        difficulty = 0
        print('Slow Down!')
    return difficulty
