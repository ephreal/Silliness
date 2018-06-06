import funcoder
import encoders
import base64

"""
This is a catchall class that
implements everything in the 
funcoder module. It's likely going
to be one huge class. we'll see
how much I like it. If it just
feels like a terrible idea, I may
not bother using it.
"""

class encoder():

# The encoder class accetps two arguments
# when creating: the message you are 
# encoding (or decoding), and the options
# which tell it HOW to do the encoding or
# decoding. 

# When encoding, the message can be ascii
# or base64. When decoding, the message 
# can be base64 or base10.

# Options are a string. Each option in the
# string is separated by a colon. The first
# option tells the encoder how to treat the
# initial message (As ascii, b10, or b64).
# Valid options strings follow.

# Options:

# asc : Only ever used to tell the encoder
#       the starting text is ascii.

# b10 : Only ever used to tell the encoder
#       the starting message is base10.

# b10c : Cipher the b10 at this step

# b10d : Decode b10 to b64 at this step

# b10e : Encode to base10 at this step

# b64c : Cipher the b64 at this step

# b64d : Decode b64 to ascii at this step

# b64e : Encode to base64 at this step


# Examples:
#   Encode ascii to base10:
#     b64e:b10e

#   Decode base10 to ascii
#     b10d:b64d

#   Cipher the base64 then convert to base10
#     b64:b64c-10:b10e

#   Encode to base10 and cipher the base10
#     b64:b10e:b10c+4

	def __init__(self, message=None, options=None):
		self.message = message
		self.options = self.split_options(options)

	def split_options(self, options):
		if options is not None:
			options = options.split(":")

		return options

	def handle_options(self):

		commands = {
					"b10c" : self.b10c, "b10d" : self.b10d,
					"b10e" : self.b10e, "b64c" : self.b64c,
					"b64d" : self.b64d, "b64e" : self.b64e
		}
		for i in self.options:
			# remove any offsets (if there are any)
			if "+" in i or "-" in i:
				cmd = i[0:4]
			else:
				cmd = i

			self.message = commands[cmd](i)

	def b10c(self, options):
		offset = int(options[4:])
		return encoders.b10_caeser_cipher(self.message, offset)

	def b10d(self, options):
		return encoders.b10_to_any(self.message, 64)

	def b10e(self, options):
		return encoders.b64_to_b10(self.message)

	def b64c(self, options):
		offset = int(options[4:])
		return encoders.caeser_encode(self.message, offset)

	def b64d(self, options):
		message = self.message
		message = funcoder.graceful_decode(message)
		return message


	def b64e(self, options):
		if isinstance(self.message, int):
			self.message = str(self.message)
		message = self.message.encode()
		message = base64.b64encode(message)
		return message.decode()