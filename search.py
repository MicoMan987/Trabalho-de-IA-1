import node # node.py
import queue
import pdb

class Search:
   estadoInicial = None # nó - ainda nao inicializado 
   estadoFinal = None   # nó - ainda nao inicializado
   maxNumberOfNodesStored = 0
   solvability = False
   solution = ''

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
        return str(node.estado) == str(self.estadoFinal.estado) # MUDEI

   def getMaxNumberOfNodesStored(self):
      return self.maxNumberOfNodesStored

   #pesquisa em largura
   def BFS(self):
      #if self.solvability == False: 
      #  self.solution = 'It is impossible to reach a solution'
      #   return
      curNode = self.estadoInicial
      if(self.isSolution(curNode)): return curNode.moveSet
      q = queue.Queue()
      q.put(curNode) #adiciona o nó à fila
      atingidas = [self.estadoInicial] #lista dos estados atingidos
      while(q.qsize()!=0):
         curNode = q.get()
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if(self.isSolution(node)):
               self.solution = node.moveSet
               return
            if(node.estado not in atingidas):
               atingidas.append(node.estado)
               q.put(node)
            if q.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = q.qsize()

   #funcao de pesquisa em profundidade iterativa d -> limite da profundidade
   def pesquisaLarguraIterativa(self):
      #if self.solvability == False: 
      #   self.solution = 'It is impossible to reach a solution'
      #   return
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
      for i in range(len(criancas)):
         if(self.dfs(criancas[i],limite-1)):
            return True
      return False
   
   #heuristicas
   #total das peças fora do sitio
   def misplaced(self, node):
      foraDoSitio = 0
      for i in range(len(node.estado)):
         if node.estado[i] != self.estadoFinal.estado[i] and node.estado[i] != 0:
            foraDoSitio += 1
      return foraDoSitio
   
   #total das distancias das peças
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
   
   def isCycle(self, node, antecessor):
      pdb.set_trace()
      if antecessor == None:
         return False
      if node.estado == antecessor.estado:
         return True
      return self.isCycle(node, antecessor.parent)
      
   #pesquisa gulosa com heuristica 
   #o tipo diz qual a heuristica a ser usada
   def greddy(self, node, tipo):
      pdb.set_trace()
      if(self.isSolution(node)):
         if self.solution == '': self.solution = node.moveSet
         return
      criancas = node.expandeNode()
      nodeToExpand = None
      if tipo == 1:
         minimo = 16
         for crianca in criancas:
            if self.isCycle(crianca, node) == False and self.misplaced(crianca) < minimo:
               minimo = self.misplaced(crianca)
               nodeToExpand = crianca
      elif tipo == 2:
         minimo = 15*6  #distancia maxima de manhattan total
         for crianca in criancas:
            if self.isCycle(crianca, node) == False and self.getManhattanDistance(crianca) < minimo:
               minimo = self.getManhattanDistance(crianca)
               nodeToExpand = crianca
      return self.greddy(nodeToExpand, tipo) 