#!/usr/bin/env python3

from collections import defaultdict

filename = 'input.txt'

with open( filename ) as f:
  jolts = [ int( i ) for i in f.read().splitlines() ]
  jolts = sorted( jolts )

jolts.insert( 0, 0 )
jolts.append( jolts[ -1 ] + 3 )

diffs = defaultdict( int )
for i in range( 1, len( jolts ) ):
  j = jolts[ i ]
  last_jolt = jolts[ i - 1 ]
  diffs[ j - last_jolt ] += 1

print( f"1 jolt ( { diffs[ 1 ] } ) * 3 jolts ( { diffs[ 3 ] } ) "
       f"= { diffs[ 1 ] * diffs[ 3 ] }" )

# Transitive closure of the graph of
#
# { 0 } -> { x }
#   |        |
#   |        v
#   |----> { y }
#
# We can calculate that with some dynamic programming

costs = defaultdict( int )
for i in range( len( jolts ) - 1, -1, -1 ):
  # Cost for this cell is sum of all exit cells
  j = jolts[ i ]
  if i == len( jolts ) - 1:
    costs[ j ] = 1
    continue

  cost = costs[ j + 1 ] + costs[ j + 2 ] + costs[ j + 3 ]
  costs[ j ] = cost

print( f"Number: { costs[ 0 ] }" )
