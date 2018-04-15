import networkx as nx
import matplotlib.pyplot as plt
import re

def LZCompress(katar):
    i, k = 0, 2
    n = len(katar)
    tmparray = []
    tmp = ""
    while True:
        if i >= n:
            if tmp:
                tmparray.append(tmp)
            break
        if katar[i] is tmp:
            tmp = tmp + katar[i]
            i += 1
            continue
        tmp = tmp + katar[i]
        if not tmp in tmparray:
            tmparray.append(tmp)
            tmp = ""
        i += 1
    return tmparray


def correctionArray(array):
    i, k = 1, 2
    n = len(array)
    tmparray = []
    tmp = ""
    while True:
        if i >= n:
            if tmp:
                tmparray.append(tmp)
            break
        tmp = array[i]
        tmparray.append(array[i - 1][-1:] + tmp[0])
        if len(tmp) > 1:
            tmparray.append(tmp)
        i += 1
    return tmparray


def creategraph(array):
    G = nx.DiGraph()
    i = 0
    n = len(array)
    while True:
        if i > n - 2:
            break
        G.add_edge(array[i], array[i + 1])
        i += 1
    return G





def readDNAtoFile(filename):
    ff = open(filename, 'r')
    s = ff.read()
    s = re.sub('[0-9]', '', s.rstrip('\n').strip())
    s = re.sub('[\s+]', '', s.rstrip('\n').strip())
    return s

def draw():
    plt.subplot(2, 1, 1)
    plt.title("insan")
    nx.draw(H, node_size=50)
    plt.subplot(2, 1, 2)
    plt.title('şempanze')
    nx.draw(C, node_size=50)
    plt.show()

#dnaHomoSapiens=readDNAtoFile('HomoSapiens.txt')
dnaHomoSapiens="gatcacaggtctatcaccctattaaccactcacgggagctctccatgcatttggtattttcgtctggggggtatgcac" \
               "gcgatagcattgcgagacgctggagccggagcaccctatgtc"
dnaHomoSapiens = LZCompress(dnaHomoSapiens)
dnaHomoSapiens = correctionArray(dnaHomoSapiens)

#dnaChimpanzee=readDNAtoFile('chimpanzee.txt')
dnaChimpanzee = "gtttatgtagcttacccccttaaagcaatacactgaaaatgtttcgacgggtttatatcaccccataaacaaacaggtttggtcctagcctttctatt" \
              "agctcttagtaagattacacat"
dnaChimpanzee = LZCompress(dnaChimpanzee)
dnaChimpanzee = correctionArray(dnaChimpanzee)

H = creategraph(dnaHomoSapiens)
print("insan dna sı grafı node sayısı" ,H.number_of_nodes())
C = creategraph(dnaChimpanzee)
print("şempanze dna sı grafı node sayısı" ,C.number_of_nodes())




if __name__ == "__main__":
    draw()