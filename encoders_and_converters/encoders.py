def b10_to_any(b10, base):
	"""
	This will convert the base 10 number b10 to
	the base specified by base. ie: Pass in 32, 64
	to get the int 32 in base 64. Currently only
	works up to base 64.

	If you don't know what a base(whatever) means,
	why are you here? Go learn something over on
	this page: https://en.wikipedia.org/wiki/Radix
	Check out binary and hexadecimal for a start.
	Also good for visualizing:
	https://en.wikipedia.org/wiki/Binary_number#/media/File:Binary_counter.gif
	"""

	# The difference between these 2:
	# If this is being converted to base64, it uses b64.
	# For all others, it uses b16. 
	# This is ONLY because I couldn't find ANY
	# standards on how different bases represent their
	# numbers. If one is found, I'll change it. It's
	# not hard to do.
	b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	b16 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

	if base == 64:
		convert = b64
	elif (base >= 2) and (base < 64):
		convert = b16
	else:
		return "That base is not yet supported."

	if b10 == 0:
		return convert[0]

	conv_num = ""
	curr_val = 1
	places = 0
	while curr_val <= b10:
		curr_val *= base
		places += 1
	# curr_val // 64 because curr_val is currently bigger
	# than b10, and we need it to be smaller.
	curr_val //= base

	while places > 0:
		# Put the b64 value in the right place
		# Get whole number remaining (ie: 142//64 = 2)
		whole = b10 // curr_val
		# Subtract decimal value from value passed in
		b10 -= curr_val * whole
		# Select b64 val based on whole number
		conv_num += convert[whole]

		curr_val //= base
		places -= 1

	return conv_num


def b64_to_b10(b64_string):
	"""
	Converts a base64 string into base 10 number.
	"""
	b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

	curr_pass = 1
	dec_val = 0
	# I need to start from right to left because 
	# I have no idea how many decimal places this
	# will have. Yes... I could figure it out, 
	# but this is simpler. Done like this:
	# for i in reversed b64_string
	for i in b64_string[-1::-1]:
		if i not in b64:
                        # So I can use most anything
                        # as a b64 "number" for fun.
			continue
		dec_val += b64.index(i) * curr_pass
		curr_pass *= 64

	return dec_val



def caeser_encode(phrase, offset):
	"""
	Very simple Caeser cipher. Reminder everyone:
	This is NOT encryption. This is just for fun. 
	Caeser ciphers are very easy to break, 
	especially when implemented as simply as this 
	one is.

	This returns an encoded string in which only
	the uppercase/lowercase parts change. 
	"""

	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	# Note: I could encode in any way I like
	# Ie:
	# lower = 'qwertyuiopasdfghjklzxcvbnm'
	# upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'

	encoded = ''

	for i in phrase:
		if i in lower:
			new_chr = lower[(lower.index(i)+offset)%26]
		elif i in upper:
			new_chr = upper[(upper.index(i)+offset)%26]
		else:
			new_chr = i

		encoded += new_chr

	return encoded

def better_caeser_encode(phrase, offset):
	"""
	Slightly more complex Caeser cipher. 
	import caeser_encode_disclaimer
	print(caeser_encode_disclaimer.text)
	This one would be broken using
	statistical analysis of a large
	body of text.

	I decided to make this more "secure"
	just for the fun of it. enc_range is
	now in random order.

	Returns a string in which
	[A-Za-z0-9] and !@#$%^&*()_+-=:;"'{[}]\/
	<>,.? all change. Includes spaces.
	"""

	enc_range =  'Q6MbxW/52mo@JLa~GB8^"N;p>w:'
	enc_range += '$_)VvS%`DuP]-eE\\(rZt}i<cgs'
	enc_range += 'dfX#lYAIh *T\'.n=1R09kKy[U|'
	enc_range += 'F7qHz!3?4jC&,{+O'

	encoded = ''

	for i in phrase:
		if i in enc_range:
			new_chr = enc_range[(enc_range.index(i)+offset)%95]
		else:
			new_chr = i

		encoded += new_chr

	return encoded

def b10_caeser_cipher(b10_int, offset):
	"""
	This silly caeser cipher mods the integer by some
	amount. Yes, I realize I could run it through the
	one above, but I want one to keep it as a b10 int
	"""

	enc_range = '0123456789'
	encoded = ""

	for i in str(b10_int):
		encoded += enc_range[(enc_range.index(i)+offset) % 10]

	return int(encoded)