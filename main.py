import field

b = field.Board(47, 5)
print b.get_cost()

for i in xrange(10000):
    current_val = b.get_cost()
    b.swap_random()

    if b.get_cost() <= current_val:
        b.unswap()
    
    if i % 100 == 0:
        print i, ": ", current_val

print "Result: ", current_val

for patch in [ patch for row in b.patches for patch in row ]:
    print "Number: ", patch.number, "Position: ", patch.position
