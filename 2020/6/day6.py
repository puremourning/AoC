#!/usr/bin/env python3

from collections import defaultdict

PART = 2

# file_name = 'example_input.txt'
file_name = 'input.txt'

with open( file_name ) as f:
  groups = f.read().split( '\n\n' )

sum = 0
for group in groups:
  answers = defaultdict( int )
  group = group.splitlines()
  for person in group:
    for question in person:
      answers[ question ] += 1

  if PART == 1:
    sum += len( answers )
  else:
    for answer, count in answers.items():
      if count == len( group ):
        sum += 1


print( f"Sum: { sum }" )
