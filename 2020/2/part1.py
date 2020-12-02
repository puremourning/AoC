#!/usr/bin/env python3

PART = 1

with open( 'input.txt' ) as f:
  rules = f.read().splitlines()

valid = []

for line in rules:
  rule, data = line.split( ': ' )
  min_max, letter = rule.split( ' ' )
  lmin, lmax = min_max.split( '-' )

  # Part 1
  if PART == 1:
    num_letter = len( [ x for x in data if x == letter ] )
    lmin = int( lmin )
    lmax = int( lmax )
    if num_letter >= lmin and num_letter <= lmax:
      valid.append( data )

  # Part 2
  if PART == 2:
    lmin = int( lmin ) - 1
    lmax = int( lmax ) - 1

    try:
      if data[ lmin ] == letter and data[ lmax ] != letter:
        valid.append( data )
      elif data[ lmin ] != letter and data[ lmax ] == letter:
        valid.append( data )
    except IndexError:
      pass

print( f"Valid: {len(valid)}" )
