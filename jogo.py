import time # importando módulo time
import node # node.py
import search # search.py


def printMoves(solucao):
    moves = 'Moves: '
    for move in solucao:
        moves+= '-> '+str(move)
    print(moves+'\n')


def printInfo(numeroDePassos, elapsedTime, visitedStates ,maxNumberOfNodesStored):
    print(f'Number of moves/Depth: {numeroDePassos}\n')
    print(f'Time: {elapsedTime} seconds\n');
    print(f'Visited states: {visitedStates}\n')
    print(f'Used memory: {maxNumberOfNodesStored}');


def showMenu():
    menu = { 1 : "- Pesquisa em Largura",
             2 : "- Pesquisa Iterativa em profundidade",
             3 : "- Gulosa",
             4 : "- A*",
             5 : "- Pesquisa em Profundidade" }
    print("Insira o tipo de estratégia de busca:")             
    
    for  entry in menu:
        print(entry, menu[entry])
    
    tipo = int(input("Tipo de pesquisa: "))
    return tipo


# -------------------------------------------------------------------
# ler as configurações inicial e final
configInicial = list(map(int,input().split()))
configFinal = list(map(int,input().split()))

#transforma a lista num nó
estadoInicial = node.Node(configInicial, None)
estadoFinal = node.Node(configFinal, None)

jogo = search.Search(estadoInicial, estadoFinal)

print('Configuracao inicial:')
print(str(estadoInicial) + '\n')
print('Configuracao final:')
print(str(estadoFinal) + '\n')

if jogo.solvability:
    tipo = showMenu()
    if tipo == 1:
        start = time.time_ns()
        jogo.BFS() # inicia a pesquisa
        end = time.time_ns()
    elif tipo == 2:
        start = time.time_ns()
        jogo.iterativaEmProfundidade() # inicia a pesquisa
        end = time.time_ns()
    elif tipo == 3:
        # número 1 -> misplaced tiles | número 2 -> manhattan distance
        heuristica = int(input("Insira o tipo de heuristica: "))
        start = time.time_ns()
        jogo.greedy(heuristica) # inicia a pesquisa
        end = time.time_ns()
    elif tipo == 4:
        # número 1 -> misplaced tiles | número 2 -> manhattan distance
        heuristica = int(input("Insira o tipo de heuristica: "))        
        start = time.time_ns()
        jogo.A_star(heuristica) # inicia a pesquisa
        end = time.time_ns()
    elif tipo == 5:
        start = time.time_ns()
        jogo.DFS() # inicia a pesquisa
        end = time.time_ns()

    elapsedTime = (end -start)/1000000000 # tempo decorrido em segundos  
    solucao = jogo.solution # obter a string com os movimentos que levaram ao estado final      
    numeroDePassos = len(solucao) # n° de passos/movimentos até o estado final
    printMoves(solucao)
    printInfo(numeroDePassos, elapsedTime, len(jogo.visited), jogo.getMaxNumberOfNodesStored())

else:
    print("Nao ha solucao!")