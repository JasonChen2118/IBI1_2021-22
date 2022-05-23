from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt


def node_sum(id):
    global term_childNode_nore, temp
    for j in range(len(all_is_a)):
        for k in range(len(all_is_a[j])):
            if all_is_a[j][k] == id:
                storage[temp].append(all_id[j])
                if not boolean[j]:
                    node_sum(all_id[j])
                    # If the childnode have not been searched, then searched the childnode's childnode.
                storage[temp] = storage[temp] + storage[j]
    boolean[all_id.index(id)] = True


DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
print("There are", len(terms), "terms in go_obo.xml")
# here counts the total number of GO terms

all_id = []
# All GO ID are stored in this list.
all_is_a = []
# All "is a" for all GO terms are stored (2 dimensions list).
# This is only one layer. Only the straight childnode of terms are calculated in this list.
storage = []
# All childnodes for all GO terms are stored.
# This is multi layers. In this list, childnodes of childnodes are included, but the repeat childnodes are not deleted.
boolean = []
# This list stores whether the childnodes of a term have been searched. If searched, then True. If not, then False.
# All 4 lists above have corresponding relationship.
# "all_id[n]", "all_is_a[n]", "storage[n]" and "boolean[n]" describe a same GO term.
for i in range(len(terms)):
    storage.append([])
    boolean.append(False)  # Initialise all boolean value as "False"
for i in range(len(terms)):
    is_a = terms[i].getElementsByTagName("is_a")
    all_id.append(terms[i].getElementsByTagName("id")[0].childNodes[0].data)
    all_is_a.append([])
    for j in range(len(is_a)):
        all_is_a[i].append(terms[i].getElementsByTagName("is_a")[j].childNodes[0].data)
    # store information of terms id and "is a"

all_term_childNode = []
# This list stores all total childnodes without repetition.
translation = []
# Translation relate GO
temp = 0
for i in range(len(all_id)):
    temp = i
    term_childNode_nore = []
    node_sum(all_id[i])
    for l in storage[i]:
        if l not in term_childNode_nore:
            term_childNode_nore.append(l)
    # Delete repetition
    print(i, len(term_childNode_nore))
    # An output was put here to check whether the code is running
    all_term_childNode.append(len(term_childNode_nore))
    if terms[i].getElementsByTagName("defstr")[0].childNodes[0].data.find("translation") != -1:
        translation.append(len(term_childNode_nore))
    # Final total number of child nodes are stored in "all_term_childNode" and "translation"

# boxplot drawing
plt.boxplot(all_term_childNode)
plt.title('Distribution of child node number of all GO terms')
plt.xlabel("all GO terms")
plt.ylabel("Number")
plt.show()
plt.boxplot(translation)
plt.title('Distribution of child node number of terms associated with ‘translation’')
plt.xlabel("associated with ‘translation’")
plt.ylabel("Number")
plt.show()
print("There are", len(terms), "terms in go_obo.xml")
print("The boxplot of child node distribution are showing.")

"""
Translation terms contain smaller number of child nodes than the overall GO.
The second picture has similar overview with the first picture, but the number is much more smaller.
"""
