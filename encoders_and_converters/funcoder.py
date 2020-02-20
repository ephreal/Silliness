import base64
import encoders
import sys
import binascii

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
    some_int = encoders.base_ten_to_any(some_int, 64)
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
    enc = encoders.b64_to_b10(enc.decode())

    return enc


def ascii_b10_cipher(some_ascii, offset):
    """
    Converts ascii to base10 and then
    runs the b10 through a simple b10
    caeser cipher.
    """

    # Convert to base10
    some_ascii = ascii_to_b10(some_ascii)
    # Shuffle int around
    some_ascii = cipher_b10(some_ascii, offset)

    try:
        b10 = int(some_ascii)
    except Exception:
        print("Error decoding ascii to b10")
        print("cipher_b10 may have returned")
        print("something besides b10 chars.")
        sys.exit()

    return b10


def cipher_b10_ascii(ciphered_b10, offset):
    """
    Deciphers a b10 int that has been encoded
    with a caeser cipher.
    """
    b10 = cipher_b10(ciphered_b10, offset)
    some_ascii = b10_to_ascii(int(b10))

    return some_ascii


def b10_caeser_ascii(b10, offset):
    """
    Things get a little more interesting here.
    Decodes a base 10 number as though it is a
    base64 caeser ciphered string. See
    ascii_caeser_10 for a description of how it
    got there.
    """
    b10 = encoders.base_ten_to_any(b10, 64)
    b10 = encoders.caeser_encode(b10, offset)
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
    encoded_str = encoders.caeser_encode(encoded_str, offset)
    copy = encoded_str
    encoded_str = encoders.b64_to_b10(encoded_str)

    # Time for some error checking
    decoded = encoders.base_ten_to_any(encoded_str, 64)
    if decoded != copy.replace("=", ''):
        print("Error encoding. Original might start with 'A' (0 in base 10)")
        print(f"Original: {copy}")
        print(f"Decoded:  {decoded}")
        sys.exit()

    return encoded_str


def cipher_b10(b10_int, offset):
    b10_int = encoders.b10_caeser_cipher(b10_int, offset)

    b10_int = str(b10_int)

    if b10_int.startswith("0"):
        print("ciphered b10 int starts with 0. Choose a different offset.")
        sys.exit()

    return b10_int


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

        # Note to future self: If this has issues, return to having this be a
        # bare except.
        except binascii.Error:
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
