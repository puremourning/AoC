#!/usr/bin/env python3

filename = 'input.txt'
preamble_size = 25

with open( filename ) as f:
  lines = [ int( line ) for line in f.read().splitlines() ]


def ContainsSum( window, target ):
  low = 0
  high = len( window ) - 1

  window = sorted( window )

  while low < high:
    if window[ low ] + window[ high ] < target:
      low += 1
    elif window[ low ] + window[ high ] > target:
      high -= 1
    else:
      return True

  return False


def FindInvalid( lines ):
  window = []

  for i in range( len( lines ) ):
    n = lines[ i ]
    if i < preamble_size:
      window.append( n )
      continue

    assert len( window ) == preamble_size

    # check this number
    if not ContainsSum( window, n ):
      print( f"{ n } not a sum of any 2 in { window } at pos { i }" )
      return n

    window.pop( 0 )
    window.append( n )


invalid_value = FindInvalid( lines )


def FindSumRange( lines, target ):
  low = 0
  high = 0
  s = 0

  while high < len( lines ):
    s += lines[ high ]
    while s > target:
      s -= lines[ low ]
      low += 1

    if s == target:
      return low, high

    high += 1

  raise ValueError( f"didn't find any range summing to { target }" )


print( f"Searching for ranges summing to { invalid_value }" )

sum_i, sum_j = FindSumRange( lines, invalid_value )

found_range =  lines[ sum_i : sum_j + 1 ]

print( f"Sum found between { sum_i } and { sum_j }: min+max = "
       f"{ min( found_range ) + max( found_range ) }:" )
