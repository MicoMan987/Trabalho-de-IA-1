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
    print("Insira o tipo de pesquisa que quer:")
    print("1 - Pesquisa em Largura (pouco eficiente)")
    print("2 - Pesquisa em Profundidade (mais eficiente)")
    tipo = int(input("Tipo de pesquisa: "))

    if tipo == 1:
        jogo = search.Search(estadoInicial, estadoFinal)
        start = time.time_ns()
        jogo.BFS() # retorna uma string com os movimentos que levaram ao estado final
        end = time.time_ns()
        elapsedTime = (end - start)/1000000000 # tempo decorrido em segundos  
        solucao = jogo.solution
        if jogo.solvability == False:
            print('\n'+solucao)
        else:
            numeroDePassos = len(solucao) # n° de passos/movimentos até o estado final
            printMoves(solucao)
            printInfo(numeroDePassos, elapsedTime, jogo.getMaxNumberOfNodesStored())
    elif tipo == 2:
        jogo = search.Search(estadoInicial, estadoFinal)
        start = time.time_ns()
        jogo.pesquisaLarguraIterativa() # retorna uma string com os movimentos que levaram ao estado final
        end = time.time_ns()
        elapsedTime = (end - start)/1000000000 # tempo decorrido em segundos
        solucao = jogo.solution
        if jogo.solvability == False: 
            print('\n'+solucao)
        else:
            numeroDePassos = len(solucao) # n° de passos/movimentos até o estado final
            printMoves(solucao)
            printInfo(numeroDePassos, elapsedTime, jogo.getMaxNumberOfNodesStored())
    
    elif tipo == 3:
        jogo = search.Search(estadoInicial, estadoFinal)
        start = time.time_ns()
        print("Numero de pecas fora do sito: ", jogo.misplaced(jogo.estadoInicial))
        print("Manhattan distance total: ", jogo.getManhattanDistance(jogo.estadoInicial))

else:
    print("Nao ha solucao!")