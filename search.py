import node # node.py
import queue
import pdb

class Search:
   estadoInicial = None # nó - ainda nao inicializado 
   estadoFinal = None   # nó - ainda nao inicializado
   maxNumberOfNodesStored = 0
   solvability = False
   solution = ''
   visited = []

   def __init__(self, estadoInicial, estadoFinal):
      self.estadoInicial = estadoInicial
      self.estadoFinal = estadoFinal
      self.solvability = self.haSolucao(self.estadoInicial.estado, self.estadoFinal.estado)

   #verificar se existe solucao
   def haSolucao(self, estadoInicial, estadoFinal):
       blankRowI = self.blankRow(estadoInicial)
       blankRowF = self.blankRow(estadoFinal)
       inversionsI = self.inversions(estadoInicial)
       inversionsF = self.inversions(estadoFinal)
       return (((blankRowI%2==1) == (inversionsI%2 == 0)) == ((blankRowF%2==1) == (inversionsF%2 == 0)))

   def blankRow(self, config):
      return (config.index(0)//4)

   def inversions(self, config):
       totalInversoes = 0
       for i in range(len(config)):
           for j in range(i+1,len(config)):
               if(config[i] > config[j] and config[j] > 0):
                   totalInversoes += 1
       return totalInversoes

   def isSolution(self, node):
        return str(node.estado) == str(self.estadoFinal.estado)

   def getMaxNumberOfNodesStored(self):
      return self.maxNumberOfNodesStored

   #pesquisa em largura
   def BFS(self):
      curNode = self.estadoInicial
      if(self.isSolution(curNode)): return curNode.moveSet
      q = queue.Queue()
      q.put(curNode) #adiciona o nó à fila
      self.visited.append(self.estadoInicial) #lista dos estados visitados
      while(q.qsize()!=0):
         curNode = q.get()
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if(self.isSolution(node)):
               self.solution = node.moveSet
               return
            if(node.estado not in self.visited):
               self.visited.append(node.estado)
               q.put(node)
            if q.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = q.qsize()

   #funcao de pesquisa em profundidade iterativa d -> limite da profundidade
   def pesquisaLarguraIterativa(self):
      nodeInicial = self.estadoInicial 
      d = 0
      result = self.dfs(nodeInicial,d)
      while(not result):
        d += 1
        result = self.dfs(nodeInicial,d)
      return d

   def dfs(self, node, limite):
      if(self.isSolution(node)):
         if self.solution == '': self.solution = node.moveSet
         return True
      if limite <= 0:
         return False
      criancas = node.expandeNode()
      for crianca in criancas:
         if(self.dfs(crianca,limite-1)):
            return True
      return False
   
   #heuristicas
   #somatório do número de peças fora do lugar
   def misplaced(self, node):
      foraDoSitio = 0
      for i in range(len(node.estado)):
         if node.estado[i] != self.estadoFinal.estado[i] and node.estado[i] != 0:
            foraDoSitio += 1
      return foraDoSitio
   
   #somatório das distâncias de cada peça ao seu lugar na configuração final
   def getManhattanDistance(self, node):
        manhattan = 0
        for i in range(1,16):
            collumnDifference = node.estado.index(i)%4-self.estadoFinal.estado.index(i)%4
            if collumnDifference < 0:
                collumnDifference *= -1
            rowDifference = int(node.estado.index(i)/4) - int(self.estadoFinal.estado.index(i)/4)
            if(rowDifference<0):
                rowDifference *= -1
            manhattan += collumnDifference + rowDifference
        return manhattan


   def greddy(self, node, tipo):
      while True:
         if(self.isSolution(node)):
            if self.solution == '': self.solution = node.moveSet
            return
         criancas = node.expandeNode()
         if tipo == 1:
            minimo = 16
            for crianca in criancas:
               if crianca not in self.visited:
                  self.visited.append(crianca)
                  if self.misplaced(crianca) < minimo:
                     minimo = self.misplaced(crianca)
                     node = crianca
         elif tipo == 2:
            minimo = 15*6  #distancia maxima de manhattan total
            for crianca in criancas:
               if crianca not in self.visited:
                  self.visited.append(crianca)
                  if self.getManhattanDistance(crianca) < minimo:
                     minimo = self.getManhattanDistance(crianca)
                     node = crianca
