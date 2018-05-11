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
b10_problem = funcoder.ascii_to_b10(random_problem)
caeser_b10_problem = funcoder.ascii_caeser_b10(random_problem, 77)

print(b10_problem)
print(caeser_b10_problem)
# prints the following:
# b10_problem        = 217962183702530634581528034650361109669548655892357155624308396204829441676850162897719800435909614499457074760279469155630
# caeser_b10_problem = 207469231816971133010862712300634585227827946646192872006646233096988195795175112776214053293750168857822097513662611805421
# Note that they still are the same length though.
