import time # importando módulo time
import node # node.py
import search # search.py


def printMoves(solucao):
    moves = 'Moves: '
    print('\nU: UP, D: DOWN, R: RIGHT, L: LEFT')
    for move in solucao:
        moves+= '-> '+str(move)
    print(moves+'\n')

def printInfo(numeroDePassos, elapsedTime, maxNumberOfNodesStored):
    print(f'Number of moves/Depth: {numeroDePassos}\n')
    print(f'Time: {elapsedTime} seconds\n');
    print(f'Used memory: {maxNumberOfNodesStored}');

# -------------------------------------------------------------------

configInicial = list(map(int,input().split()))
configFinal = list(map(int,input().split()))

#transforma a lista num nó
estadoInicial = node.Node(configInicial, None)
estadoFinal = node.Node(configFinal, None)

jogo = search.Search(estadoInicial, estadoFinal)

print('Configuracao inicial:')
print(estadoInicial)
print()
print('Configuracao final:')
print(estadoFinal)
print()

if jogo.solvability:
    print("Insira o tipo de estratégias de busca:")
    print("1 - Pesquisa em Largura")
    print("2 - Pesquisa Iterativa em profundidade")
    print("3 - Gulosa")
    print("4 - A*")
    print("5 - Pesquisa em Profundidade")
    tipo = int(input("Tipo de pesquisa: "))

    if tipo == 1:
        jogo = search.Search(estadoInicial, estadoFinal)
        start = time.time_ns()
        jogo.BFS() # inicia a pesquisa
        end = time.time_ns()
        elapsedTime = (end - start)/1000000000 # tempo decorrido em segundos  
        solucao = jogo.solution # obter a string com os movimentos que levaram ao estado final      
        numeroDePassos = len(solucao) # n° de passos/movimentos até o estado final
        printMoves(solucao)
        printInfo(numeroDePassos, elapsedTime, jogo.getMaxNumberOfNodesStored())
    elif tipo == 2:
        jogo = search.Search(estadoInicial, estadoFinal)
        start = time.time_ns()
        jogo.iterativaEmProfundidade() # inicia a pesquisa
        end = time.time_ns()
        elapsedTime = (end - start)/1000000000 # tempo decorrido em segundos  
        solucao = jogo.solution # obter a string com os movimentos que levaram ao estado final
        numeroDePassos = len(solucao) # n° de passos/movimentos até o estado final
        printMoves(solucao)
        printInfo(numeroDePassos, elapsedTime, jogo.getMaxNumberOfNodesStored())
    elif tipo == 3:
        jogo = search.Search(estadoInicial, estadoFinal)
        heuristica = int(input("Insira o tipo de heuristica: "))
        start = time.time_ns()
        jogo.greedy(heuristica) # inicia a pesquisa
        end = time.time_ns()
        elapsedTime = (end - start)/1000000000 # tempo decorrido em segundos  
        solucao = jogo.solution # obter a string com os movimentos que levaram ao estado final
        numeroDePassos = len(solucao) # n° de passos/movimentos até o estado final
        printMoves(solucao)
        printInfo(numeroDePassos, elapsedTime, '?')
    elif tipo == 4:
        jogo = search.Search(estadoInicial, estadoFinal)
        heuristica = int(input("Insira o tipo de heuristica: "))
        start = time.time_ns()
        jogo.A_star(heuristica) # inicia a pesquisa
        end = time.time_ns()
        elapsedTime = (end - start)/1000000000 # tempo decorrido em segundos  
        solucao = jogo.solution # obter a string com os movimentos que levaram ao estado final
        numeroDePassos = len(solucao) # n° de passos/movimentos até o estado final
        printMoves(solucao)
        printInfo(numeroDePassos, elapsedTime, jogo.getMaxNumberOfNodesStored())
    elif tipo == 5:
        jogo = search.Search(estadoInicial, estadoFinal)
        start = time.time_ns()
        jogo.dfs()
        end.time_ns()
        elapsedTime = (end-start)/1000000000
        solucao = jogo.solution
        numeroDePacos = len(solucao)
        printmoves(solucao)
        printInfo(numeroDePassos, elapsedTime, jogo.getMaxNumverOfNodesStored())

else:
    print("Nao ha solucao!")
