# the same as program two but only for those named Alice or Bob
print "What is your name?"

name = raw_input("> ")

if name == "Alice" or name == "Bob":
    print "Hello, %s." % name

else:
    print "Hello."
