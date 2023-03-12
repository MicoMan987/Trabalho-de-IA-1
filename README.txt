# Sumário

Programa desenvolvido por João Vivas, Gelson Varela e Tomás Martins

Este programa foi desenvolvido usando a linguagem python (versão: Python 3, mais especificamente Python 3.11.1) 
Caso haja erros/problemas durante a execução, instale a versão igual à citada acima
	
# Execução

Para executar o programa seque os seguintes passos:

- Coloque os três ficheiros node.py, search.py e jogo.py num mesmo diretório
- Abra o terminal nesse diretório e execute `python3 jogo.py`
- Após isso o cursor estará à espera das configurações, insira as configurações inicial e final cada um numa linha. 

Exemplo:
1 2 3 4 5 6 8 12 13 9 0 7 14 11 10 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0

- Se as houver solução para as configurações inseridas, de seguida aparecerá um menu de opções com o tipo de busca, na qual deve inserir um número correspondente

```
Insira o tipo de estratégia de busca:
1 - Pesquisa em Largura
2 - Pesquisa Iterativa em profundidade
3 - Gulosa
4 - A*
5 - Pesquisa em Profundidade
Tipo de pesquisa:
```

- Se a estratégia escolhida for uma estratégia informada: 3 - Gulosa ou 4 - A*, aparecerá um campo adicional:
```
Insira o tipo de heuristica:
```
Onde deve inserir o número **1** para usar a heurística misplaced tiles ou o número **2** para usar manhattan distance

- Após apertar a tecla Enter, o programa começa a procurar a solução e imprime a resultado obtido no terminal

# Inserir o input apartir de um ficheiro '.txt'

- Para isso crie um ficheiro .txt e insira as configurações inicial e final um em cada linha e na linha seguinte o tipo de busca.
Exemplo:
1 3 4 8 6 2 7 0 5 10 11 12 9 13 14 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0
2

- Para as informadas deve indicar o tipo de heurística
Exemplo:
1 3 4 8 6 2 7 0 5 10 11 12 9 13 14 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0
4
1