# Pseudocode of the question "How many dots in triangles?"
# set 10 triangles
# take 10 loops
#   dots = 1 + 2 + 3 ... plus n
#   n = n + 1   till 10
#   print dots

triSum = 10
dotsSum = 0
for i in range(1, triSum + 1):
    dotsSum = dotsSum + i
    print(dotsSum)
    i = i + 1
