# Pseudocode of the question "How many dots in triangles?"
# set 10 triangles
# take 10 loops
#   dots = 1 + 2 + 3 ... plus n
#   n = n + 1   till 10
#   print dots

triSum = 10
# This can be improved by using "input" to customize the number of triangles.
dotsSum = 0
# Initialize the sum of dots.

for i in range(1, triSum + 1):
    dotsSum = dotsSum + i
    print(dotsSum)
    i = i + 1
