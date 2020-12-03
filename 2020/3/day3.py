#!/usr/bin/env python3

with open( 'input.txt' ) as f:
  lines = f.read().splitlines()


def CheckSlope( x_step, y_step ):
  x = 0
  y = 0

  trees = 0

  for y in range( 0, len( lines ), y_step ):
    line = lines[ y ]
    char = line[ x % len( line ) ]
    if char  == '#':
      trees += 1
    x += x_step

  return trees


print( f"Part1: { CheckSlope( 3, 1 ) }" )

paths = ( ( 1, 1), ( 3, 1 ), ( 5, 1 ), ( 7, 1 ), ( 1, 2 ) )

result = 1
for x_step, y_step in paths:
  result *= CheckSlope( x_step, y_step )

print( f"Part 2: {result}" )
