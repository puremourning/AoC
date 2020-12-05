#!/usr/bin/env python3

if 0:
  passes = (
    "FBFBBFFRLR",
    "BFFFBBFRRR", #: row 70, column 7, seat ID 567.
    "FFFBBBFRRR", #: row 14, column 7, seat ID 119.
    "BBFFBBFRLL", #: row 102, column 4, seat ID 820.
  )
else:
  with open( 'input.txt' ) as f:
    passes = f.read().splitlines()


def Walk( low: int, high: int, path: str, lower='F', upper='B' ):
  for index, letter in enumerate( path ):
    half_range = int( ( high - low ) / 2 )

    if low == high:
      break

    if letter == lower:
      high = low + half_range
    elif letter == upper:
      low = high - half_range
    else:
      raise ValueError( f"Unexpected letter: { letter }" )

  assert low == high

  return low, index


seen = []

for i, p in enumerate( passes ):
  row, idx = Walk( 0, 127, p )
  col, chk = Walk( 0, 7, p[ idx : ], 'L', 'R' )

  seat_id = row * 8 + col
  seen.append( seat_id )

  print( f'row: { row }, col: { col }, ID: { seat_id }' )


seen = sorted( seen )
print( f"Max seat ID: { seen[ -1 ] }" )

for index, seat_id in enumerate( seen ):
  if index > 0 and index < len( seen ):
    if seen[ index - 1 ] != seat_id - 1:
      print( f"My seat: { seat_id - 1 }" )
      break
