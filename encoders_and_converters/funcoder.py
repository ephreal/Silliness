import base64
import sys
from encoders import *

"""
This sets up some functions that use my encoders
to do fun an interesting things, hence the name.
Again, this is not encryption. Don't even think
about using this in anything serious. This is 
all just for fun, like sending encoded messages
everyone did as a kid.
"""

def b10_to_ascii(some_int):
	"""
	Converts a base 10 number into an ASCII
	string. It accomplishes this by turning
	it into a base64 string, and then trying
	to decrypt it with b64decode.

	Giving it random numbers will probably
	not do anything intersting. Try encoding
	with ascii_to_b10 first.
	"""
	some_int = b10_to_any(some_int, 64)
	some_int = graceful_decode(some_int)

	return some_int

def ascii_to_b10(some_ascii):
	"""
	Encodes a string as a base10 number.
	Accomplished by b64encoding the string
	and calculating what the b64 string is
	in decimal.

	Undone by using b10_to_ascii
	"""
	enc = base64.b64encode(some_ascii.encode())
	enc = b64_to_b10(enc.decode())

	return enc

def b10_caeser_ascii(b10, offset):
	"""
	Things get a little more interesting here.
	Decodes a base 10 number as though it is a
	base64 caeser ciphered string. See 
	ascii_caeser_10 for a description of how it
	got there.
	"""
	b10 = b10_to_any(b10, 64)
	b10 = caeser_encode(b10, offset)
	b10 = graceful_decode(b10)

	return b10

def ascii_caeser_b10(ascii_str, offset):
	"""
	Things get a little more interesting here.
	Encodes a string as a base10 int by
	encoding it as a base64 number, running the
	simple caeser cipher over it, checking that
	the string doesn't have "A" as it's first
	letter (A is 0 in base 64), and then calculating
	the base10 equivalent of that string. If the 
	Caeser cipher of the base64 string starts with
	an A, it'll shout at you, you can feel bad, and
	then increment your offset by 1.
	"""

	encoded_str = base64.b64encode(ascii_str.encode())
	encoded_str = encoded_str.decode()
	encoded_str = caeser_encode(encoded_str, offset)
	copy = encoded_str
	encoded_str = b64_to_b10(encoded_str)

	# Time for some error checking
	decoded = b10_to_any(encoded_str, 64)
	if decoded != copy.replace("=", ''):
		print("Error encoding. Original might start with 'A' (0 in base 10)")
		print(f"Original: {copy}")
		print(f"Decoded:  {decoded}")
		sys.exit()


	return encoded_str

def graceful_decode(b64_string):
	"""
	Makes sure that padding is correct
	when trying to decode a base64
	encoded string. Sometimes (often) 
	there are '='' signs missing. 
	"""
	decoded = False
	counter = 0
	while not decoded:
		try:
			b64_string = base64.b64decode(b64_string)

		except:
			b64_string += "="
			counter += 1
			decoded = False
			# This works in groups of four. More than 
			# 4 iterations means somethine is REALLY
			# messed up. Invalid encoding, etc.
			if counter > 4:
				print("base64 is REALLY screwed up...")
				print("Exiting...")
				sys.exit()
			continue

		return b64_string.decode()