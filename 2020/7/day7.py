#!/usr/bin/env python3


filename = 'input.txt'

import typing
import re
from collections import defaultdict

RULE_REGEXP = re.compile( r'''
  (?P<colour>[a-z ]+)    # a bag colour
  \ bags\ contain\       # followed by "bags contain"
  (?P<contains>          # forllowed by either...
    (?P<contains_nothing>no\ other\ bags\.)  # no bags
  |                                          # or...
    (?P<contains_list>                # a list of contained bags, consisting
     (
      \d+                             # a nubmer
      \                               # a space
      [a-z ]+                         # a colour
      \ bags?[.,]\ ?                  # space, bag or bags, full stop or comma
     )+                               # contains list 1 or more time
    )
  )
''', re.IGNORECASE | re.VERBOSE )

CONTAINS_REGEX = re.compile( r'''
  (?P<cbags>\d+)                  # a nubmer
  \                               # a space
  (?P<ccolour>[a-z ]+)            # a colour
  \ bags?\.?
''', re.IGNORECASE | re.VERBOSE )

with open( filename ) as f:
  rules = f.read().splitlines()


class Bag:
  contains: typing.List[ typing.Tuple[ str, int ] ]

  def __init__( self ):
    self.contains = []


graph: typing.DefaultDict[ typing.AnyStr, Bag ] = defaultdict( Bag )

for rule in rules:
  print( f"Rule: { rule }" )
  rule_match = RULE_REGEXP.match( rule )
  if not rule_match:
    raise ValueError( f" Rule '{ rule }' does not match" )

  print( f" Match groups = { rule_match.groupdict() }" )

  bag = graph[ rule_match.group( 'colour' ) ]
  if rule_match.group( "contains_nothing" ):
    print( " CONTAINS NOTHING" )
    continue

  contains_list = rule_match.group( "contains_list" )
  for contains_rule in re.split( r', ', contains_list ):
    contains_match = CONTAINS_REGEX.match( contains_rule )
    if not contains_match:
      raise ValueError( f"contains_rule does not match { contains_rule }" )

    bag.contains.append( ( contains_match.group( "ccolour" ),
                           int( contains_match.group( "cbags" ) ) ) )


def CanContain( colour: str, bag: Bag ):
  for contents in bag.contains:
    if colour == contents[ 0 ]:
      return True
    if CanContain( colour, graph[ contents[ 0 ] ] ):
      return True

  return False


bags_that_can_contain = 0

for colour, bag in graph.items():
  if CanContain( "shiny gold", bag ):
    print( f"{ colour }" )
    bags_that_can_contain += 1

print( f"Can be in { bags_that_can_contain } bags" )


def CountBags( bag ):
  bags = 1 # this bag
  for contents in bag.contains:
    bags += CountBags( graph[ contents[ 0 ] ] ) * contents[ 1 ]

  return bags


# Note CountBags - 1 becaues we don't count the shiny gold bag itself
print(  "shiny gold bags contain: "
       f"{ CountBags( graph[ 'shiny gold' ] ) - 1 } other bags" )


