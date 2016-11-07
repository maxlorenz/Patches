from image import Image

# Modify to match problem
rows = 5
columns = 47

swaps = 100000

# Setup run
image = Image(rows, columns)
percentage = swaps / 100

for i in xrange(swaps):
    last_cost = image.get_cost()
    image.swap_random()

    if image.get_cost() <= last_cost:
        image.unswap()
    
    # Print percentage
    if i % percentage == 0:
        print i/percentage, "%:", last_cost

# Print every position
for patch in [ patch for row in image.patches for patch in row ]:
    row = patch.position['y'] + 1
    column = patch.position['x'] + 1

    print "Number:", patch.number, "Row:", row, "Column:", column