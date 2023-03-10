import node # node.py
import queue
import pdb

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
         curNode = q.get()
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if(self.isSolution(node)):
               self.solution = node.moveSet
               return
            if(str(node) not in self.visited):
               self.visited[str(node)] = ''
               q.put(node)
            if q.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = q.qsize()


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
            collumnDifference = abs(node.estado.index(i)%4 - self.estadoFinal.estado.index(i)%4) # abs() -> valor absoluto
            rowDifference = abs(node.estado.index(i)//4 - self.estadoFinal.estado.index(i)//4)
            manhattan += collumnDifference + rowDifference
        return manhattan

   def greedy(self, heuristica):
      node = self.estadoInicial
      while self.solution == '':
         if(self.isSolution(node)):
            self.solution = node.moveSet
            return
         self.visited[str(node)] = ''
         criancas = node.expandeNode()
         if heuristica == 1:
            minimo = 16 # max misplaced tiles+1
            for crianca in criancas:  # vai percorrer a lista e pegar o melhor
               if str(crianca) not in self.visited and self.misplaced(crianca) < minimo: 
                     minimo = self.misplaced(crianca)
                     node = crianca # proximo nó a ser expandido
         elif heuristica == 2:
            minimo = 15*6  #soma das distancias maxima de manhattan possivel
            for crianca in criancas:
               if str(crianca) not in self.visited and self.getManhattanDistance(crianca) < minimo:
                     minimo = self.getManhattanDistance(crianca)
                     node = crianca # proximo nó a ser expandido

   # função de avaliação -> f(n) = g(n) + h(n)
   def f(self, node, heuristica):
      g = len(node.moveSet) # custo do caminho já percorrido (saida do estado inicial até o estado atual)
      h = self.misplaced(node) if heuristica==1 else self.getManhattanDistance(node) # custo estimado para chegar ao estado final
      return g+h

   def A_star(self, heuristica):
      curNode = self.estadoInicial
      q = queue.PriorityQueue()
      pair = Pair(curNode, self.f(curNode, heuristica))
      q.put(pair) #adiciona o par (nó, custo) à fila; custo = f(curNode) 
      self.visited[str(curNode)] = ''
      while(not q.empty()):
         head = q.get()  # pega o "best", pois no topo da fila fica a com o menor custo
         curNode = head.node # head = (node, cost)
         if(self.isSolution(curNode)):
            self.solution = curNode.moveSet
            return
         newNodes = curNode.expandeNode()
         for node in newNodes:
            if(str(node) not in self.visited):
               self.visited[str(node)] = ''  # adiciona o par ( str(node): '' ) ao dicionario
               pair = Pair(node, self.f(node, heuristica))
               q.put(pair)
            if q.qsize() > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = q.qsize()

   def dfs(self):
      pdb.set_trace()
      curNode = self.estadoInicial
      stack = []
      stack.append(curNode)
      self.visited[str(curNode)] = '' #adiciona o par ( str(curNode): '' ) ao dicionario
      if self.isSolution(curNode):
         self.solution = self.moveSet
         return
      while(not stack == []):
         curNode=stack.pop()
         criancas = curNode.expandeNode()
         for crianca in criancas:
            if self.isSolution(crianca):
               self.solution = crianca.moveSet
               return
            elif str(crianca) not in self.visited:
               self.visited[str(crianca)] = ''
               stack.append(crianca)
            if len(stack) > self.maxNumberOfNodesStored: self.maxNumberOfNodesStored = len(stack)

class Pair:
   def __init__(self, node, cost):
      self.node = node
      self.cost = cost

   def __lt__(self, other):
      return self.cost < other.cost

