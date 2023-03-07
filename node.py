class Node:
    def __init__(self, estado, parent):
        self.estado = estado # estado do jogo
        self.parent = parent # pai do nó
        self.move = ''       # movimento pode ser 'U' ou 'D' ou 'L' ou 'R'
        self.moveSet = ''   # lista com os movimentos que levaram o jogo do estado inicial a este atual estado
        self.blankPos = estado.index(0)

    # aqui expandimos para as várias jogadas
    def expandeNode(self):
        novosNos = [] # este é um array que vai guardar todos os nós que são filhos do nó expandido
        blankPos = self.blankPos
        #troca movimentacao da peca vazia
        if(blankPos%4 > 0): #a peça vazia pode mover para a esquerda
            novoNo = self.moveBlankPosTo('L', blankPos-1)
            novosNos.append(novoNo)
        if(blankPos%4 < 3): #a peça vazia pode mover para a direita
            novoNo = self.moveBlankPosTo('R', blankPos+1)
            novosNos.append(novoNo)
        if(blankPos > 3):   #a peça vazia pode mover para cima
            novoNo = self.moveBlankPosTo('U', blankPos-4)
            novosNos.append(novoNo)
        if(blankPos < 12):  #a peça vazia pode mover para baixo
            novoNo = self.moveBlankPosTo('D', blankPos+4)
            novosNos.append(novoNo)
        return novosNos

    # retorna um novo nó na qual blankPos foi movida para uma das quatro posições 
    def moveBlankPosTo(self, move, position):
        estadoNovo = self.estado[:]
        temp = estadoNovo[position]
        estadoNovo[position] = estadoNovo[self.blankPos]
        estadoNovo[self.blankPos] = temp
        novoNo = Node(estadoNovo, self)
        novoNo.move = move
        novoNo.moveSet = self.moveSet+move
        return novoNo

    # apenas imprime o estado do nó
    def __str__(self):
        lista = self.estado
        tmp = ''
        for num in lista:
            tmp+= f'  {num}' if (num//10 == 1) else f'   {num}'
            if (lista.index(num)!=len(lista)-1 and lista.index(num)%4==3): tmp+='\n'
        return tmp