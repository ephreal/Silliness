from encoder_classes import encoder


# Set up a simple function for ease of use
def encode(message, options):
    x = encoder()
    x.options = options
    x.options = x.split_options(x.options)
    x.message = message
    x.handle_options()
    return x.message


# Here's our message
message = "We have a new emergency number: 0118 999 881 999 119 725 3"
# We're going to base64 encode, then b10 encode
options = "b64e:b10e"

message = encode(message, options)
print(message)
# prints: 260186476658545699224031200683363762457397876178865975956964209160225
#         532223032159326005819120601040527972756126143184358252119914938107036
#         464
# And now to decode. We just do the reverse of encoding
options = "b10d:b64d"
message = encode(message, options)
print(message)

# This time we'll caeser cipher the base64 after initial encoding
# the +10 in this is the caeser offset
options = "b64e:b64c+10:b10e"
message = encode(message, options)
print(message)
# prints: 696040099233193283008468120235867625707853261175725778166135791665272
#         184915168619151166524898033297661749359318809761284803569235180536887
#         36
# And to decode, once again, reverse the steps
options = "b10d:b64c-10:b64d"
message = encode(message, options)
print(message)

# You can also get really ridiculous...
options = "b64e:b64e:b64e:b64c+10:b10e:b10c+7:b64e:b10e"
message = encode(message, options)
print(message)
# prints: 121926666216792874672015766638542326779387273595704312046122399924793
#         090962365323084026986541442599530164867630153210452704768496881460368
#         345275780081073652839804432301282987757275500276137907949010088291254
#         793665785314597355413950773285796233013506262583609078435503068917785
#         972806092256848868180142498488980541645917711048406922231671929840216
#         555771761813327802537784432730029230850490071555870832042114309099349
#         177005139732597275949947095374704267152129563840197949099208818237623
#         002271534872791524795366458341394346858731407618870299111049756391083
#         378496759563616622537177453139546588968883814359666058790337474401665
#         339600
# You could in theory chain these as long as you'd like.
