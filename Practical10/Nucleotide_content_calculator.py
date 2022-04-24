import re

seq = input("Please input the DNA sequence:")  # Input DNA sequence
A = len(re.findall('A|a',seq))/len(seq)
G = len(re.findall('G|g',seq))/len(seq)
C = len(re.findall('C|c',seq))/len(seq)
T = len(re.findall('T|t',seq))/len(seq)
# The regular expression can detect both "a" and "A".
# "Len" can
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)








