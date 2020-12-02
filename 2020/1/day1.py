#!/bin/env python3

with open( 'input.txt' ) as f:
  numbers = sorted( int( i ) for i in f.read().splitlines() )


class NotFound( Exception ):
  pass


def FindPair( val ):
  i = 0
  j = len( numbers ) - 1

  while i < j:
    tot = numbers[ i ] + numbers[ j ]
    if tot < val:
      i = i + 1
    elif tot > val:
      j = j - 1
    else:
      return i, j

  raise NotFound()


def Part1():
  i, j = FindPair( 2020 )
  print( f"Part1: { numbers[ i ] * numbers[ j ] }" )


def Part2():
  for n in numbers:
    to_find = 2020 - n
    try:
      i, j = FindPair( to_find )
      print( f"Part2: { numbers[ i ] * numbers[ j ] * n }" )
      break
    except NotFound:
      pass


Part1()
Part2()
