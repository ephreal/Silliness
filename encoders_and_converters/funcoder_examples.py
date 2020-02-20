import funcoder

"""
Examples of how to use the funcoder
"""

# First an example of ascii to base10
random_problem = "You don't really have a computer. We gave you an " \
                 "Etch-A-Sketch and wanted to see how long before you'd " \
                 "notice..."
b10_problem = funcoder.ascii_to_b10(random_problem)
print(b10_problem)
# prints: 295301391566891845876371984170187444638892141225899025729478102674070
#         260264355713093786889668911885713588761341412938442895372921616335347
#         433150386683370637500692362689584625629143917120531041352733393405728
#         8076363847140478540822896030981344456450670033741698687624733408
# That's a long number....

ascii_problem = funcoder.b10_to_ascii(b10_problem)
print(ascii_problem)
# prints: You don't really have a computer. We gave you an Etch-A-Sketch and
#         wanted to see how long before you'd notice...


# Now an example of the caeser ciphered b10 encoding
random_problem = "Floating Point operations left holes in the motherboard."
# Certifiably random offset here...
b10_problem = funcoder.ascii_caeser_b10(random_problem, 42)
print(b10_problem)
# prints: 338305424980283160307443143273002545793573151750182129042156119995645
#         572535645699690154567627972722722406828056996613120953874783466680

# To "Decode" this, make the offset negative
ascii_problem = funcoder.b10_caeser_ascii(b10_problem, -42)
print(ascii_problem)
# prints: Floating Point operations left holes in the motherboard.


# Proof that the caeser b10 is different than the ascii_to_b10
random_problem = "This is a user error. Replace the user to continue."
b10_problem = funcoder.ascii_to_b10(random_problem)
caeser_b10_problem = funcoder.ascii_caeser_b10(random_problem, 77)

print(b10_problem)
print(caeser_b10_problem)
# prints the following:
# b10_problem = 217962183702530634581528034650361109669548655892357155624308396
#               204829441676850162897719800435909614499457074760279469155630
# caeser_b10_problem = 20746923181697113301086271230063458522782794664619287200
#                      66462330969881957951751127762140532937501688578220975136
#                      62611805421
# Note that they still are the same length though.

# And decoding the above
print(funcoder.b10_to_ascii(b10_problem))
print(funcoder.b10_caeser_ascii(caeser_b10_problem, -77))
# Both print out "This is a user error. Replace the user to continue"

# Proof that the ciphered b10 is different from the ciphered b64 to b10, and
# the usual b10 encoding.
random_problem = "Someone used the printer rollers to flatten a pie crust."
b10_problem = funcoder.ascii_to_b10(random_problem)
caeser_b10_problem = funcoder.ascii_caeser_b10(random_problem, 15)
b10_ciphered = funcoder.ascii_b10_cipher(random_problem, 15)

print(b10_problem)
print(caeser_b10_problem)
print(b10_ciphered)
# prints the following
# b10_problem = 947562189423616587903751129088307189298818016701089801942175719
#               131240414729052667904879791055617106173768517081238398371312447
#               511187640
# caeser_b10_problem = 44785863000993558930983415410400187370029764374207816441
#                      35264379012984857647265895927834257786379196718174643859
#                      05916868755903559681144
# b10_ciphered = 49201763497816103245820667453385263474336356125653435649762026
#                46867959692745071124593242465001626516282130625367838438268679
#                92066632195

# And decipher the above, of course
print(funcoder.b10_to_ascii(b10_problem))
print(funcoder.b10_caeser_ascii(caeser_b10_problem, -15))
print(funcoder.cipher_b10_ascii(b10_ciphered, -15))
# All 3 print out "Someone used the printer rollers to flatten a pie crust."
