print "Give me a number"
n = raw_input("> ")

if n.isDigit():
    n = int(n)
    print n + 1
else:
    print "what?"
