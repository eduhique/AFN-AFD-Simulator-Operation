# coding: utf-8

import sys
import getopt
from simulador import simulador
from conversao import conversao
from operacoes import uniao,intersecao, complemento, estrela
from util import saidaAuto, afn_checker

x = 0
z = []
maquina = {}
maquina2 = {}

def usage():
    print('''
    Ferramenta desenvolvida para o Projeto da cadeira de Teoria da Computação
    GEEE

    Para usar nossa ferramenta: main.py ou main.py -h

    -s  --simulador
    -c  --conversao                                                     de AFN para AFD
    -u  --uniao
    -i  --intersecao
    -e  --estrela
    -c  --complemento


    Exemplos:
    $ main.py -s arquivo.txt
    $ main.py -u arquivo1.txt arquivo2.txt
    $ main.py -i arquivo1.txt arquivo2.txt
    $ main.py -c arquivo.txt
    $ main.py -e arquivo.txt
    ''')
    sys.exit()

def retornoErros():
    print ('''Confira a linha de comando, esta faltando argumentos.
Exemplos de execucao:

    $ main.py -s arquivo.txt palavra
    $ main.py -u arquivo1.txt arquivo2.txt
    $ main.py -i arquivo.txt arquivo1.txt arquivo2.txt
    $ main.py -e arquivo.txt
    $ main.py -c arquivo.txt
    $ main.py -co arquivo.txt''')
    return


############### Funções que geram maquinas de estados ####################
# Como são no máximo duas maquinas essa funcões manipula duas variaveis ja instanciadas(eduardo) 
# Serve apenas como refatoração do codigo main() (eduardo)
# Será que essas funções deveriam ser modularizadas? (eduardo)

def geraMaquina1(file):
    arquivo = open(file, 'r')
    list = []
    maquina["transicao"] = list
    while True:
        l = arquivo.readline()
        if l == '':
            break
        elif l.startswith("estados "):
            aux = l.replace("estados ", "")
            split = aux.split(",")
            for i in range(len(split)):
                split[i] = split[i].strip()
            maquina["estados"] = split
        elif l.startswith("inicial "):
            aux = l.replace("inicial ", "")
            maquina["inicial"] = aux.split("\n")[0]
        elif l.startswith("aceita "):
            aux = l.replace("aceita ", "")
            split = aux.split(",")
            for i in range(len(split)):
                split[i] = split[i].strip()
            maquina["aceita"] = split
        else:
            split = (l.split("\n")[0]).split(" ")
            maquina["transicao"].append(split)

def geraMaquina2(file):
    arquivo = open(file, 'r')
    list = []
    maquina2["transicao"] = list
    while True:
        l = arquivo.readline()
        if l == '':
            break
        elif l.startswith("estados "):
            aux = l.replace("estados ", "")
            split = aux.split(",")
            for i in range(len(split)):
                split[i] = split[i].strip()
            maquina2["estados"] = split
        elif l.startswith("inicial "):
            aux = l.replace("inicial ", "")
            maquina2["inicial"] = aux.split("\n")[0]
        elif l.startswith("aceita "):
            aux = l.replace("aceita ", "")
            split = aux.split(",")
            for i in range(len(split)):
                split[i] = split[i].strip()
            maquina2["aceita"] = split
        else:
            split = (l.split("\n")[0]).split(" ")
            maquina2["transicao"].append(split)

####################################################################################

###### A magica acontecendo ######
def main():
    if not len(sys.argv[1:]):
        usage()
    

    ###### Trata a entrada para saber se esta de acordo com a especificação ######
    comandLine = sys.argv[1:]
    if len(comandLine) > 3 or len(comandLine) < 2:
        retornoErros()
 
    ###### Captura o arquivo que sera lido ######
    try:
        file = comandLine[1]
    except:
        return
    ###### Captura a linha de comando e faz a verificao para agir com tal   ######
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:c:u:i:e:l", [
                                   "simulador=", "conversao=", "uniao=", "intersecao=", "estrela=", "complemento="])
    except getopt.GetoptError as err:
        retornoErros()

    for o, a in opts:
        if o in ("-s", "--simulador"):
            geraMaquina1(file)
            try:
                palavra = comandLine[2]
            except:
                retornoErros()
                return
            print("Todos os caminhos tentados:\n\nEstado       Palavra")
            result_simula = simulador(maquina["inicial"], maquina["transicao"], palavra, maquina["aceita"])
            if (result_simula.split("\n")[-1] == "palavra aceita"):
                    print("\n\nCaminho até um estado aceito:\nEstado       Palavra")
                    print(result_simula)
            else:
                    print(result_simula)
        elif o in ("-c", "--conversao"):
            geraMaquina1(file)
            check = afn_checker(maquina["transicao"],maquina["estados"])
            print ("É uma AFN? " + str(check))
            if (check):
                new_maquina = conversao(maquina)
                print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["aceita"], new_maquina["transicao"]))
            else:
                print("\nO automato '" + file + "' já é uma AFD, portanto, não precisa de conversão :D.\n")
        elif o in ("-u", "--uniao"):
            geraMaquina1(file)
            file2 = comandLine[2]
            geraMaquina2(file2)
            new_maquina = uniao(maquina, maquina2)
            print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["aceita"], new_maquina["transicao"]))
        elif o in ("-i", "--intersecao"):
            geraMaquina1(file)
            file2 = comandLine[2]
            geraMaquina2(file2)
            new_maquina = intersecao(maquina, maquina2)
            print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["aceita"], new_maquina["transicao"]))
        elif o in ("-e", "--estrela"):
            geraMaquina1(file)
            new_maquina = estrela(maquina)
            print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["aceita"], new_maquina["transicao"]))
        elif o in ("-l", "--complemento"):
            geraMaquina1(file)
            check = afn_checker(maquina["transicao"],maquina["estados"])
            print ("É uma AFN? " + str(check))
            if (check):
                print("\nSerá feita a conversão antes de aplicar o Complemento")
                maquina_convert = conversao(maquina)
                new_maquina = complemento(maquina_convert)
                print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["aceita"], new_maquina["transicao"]))
            else:
                print("\nComo o automato '" + file + "' já é uma AFD, Será realizado o complemento diretamente sem conversão.add()\n")
                new_maquina = complemento(maquina)
                print(saidaAuto(new_maquina["estados"], new_maquina["inicial"], new_maquina["aceita"], new_maquina["transicao"]))
        else:
            assert False,"Unhandled Option"
main()