# sum all numbers from 1 to the input
print "Give me a number"
n = raw_input("> ")
n = int(n)

sum = 0

for i in range (1, n):
    sum = sum + i
print sum
