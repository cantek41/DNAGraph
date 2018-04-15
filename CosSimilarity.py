import dnaToGraph as dna
from math import *
import networkx as nx
import numpy as np


class CosSim():

    def __init__(self, graph1, graph2):
        self.graph1 = graph1
        self.graph2 = graph2

    def _Similarity(self, list1, list2):
        tmp = [0 for x in range(min(list1.shape[0], list2.shape[0]))]
        ii = 0
        s = 0
        for i in range(min(list1.shape[0], list2.shape[0])):
            for j in range(min(list1.shape[0], list2.shape[0])):
                s += list1[i][j] * list2[i][j]
            dd = (np.linalg.norm(list1[i]) * np.linalg.norm(list2[i]))
            if dd != 0:
                tmp[ii] = s / dd
            s = 0
            ii += 1
        return np.mean(tmp)

    def getSimilarity(self):
        if self.graph1.size() < self.graph2.size():
            return self._Similarity(np.array(nx.to_numpy_matrix(self.graph1)),
                                    np.array(nx.to_numpy_matrix(self.graph2)))
        else:
            return self._Similarity(np.array(nx.to_numpy_matrix(self.graph2)),
                                    np.array(nx.to_numpy_matrix(self.graph1)))


if __name__ == "__main__":
    nbsimilarity = CosSim(dna.H, dna.C)
    print(nbsimilarity.getSimilarity())
