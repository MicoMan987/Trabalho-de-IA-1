import node # node.py
import queue

class Pair:
   def __init__(self, node, cost):
      self.node = node
      self.cost = cost

   def __lt__(self, other):
      return self.cost < other.cost

      
class Search:
   estadoInicial = None # nó inicial- ainda nao inicializado 
   estadoFinal = None   # nó final - ainda nao inicializado
   maxNumberOfNodesStored = 0
   solvability = False
   solution = ''
   visited = dict() # permite adicionar, remover e verificar se contém item em O(1)
                    # o dict terá como chave uma representação em string do nó < str(node) > e valor uma string vazia (não nos interessa o valor)

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
      if(self.isSolution(curNode)): 
         self.solution = curNode.moveSet
         return
      q = queue.Queue()
      q.put(curNode) #adiciona o nó à fila
      self.visited[str(curNode)] = '' #adiciona o par ( str(curNode): '' ) ao dicionario
      while(not q.empty()):
         if q.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = q.qsize() # atualizar o maximo
         curNode = q.get()
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if(self.isSolution(node)):
               self.solution = node.moveSet
               return
            elif(str(node) not in self.visited):
               self.visited[str(node)] = ''
               q.put(node)

   #pesquisa em profundidade
   def DFS(self):
      curNode = self.estadoInicial
      stack = queue.LifoQueue()
      stack.put(curNode)
      self.visited[str(curNode)] = '' #adiciona o par ( str(curNode): '' ) ao dicionario
      if self.isSolution(curNode):
         self.solution = self.moveSet
         return
      while(not stack.empty()):
         if stack.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = stack.qsize()
         curNode = stack.get()
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if self.isSolution(node):
               self.solution = node.moveSet
               return
            elif str(node) not in self.visited:
               self.visited[str(node)] = ''
               stack.put(node)

   #funcao de pesquisa em profundidade iterativa d -> limite da profundidade
   def iterativaEmProfundidade(self):
      node = self.estadoInicial 
      d = 0
      result = self.idfs(node, d)
      while(not result):
        d += 1
        result = self.idfs(node, d)
      self.maxNumberOfNodesStored = d

   def idfs(self, node, limite):
      if(self.isSolution(node)):
         self.solution = node.moveSet
         return True
      if limite <= 0:
         return False
      newNodes = node.expandeNode()
      for node in newNodes:
         if(self.idfs(node,limite-1)):
            return True
      return False
   

   #heuristicas
   #somatório do número de peças fora do lugar
   def getMisplacedTiles(self, node):
      foraDoSitio = 0
      for i in range(len(node.estado)):
         if node.estado[i] != self.estadoFinal.estado[i] and node.estado[i] != 0:
            foraDoSitio += 1
      return foraDoSitio
   
   #somatório das distâncias de cada peça ao seu lugar na configuração final
   def getManhattanDistance(self, node):
        manhattan = 0
        for i in range(1,16):
            collumnDifference = abs(node.estado.index(i)%4 - self.estadoFinal.estado.index(i)%4) # abs() -> valor absoluto
            rowDifference = abs(node.estado.index(i)//4 - self.estadoFinal.estado.index(i)//4)
            manhattan += collumnDifference + rowDifference
        return manhattan


   # custo estimado para chegar ao estado final
   def h(self, node, heuristica):
      h = self.getMisplacedTiles(node) if heuristica==1 else self.getManhattanDistance(node)
      return h

   def greedy(self, heuristica):
      curNode = self.estadoInicial
      q = queue.PriorityQueue()
      pair = Pair(curNode, self.h(curNode, heuristica))
      q.put(pair) #adiciona o par (nó, custo) à fila; custo = h(curNode) 
      while not q.empty():
         if q.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = q.qsize()
         head = q.get()  # pega o "best", pois no topo da fila fica a com o menor custo
         curNode = head.node # head = (node, cost)
         if(self.isSolution(curNode)):
            self.solution = curNode.moveSet
            return
         self.visited[str(curNode)] = ''
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if str(node) not in self.visited:
               pair = Pair(node, self.h(node, heuristica))
               q.put(pair)


   # função de avaliação -> f(n) = g(n) + h(n)
   def f(self, node, heuristica):
      g = len(node.moveSet) # custo do caminho já percorrido/depth (saida do estado inicial até o estado atual)
      h = self.h(node, heuristica) # custo estimado para atingir a solução
      return g+h

   def A_star(self, heuristica):
      curNode = self.estadoInicial
      q = queue.PriorityQueue()
      pair = Pair(curNode, self.f(curNode, heuristica))
      q.put(pair) #adiciona o par (nó, custo) à fila; custo = f(curNode) 
      while not q.empty():
         if q.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = q.qsize()
         head = q.get()  # pega o "best", pois no topo da fila fica a com o menor custo
         curNode = head.node # head = (node, cost)
         if(self.isSolution(curNode)):
            self.solution = curNode.moveSet
            return
         self.visited[str(curNode)] = ''  # adiciona o par ( str(curNode): '' ) ao dicionario
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if(str(node) not in self.visited):
               pair = Pair(node, self.f(node, heuristica))
               q.put(pair)
