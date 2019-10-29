# estados <lista com os nomes dos estados>
# inicial <nome do estado inicial>
# aceita <lista com os nomes dos estados de aceitação>
# <transições>

# Note que estados, inicial e aceita são palavras reservadas.
# <transições> descreve cada transição do autômato (é uma lista) e tem o formato
# estado1 estado2 0
# siginifcando que a transição leva do estado1 para o estado2 lendo o símbolo 0.
# Um exemplo de arquivo de entrada seria
# estados A, B
# inicial A
# aceita B
# A B 0
# B A 0
# A A 1
# B B 1
# Todos os autômatos que serão testados terão esse formato. Use o símbolo e para denotar o símbolo vazio.

Automato = {}

def Organiza_entrada(strip, entrada, slplit_key):
    entrada = entrada.replace(strip)
    

def entrada():
    estados = False
    inicial = False
    aceita = False

    while True:
        entrada = input()
        if(entrada.startswhith("estados")):
            aux = entrada.replace("estados", "")