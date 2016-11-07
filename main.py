from image import Image

# Modify to match problem
rows = 5
columns = 47
width = 3
height = 4.5

# Increase to get better results
swaps = 100000

# Setup
image = Image(rows, columns, patch_width=width, patch_height=height)
percentage = swaps / 100

# Run
for i in xrange(swaps):
    last_total_distances = image.get_total_distances()
    image.swap_random()

    if image.get_total_distances() <= last_total_distances:
        image.undo_swap()
    
    # Print percentage
    if i % percentage == 0:
        print i/percentage, "%:", last_total_distances

# Print results
for patch in image.all_patches():
    row = patch.position['y'] + 1
    column = patch.position['x'] + 1

    print "Number:", patch.number, "Row:", row, "Column:", column