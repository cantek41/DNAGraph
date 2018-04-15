import dnaToGraph as dna
from math import *
import networkx as nx


class NbSimilarity():

    def __init__(self, graph1, graph2, alfa):
        self.graph1 = graph1
        self.graph2 = graph2
        self.alfa = alfa

        self.inNodeSimilarity = [[0 for x in range(graph2.number_of_nodes())] for y in range(graph1.number_of_nodes())]
        self.outNodeSimilarity = [[0 for x in range(graph2.number_of_nodes())] for y in range(graph1.number_of_nodes())]
        self.nodeSimilarity = [[0 for x in range(graph2.number_of_nodes())] for y in range(graph1.number_of_nodes())]
        self._init()

    def _init(self):
        ii, jj = 0, 0
        for i in self.graph1.nodes():
            for j in self.graph2.nodes():
                maxdegree = max(self.graph1.in_degree(i), self.graph2.in_degree(j))
                if maxdegree == 0:
                    self.inNodeSimilarity[ii][jj] = 0
                else:
                    self.inNodeSimilarity[ii][jj] = min(self.graph1.in_degree(i), self.graph2.in_degree(j)) / maxdegree


                maxdegree = max(self.graph1.out_degree(i), self.graph2.out_degree(j))
                if maxdegree == 0:
                    self.outNodeSimilarity[ii][jj] = 0
                else:
                    self.outNodeSimilarity[ii][jj] = min(self.graph1.out_degree(i), self.graph2.out_degree(j)) / maxdegree


                self.nodeSimilarity[ii][jj] = (self.inNodeSimilarity[ii][jj] + self.outNodeSimilarity[ii][jj]) / 2
                jj += 1
            ii += 1
            jj = 0


    def _Similarity(self):
        checkDifferrence = True
        while checkDifferrence:
            maxDifference = 0
            ii, jj = 0, 0
            for i in self.graph1.nodes():
                for j in self.graph2.nodes():
                    maxdegree = max(self.graph1.in_degree(i), self.graph2.in_degree(j))
                    minDegree = min(self.graph1.in_degree(i), self.graph2.in_degree(j))
                    if minDegree == self.graph1.in_degree(i):
                        similaritySum = self.enumerationFunction(
                            list(set(nx.all_neighbors(self.graph1, i)) - set(self.graph1.neighbors(i))),
                            list(set(nx.all_neighbors(self.graph2, j)) - set(self.graph2.neighbors(j))),
                        0)
                    else:
                        similaritySum = self.enumerationFunction(
                            list(set(nx.all_neighbors(self.graph2, j)) - set(self.graph2.neighbors(j))),
                            list(set(nx.all_neighbors(self.graph1, i)) - set(self.graph1.neighbors(i))),
                        1)

                    if maxdegree == 0 and similaritySum == 0:
                        self.inNodeSimilarity[ii][jj] = 1
                    elif maxdegree == 0:
                        self.inNodeSimilarity[ii][jj] = 0
                    else:
                        self.inNodeSimilarity[ii][jj] = similaritySum / maxdegree

                    # outdegre hesaplaması
                    maxdegree = max(self.graph1.out_degree(i), self.graph2.out_degree(j))
                    minDegree = min(self.graph1.out_degree(i), self.graph2.out_degree(j))
                    if minDegree == self.graph1.out_degree(i):
                        similaritySum = self.enumerationFunction(list(self.graph1.neighbors(i)),
                                                                 list(self.graph2.neighbors(j)), 0)
                    else:
                        similaritySum = self.enumerationFunction(list(self.graph2.neighbors(j)),
                                                                 list(self.graph1.neighbors(i)), 1)

                    if maxdegree == 0 and similaritySum == 0:
                        self.outNodeSimilarity[ii][jj] = 1
                    elif maxdegree == 0:
                        self.outNodeSimilarity[ii][jj] = 0.0
                    else:
                        self.outNodeSimilarity[ii][jj] = similaritySum / maxdegree

                    tmp = (self.inNodeSimilarity[ii][jj] + self.outNodeSimilarity[ii][jj]) / 2
                    if abs(self.nodeSimilarity[ii][jj] - tmp) > maxDifference:
                        maxDifference = abs(self.nodeSimilarity[ii][jj] - tmp)
                    self.nodeSimilarity[ii][jj] = tmp

                    if maxDifference < self.alfa:
                        checkDifferrence = False
                    jj += 1
                ii += 1
                jj = 0


    def enumerationFunction(self, nbList1, nbList2, graph):
        dict = {}
        if graph == 0:
            for i in nbList1:
                max = 0
                key = ""
                ii = self.getindex(self.graph1, i)
                for j in nbList2:
                    jj = self.getindex(self.graph2, j)
                    if not dict.get(j):
                        if max < self.nodeSimilarity[ii][jj]:
                            max = self.nodeSimilarity[ii][jj]
                            key = j
                dict[key] = max
            similaritySum = sum(dict.values())
        else:
            for i in nbList1:
                max = 0
                key = ""
                ii = self.getindex(self.graph2, i)
                for j in nbList2:
                    jj = self.getindex(self.graph1, j)
                    if not dict.get(j):
                        if max < self.nodeSimilarity[jj][ii]:
                            max = self.nodeSimilarity[jj][ii]
                            key = j
                dict[key] = max
            similaritySum = sum(dict.values())

        return abs(similaritySum)

    def getindex(self, nbList1, c):
        index = 0
        for i in nbList1:
            if i==c:
                break
            index +=1
        return index


    def getSimilarity(self):
        self._Similarity()
        if self.graph1.size() < self.graph2.size():
            similarity = self.enumerationFunction(self.graph1.nodes(), self.graph2.nodes(), 0) / self.graph1.number_of_nodes()
        else:
            similarity = self.enumerationFunction(self.graph2.nodes(), self.graph1.nodes(), 1) / self.graph2.number_of_nodes()
        return similarity


if __name__ == "__main__":
    nbsimilarity = NbSimilarity(dna.H, dna.H, 0.0001)
    print(nbsimilarity.getSimilarity())
