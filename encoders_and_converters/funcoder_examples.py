import funcoder

"""
Examples of how to use the funcoder
"""

# First an example of ascii to base10
random_problem = "You don't really have a computer. We gave you an Etch-A-Sketch and wanted to see how long before you'd notice..."
b10_problem = funcoder.ascii_to_b10(random_problem)
print(b10_problem)
# prints: 2953013915668918458763719841701874446388921412258990257294781026740702602643557130937868896689118857135887613414129384428953729216163353474331503866833706375006923626895846256291439171205310413527333934057288076363847140478540822896030981344456450670033741698687624733408
# That's a long number....

ascii_problem = funcoder.b10_to_ascii(b10_problem)
print(ascii_problem)
# prints: You don't really have a computer. We gave you an Etch-A-Sketch and wanted to see how long before you'd notice...



# Now an example of the caeser ciphered b10 encoding
random_problem = "Floating Point operations left holes in the motherboard."
# Certifiably random offset here...
b10_problem = funcoder.ascii_caeser_b10(random_problem, 42)
print(b10_problem)
# prints: 338305424980283160307443143273002545793573151750182129042156119995645572535645699690154567627972722722406828056996613120953874783466680

# To "Decode" this, make the offset negative
ascii_problem = funcoder.b10_caeser_ascii(b10_problem, -42)
print(ascii_problem)
#prints: Floating Point operations left holes in the motherboard.


# Proof that the caeser b10 is different than the ascii_to_b10
random_problem = "This is a user error. Replace the user to continue."
b10_problem        = funcoder.ascii_to_b10(random_problem)
caeser_b10_problem = funcoder.ascii_caeser_b10(random_problem, 77)

print(b10_problem)
print(caeser_b10_problem)
# prints the following:
# b10_problem        = 217962183702530634581528034650361109669548655892357155624308396204829441676850162897719800435909614499457074760279469155630
# caeser_b10_problem = 207469231816971133010862712300634585227827946646192872006646233096988195795175112776214053293750168857822097513662611805421
# Note that they still are the same length though.

# And decoding the above
print(funcoder.b10_to_ascii(b10_problem))
print(funcoder.b10_caeser_ascii(caeser_b10_problem, -77))
# Both print out "This is a user error. Replace the user to continue"

# Proof that the ciphered b10 is different from the ciphered b64 to b10, and the usual b10 encoding.
random_problem = "Someone used the printer rollers to flatten a pie crust."
b10_problem        = funcoder.ascii_to_b10(random_problem)
caeser_b10_problem = funcoder.ascii_caeser_b10(random_problem, 15)
b10_ciphered       = funcoder.ascii_b10_cipher(random_problem, 15)

print(b10_problem)
print(caeser_b10_problem)
print(b10_ciphered)
# prints the following
# b10_problem        = 947562189423616587903751129088307189298818016701089801942175719131240414729052667904879791055617106173768517081238398371312447511187640
# caeser_b10_problem = 447858630009935589309834154104001873700297643742078164413526437901298485764726589592783425778637919671817464385905916868755903559681144
# b10_ciphered       = 492017634978161032458206674533852634743363561256534356497620264686795969274507112459324246500162651628213062536783843826867992066632195

# And decipher the above, of course
print(funcoder.b10_to_ascii(b10_problem))
print(funcoder.b10_caeser_ascii(caeser_b10_problem, -15))
print(funcoder.cipher_b10_ascii(b10_ciphered, -15))
# All 3 print out "Someone used the printer rollers to flatten a pie crust."