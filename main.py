import field
b = field.Board(47, 5)

for i in xrange(100000):
    current_val = b.get_cost()
    b.swap_random()

    if b.get_cost() <= current_val:
        b.unswap()
    
    if i % 1000 == 0:
        print i/1000, "%:", current_val

for patch in [ patch for row in b.patches for patch in row ]:
    row = patch.position['y'] + 1
    column = patch.position['x'] + 1

    print "Number:", patch.number, "Row:", row, "Column:", column