import re

fin = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
fout = open('cut_genes.fa','w')

name_list = []
length_list = []
seq_list = []

i = 0
for line in fin:
    if line.startswith('>'):
        name = '>' + re.findall(r'gene:(\w+)',line)[0]
        name_list.append(name)
        i = i + 1
    if not line.startswith('>'):
        edited_line = re.findall(r'(\w+)\n', line)[0]
        if len(seq_list) < i:
            seq_list.append(edited_line)
        else:
            seq_list[i - 1] = seq_list[i - 1] + edited_line

for i in range(len(name_list)):
    length_list.append(len(seq_list[i]))

for i in range(len(seq_list)):
    if len(re.findall("GAATTC", seq_list[i])) != 0:
        fout.write(name_list[i])
        fout.write('    ')
        fout.write(str(length_list[i]))
        fout.write('\n')
        fout.write(seq_list[i])
        fout.write('\n')

fout.close()