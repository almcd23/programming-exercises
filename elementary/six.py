print "Give me a number"
n = raw_input("> ")
n = int(n)

sum = 0
prod = 1

print "Do you want to compute the sum or the product?"
equate = raw_input("> ")

if equate == 'sum':
    for i in range (1, n):
        sum = sum + 1
    print sum

elif equate == 'product':
    for i in range (1, n):
        prod = prod * i
    print prod
