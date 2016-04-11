#!/usr/bin/python3


blue =  0xbcc0e8c4c8fad03e 
green = 0x9f0f1d0958991899
red =   0xb3212141a971b1b1


MASKS = [ 
          0x8000000000000000,
          0x4000000000000000,
          0x2000000000000000,
          0x1000000000000000,
          0x0800000000000000,
          0x0400000000000000,
          0x0200000000000000,
          0x0100000000000000,
          0x0080000000000000,
          0x0040000000000000,
          0x0020000000000000,
          0x0010000000000000,
          0x0008000000000000,
          0x0004000000000000,
          0x0002000000000000,
          0x0001000000000000,
          0x0000800000000000,
          0x0000400000000000,
          0x0000200000000000,
          0x0000100000000000,
          0x0000080000000000,
          0x0000040000000000,
          0x0000020000000000,
          0x0000010000000000,
          0x0000008000000000,
          0x0000004000000000,
          0x0000002000000000,
          0x0000001000000000,
          0x0000000800000000,
          0x0000000400000000,
          0x0000000200000000,
          0x0000000100000000,
          0x0000000080000000,
          0x0000000040000000,
          0x0000000020000000,
          0x0000000010000000,
          0x0000000008000000,
          0x0000000004000000,
          0x0000000002000000,
          0x0000000001000000,
          0x0000000000800000,
          0x0000000000400000,
          0x0000000000200000,
          0x0000000000100000,
          0x0000000000080000,
          0x0000000000040000,
          0x0000000000020000,
          0x0000000000010000,
          0x0000000000008000,
          0x0000000000004000,
          0x0000000000002000,
          0x0000000000001000,
          0x0000000000000800,
          0x0000000000000400,
          0x0000000000000200,
          0x0000000000000100,
          0x0000000000000080,
          0x0000000000000040,
          0x0000000000000020,
          0x0000000000000010,
          0x0000000000000008,
          0x0000000000000004,
          0x0000000000000002,
          0x0000000000000001
         ]

def pearl_necklace(values):
	val = 0
	bits = 1
	for mask in MASKS:
		for input_val in values:
			new = (input_val & mask) / mask
			val = val << 1
			val += int(new)

			bits+=1
			if bits % 64 == 0:
				bits =0
				print("Val is %02x" % val)
				val = 0

import itertools

for perm in list(itertools.permutations([red, green, blue])):
	pearl_necklace(perm)
	print()