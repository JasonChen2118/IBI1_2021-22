# First, code to calculate pizza slices under given cuts.
# Second, code a loop to find out the number of cuts for 64 slices. (1 slide for each IBIers)

# cuts = 1
# while (True)
#   caculate the slices under certain cuts
#   cuts++
#   print slices number
#   if slices >= 64
#       break

cuts = 1
slices = 0
while True:
    slices = (cuts ** 2 + cuts + 2) / 2
    cuts = cuts + 1
    print(slices)
    if slices >= 64:
        break
