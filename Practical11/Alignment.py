genedict = {}

human = open('DLX5_human.fa')
for line in human:
    if not line.startswith(">"):
        genedict['human'] = line

mouse = open('DLX5_mouse.fa')
for line in mouse:
    if not line.startswith(">"):
        genedict['mouse'] = line

random = open('RandomSeq(1).fa')
print(random)
for line in random:
    if not line.startswith(">"):
        genedict['random'] = line

human_mouse_ct = 0
for i in range(len(genedict['human'])):
    if genedict['human'][i] == genedict['mouse'][i]:
        human_mouse_ct = human_mouse_ct + 1

human_random_ct = 0
for i in range(len(genedict['human'])):
    if genedict['human'][i] == genedict['random'][i]:
        human_random_ct = human_random_ct + 1

mouse_random_ct = 0
for i in range(len(genedict['mouse'])):
    if genedict['mouse'][i] == genedict['random'][i]:
        mouse_random_ct = mouse_random_ct + 1

human_mouse_pc = human_mouse_ct / len(genedict['human'])
human_random_pc = human_random_ct / len(genedict['human'])
mouse_random_pc = mouse_random_ct / len(genedict['mouse'])

print(human_mouse_ct, human_random_ct, mouse_random_ct)
print(human_mouse_pc, human_random_pc, mouse_random_pc)

