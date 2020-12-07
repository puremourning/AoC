#!/usr/bin/env python3

import re

input_file = 'data.txt'

with open( input_file ) as f:
  passports = f.read().lstrip().rstrip().split( '\n\n' )


def Between( v, a, b ):
  return v >= a and v <= b


def YearBetween( v, y1, y2 ):
  if not re.match( r'^[0-9]{4}$', v ):
    return False
  return Between( int( v ), y1, y2 )


def ValidHeight( v ):
  match = re.match( r'^(\d+)(cm|in)$', v )
  if not match:
    return False

  if match.group( 2 ) == 'cm':
    return Between( int( match.group( 1 ) ), 150, 193 )
  elif match.group( 2 ) == 'in':
    return Between( int( match.group( 1 ) ), 59, 76 )
  else:
    raise ValueError( "WUT" )


PART = 2
if PART == 1:
  mandatory = {
    'byr': lambda v: True,
    'iyr': lambda v: True,
    'eyr': lambda v: True,
    'hgt': lambda v: True,
    'hcl': lambda v: True,
    'ecl': lambda v: True,
    'pid': lambda v: True,
  }
else:
  mandatory = {
    'byr': lambda v: YearBetween( v, 1920, 2002 ),
    'iyr': lambda v: YearBetween( v, 2010, 2020 ),
    'eyr': lambda v: YearBetween( v, 2020, 2030 ),
    'hgt': lambda v: ValidHeight( v ),
    'hcl': lambda v: re.match( r'^#[0-9a-f]{6}$', v ),
    'ecl': lambda v: v in ( 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ),
    'pid': lambda v: re.match( r'^\d{9}$', v ),
  }

valid = 0
for passport_text in passports:
  passport = {}
  for kv in re.split( r'\s', passport_text ):
    k, v = kv.split( ':', 1 )
    passport[ k ] = v

  is_valid = 1
  for key, validator in mandatory.items():
    if key not in passport:
      is_valid = 0
    elif not validator( passport[ key ] ):
      is_valid = 0

  valid += is_valid

print( f"Valid: {valid}" )
