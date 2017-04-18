# the same thing as program four, but only using multiples of 3 and 5.

print "Give me a number"
n = raw_input("> ")
n = int(n)

sum = 0

for i in range (1, n):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print sum
