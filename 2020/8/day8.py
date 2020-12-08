#!/usr/bin/env python3

from collections import namedtuple

Instruction = namedtuple( "Instruction", [ "inst", "operand" ] )

filename = 'input.txt'


class InfiniteLoop( Exception ):
  pass


def Run( patch_instruction = None ):
  acc = 0
  trace = set()
  pc = 0

  while pc < len( program ):
    if pc in trace:
      raise InfiniteLoop(
        f"Loop detected with accumulator: { acc } at pc { pc }" )

    i = program[ pc ]
    trace.add( pc )

    if i.inst == 'acc':
      acc += i.operand
      pc += 1
    elif i.inst == 'nop':
      if pc == patch_instruction:
        pc += i.operand
      else:
        pc += 1
    elif i.inst == 'jmp':
      if pc == patch_instruction:
        pc += 1
      else:
        pc += i.operand

  if pc >= len( program ):
    print( f"End of program: accumulator: { acc }" )

  # Finished
  return acc


program = []
with open( filename ) as f:
  lines = f.read().splitlines()

for line in lines:
  inst, operand = line.split( ' ', 1 )
  operand = int( operand )
  program.append( Instruction( inst, operand ) )

print( "Part1:" )

try:
  Run()
except InfiniteLoop as e:
  print( str( e ) )

print( "Part2:" )

for to_patch in range( len( program ) ):
  try:
    Run( to_patch )
    break
  except InfiniteLoop:
    pass

