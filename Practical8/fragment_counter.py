import re

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
count = len(re.findall('GAATTC', seq)) + 1
print(count)
