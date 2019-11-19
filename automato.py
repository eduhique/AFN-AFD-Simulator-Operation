# coding: utf-8

# Onde estamos -> A CLI esta quase 100%, a unica coisa que falta eh retornar um erro quando o argumento eh invalido (#WeS)
#              -> Refatorar o codigo que tinha sido feito anteriormente para o modelo abaixo (Acho que fica mais bonito #WeS)
#
import sys
import getopt

x = 0
z = []
maquina = {}
maquina2 = {}

def usage():
    print('''
    Ferramenta desenvolvida para o Projeto da cadeira de Teoria da Computação
    GEEE

    Para usar nossa ferramenta: geee.py ou geee.py -h

    -s  --simulador
    -c  --conversao                                                     de AFN para AFD
    -u  --uniao
    -i  --intersecao
    -e  --estrela
    -c -- complemento


    Exemplos:
    $ geee.py -s arquivo.txt
    $ geee.py -u arquivo.txt
    $ geee.py -i arquivo.txt
    $ geee.py -co arquivo.txt
    ''')
    sys.exit()


############################# Funcoes a serem implementadas ########################
def simulador():
    pass


def conversao():
    pass


def uniao():
    pass


def intersecao():
    pass


def estrela():
    pass


def complemento():
    pass

####################################################################################
#print len(sys.argv[1:])
#print "X = %d, sofreu alteracao?(antes do paramentro)" % x

###### A magica acontecendo ######
def main():
    if not len(sys.argv[1:]):
        usage()
    

    ###### Trata a entrada para saber se esta de acordo com a especificação ######
    comandLine = sys.argv[1:]
    if len(comandLine) > 2 or len(comandLine) < 2:
        print ('''Confira a linha de comando, esta faltando argumentos.
Exemplos de execucao:

    $ geee.py -s arquivo.txt
    $ geee.py -u arquivo.txt
    $ geee.py -i arquivo.txt
    $ geee.py -co arquivo.txt''')
        return
    
    ###### Captura o arquivo que sera lido ######
    file = comandLine[1]
    
    ###### Captura a linha de comando e faz a verificao para agir com tal   ######
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:c:u:i:e:c", [
                                   "simulador=", "conversao=", "uniao=", "intersecao=", "estrela=", "complemento="])
    except getopt.GetoptError as err:
        print (str(err))

    arquivo = open(file, 'r')
    for o, a in opts:
        if o in ("-s", "--simulador"):
            while True:
                a = arquivo.readline()
                if a == '':
                    break
                if a.startswith("estados "):
                    aux = a.replace("estados ", "")
                    split = aux.split(",")
                    for i in range(len(split)):
                        split[i] = split[i].strip()
                    maquina["estados"] = split
                if a.startswith("inicial "):
                    aux = a.replace("inicial ", "")
                    maquina["inicial"] = aux.split("\n")[0]
                    if a.startswith("aceita "):
                        aux = a.replace("aceita ", "")
                        split = aux.split(",")
                        for i in range(len(split)):
                            split[i] = split[i].strip()
                        maquina["aceita"] = split
        elif o in ("-c", "--conversao"):
            x = 4
        elif o in ("-u", "--uniao"):
            pass
        elif o in ("-i", "--intersecao"):
            pass
        elif o in ("-e", "--estrela"):
            pass
        elif o in ("-c", "--complemento"):
            pass
        else:
            assert False,"Unhandled Option"

    print ("File = " + file)
    print (maquina)

main()
