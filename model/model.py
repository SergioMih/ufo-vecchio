import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
    def getAnni(self):
        tupla_anni = DAO.getAnni()
        return tupla_anni
    def buildGraph(self,anno):
        self.grafo.clear()
        nodes = DAO.getNodes(anno)
        self.grafo.add_nodes_from(nodes)
        for n1 in self.grafo.nodes:
            for n2 in self.grafo.nodes:
                if n1 != n2 :
                    data1 = DAO.getData(anno,n1)[0]
                    data2 = DAO.getData(anno,n2)[-1]
                    if data2 > data1:
                        self.grafo.add_edge(n1,n2)
        print(len(self.grafo.edges))

    def getNodes(self):
        return list(self.grafo.nodes)
    def getps(self,nodo):
        pred = self.grafo.predecessors(nodo)
        listP =[]
        for p in pred:
            listP.append(p)
        succ = self.grafo.successors(nodo)
        listS=[]
        for s in succ:
            listS.append(s)
        return listP,listS

    def getRaggiungibili(self,nodo):
        tree = list(nx.bfs_tree(self.grafo,nodo))
        tree.remove(nodo)
        print (len(tree))
        return tree

    def getCammino(self,n):
        self.bestPath=[]
        self.bestObj =0
        parziale=[n]
        self.ricorsione(parziale)
        return self.bestPath
    def ricorsione(self,parziale):
        if len(parziale)>self.bestObj:
            self.bestPath = copy.deepcopy(parziale)
            self.bestObj = len(parziale)
        succ = list(self.grafo.successors(parziale[-1]))
        for node in succ:
            if node not in parziale:
                parziale.append(node)
                self.ricorsione(parziale)
                parziale.pop()



