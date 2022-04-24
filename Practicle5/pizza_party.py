# First, code to calculate pizza slices under given cuts.
# Second, code a loop to find out the number of cuts for 64 slices. (1 slide for each IBIers)

# pseudocode:
# cuts = 1
# while (True)
#   calculate the slices under certain cuts
#   cuts++
#   print slices and cuts number
#   if slices >= 64
#       break
# prints results

cuts = 1
slices = 0
while True:
# I set the condition as "True" to make an "infinite" loop until it meets the command "break".
    slices = (cuts ** 2 + cuts + 2) / 2
    cuts = cuts + 1
    if slices >= 64:
        break
        # Now it's time to jump out of this loop.
print("cuts:",cuts,"slices:", slices)


# I wonder why the output numbers include fractional parts like 64.0.
