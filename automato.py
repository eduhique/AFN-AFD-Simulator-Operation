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
    -c  --complemento


    Exemplos:
    $ geee.py -s arquivo.txt
    $ geee.py -u arquivo1.txt arquivo2.txt
    $ geee.py -i arquivo1.txt arquivo2.txt
    $ geee.py -c arquivo.txt
    $ geee.py -e arquivo.txt
    ''')
    sys.exit()


############################# Funcoes a serem implementadas ########################

# função testada com algumas palavras usando os arquivos entrada1.txt, entrada2.txt, entrada4.txt e entrada.txt (eduardo) 
def simulador(estado_atual, lista_de_transicoes, palavra, estado_de_aceitacao):
    if((estado_atual in estado_de_aceitacao) and ((len(palavra) == 0) or (len(palavra)== 1) and (palavra == "e"))):
        print(estado_atual + "            e")
        return "\npalavra aceita"
    elif(len(palavra) > 0):
        result = "\npalavra não aceita"
        # achou = False
        for elemento in lista_de_transicoes:
            if (elemento[0] == estado_atual and (elemento[2] == palavra[0] or elemento[2] == "e")):
                # achou = True
                print(estado_atual + "            " + palavra)
                aux = ""
                if (elemento[2] == "e"):
                    aux = simulador(elemento[1], lista_de_transicoes, palavra, estado_de_aceitacao)
                else:
                    if(len(palavra) <= 1):
                        aux = simulador(elemento[1], lista_de_transicoes, "", estado_de_aceitacao)
                    else:
                        aux = simulador(elemento[1], lista_de_transicoes, palavra[1:], estado_de_aceitacao)
                if (aux == "\npalavra aceita"):
                    result = aux
                    break
        # if(achou == False):
        #     print(estado_atual + "            " + palavra)
        #     # Tem que perguntar o prof o que fazer quando recebe uma palavra que não possui um determinada transição(eduardo) 
        #     # return simulador(estado_atual, lista_de_transicoes, palavra[1:], estado_de_aceitacao)
        return result
    elif(len(palavra) == 0):
        return "\npalavra não aceita"

def conversao(maquina_1):
    new_estados = geraEstados(maquina_1["estados"])
    print(new_estados)
    print (len(new_estados))

######### Precisa ser revisto ##########
def geraEstados(lista_estados):
    result = [x for x in powerset(lista_estados)]
    result.sort(reverse=True, key=myLen)
    result.reverse()
    for e in result:
        if len(e) == 0:
            e.append("ø")
            break
    return result

def powerset(list):
    if len(list) <= 1:
        yield list
        yield []
    else:
        for item in powerset(list[1:]):
            yield [list[0]]+item
            yield item

def myLen(e):
    return len(e)

# função testada usando os arquivos entrada1.txt e entrada2.txt (eduardo) 
def uniao(maquina_1, maquina_2):
    lista_estados = ["N"]
    inicial = "N"
    lista_aceita = [] 
    lista_transicao = []

    for elemento in maquina_1["estados"]:
        lista_estados.append((elemento + "1"))
    for elemento in maquina_2["estados"]:
        lista_estados.append((elemento + "2"))
    for elemento in maquina_1["aceita"]:
        lista_aceita.append((elemento + "1"))
    for elemento in maquina_2["aceita"]:
        lista_aceita.append((elemento + "2"))
    lista_transicao.append(["N", maquina_1["inicial"] + "1", "e"])
    lista_transicao.append(["N", maquina_2["inicial"]+ "2", "e"])
    for elemento in maquina_1["transicao"]:
        lista_transicao.append([(elemento[0] + "1"), (elemento[1] + "1"), (elemento[2])])
    for elemento in maquina_2["transicao"]:
        lista_transicao.append([(elemento[0] + "2"), (elemento[1] + "2"), (elemento[2])])
    saidaAuto(lista_estados, inicial, lista_aceita, lista_transicao)


# Função testada usando os arquivos entrada1.txt e entrada2.txt. Resultado armazenado no arquivo intersecao-entrada1-e-entrada2.txt (#Euclides)
def intersecao(maquina_1, maquina_2):
    lista_estados = []
    inicial = maquina_1["inicial"] + "1" + maquina_2["inicial"] + "2"
    lista_aceita = [] 
    lista_transicao = []

    for elemento1 in maquina_1["estados"]:
        for elemento2 in maquina_2["estados"]:
            lista_estados.append(elemento1 + "1" + elemento2 + "2")
    
    for elemento1 in maquina_1["aceita"]:
        for elemento2 in maquina_2["aceita"]:
            lista_aceita.append(elemento1 + "1" + elemento2 + "2")

    for elemento1 in maquina_1["transicao"]:
        for elemento2 in maquina_2["transicao"]:
            if (elemento1[2] == elemento2[2]):
                lista_transicao.append([(elemento1[0] + "1" + elemento2[0] + "2"), (elemento1[1] + "1" + elemento2[1] + "2"), elemento1[2]])
    
    saidaAuto(lista_estados, inicial, lista_aceita, lista_transicao)


def estrela(maquina_1):
    lista_estados = ["N"]
    inicial = "N"
    lista_transicao = maquina_1["transicao"]
    for elemento in maquina_1["estados"]:
        lista_estados.append((elemento))
    lista_transicao.append(["N", maquina_1["inicial"], "e"])
    for elemento in maquina_1["aceita"]:
        lista_transicao.append([elemento, "N",  "e"])
    saidaAuto(lista_estados, inicial, maquina_1["aceita"], lista_transicao)

# Tem que verificar um detalhe com o professor (eduardo) 
# De acordo com o prof, está solução só funciona para AFD, portanto, para AFN deve-se converter e depois operar sobre
def complemento(maquina_1):
    lista_aceita = []
    for elemento in maquina_1["estados"]:
        if (elemento not in maquina_1["aceita"]):
            lista_aceita.append(elemento)
    saidaAuto(maquina_1["estados"], maquina_1["inicial"], lista_aceita, maquina_1["transicao"])

def saidaAuto(lista_estados, inicial, lista_aceita, lista_transicao):
    estados = "estados "
    inicial_saida = "inicial " + inicial
    aceita = "aceita "
    for elemento in lista_estados:
        estados += (elemento + ",")
    print("\nAutomato: \n")
    print (estados[:-1] + "\n" + inicial_saida)
    for elemento in lista_aceita:
        aceita += (elemento + ",")
    print (aceita[:-1])
    for elemento in lista_transicao:
        print (elemento[0] + " " + elemento[1] + " " + elemento[2])

def afn_checker(lista_transicao, lista_estados):
    count = 0
    for elemento in lista_transicao:
        if "e" == elemento[2]:
            return True
    for estado in lista_estados:
        for elemento in lista_transicao:
            if estado == elemento[0] and elemento[2] != "e":
                count += 1
        if count < 2 or count > 2:
            return True
        else:
            count = 0  
    return False

############### Funções que geram maquinas de estados ####################
# Como são no máximo duas maquinas essa funcões manipula duas variaveis ja instanciadas(eduardo) 
# Serve apenas como refatoração do codigo main() (eduardo)

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
#print len(sys.argv[1:])
#print "X = %d, sofreu alteracao?(antes do paramentro)" % x

###### A magica acontecendo ######
def main():
    if not len(sys.argv[1:]):
        usage()
    

    ###### Trata a entrada para saber se esta de acordo com a especificação ######
    comandLine = sys.argv[1:]
    if len(comandLine) > 3 or len(comandLine) < 2:
        print ('''Confira a linha de comando, esta faltando argumentos.
Exemplos de execucao:

    $ automato.py -s arquivo.txt palavra
    $ automato.py -u arquivo1.txt arquivo2.txt
    $ automato.py -i arquivo.txt arquivo1.txt arquivo2.txt
    $ automato.py -e arquivo.txt
    $ automato.py -c arquivo.txt
    $ automato.py -co arquivo.txt''')
        return
    
    ###### Captura o arquivo que sera lido ######
    file = comandLine[1]
    
    ###### Captura a linha de comando e faz a verificao para agir com tal   ######
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:c:u:i:e:l", [
                                   "simulador=", "conversao=", "uniao=", "intersecao=", "estrela=", "complemento="])
    except getopt.GetoptError as err:
        print (str(err))

    for o, a in opts:
        if o in ("-s", "--simulador"):
            geraMaquina1(file)
            palavra = comandLine[2]
            print("Estado       Palavra")
            print (simulador(maquina["inicial"], maquina["transicao"], palavra, maquina["aceita"]))
        elif o in ("-c", "--conversao"):
            geraMaquina1(file)
            check = afn_checker(maquina["transicao"],maquina["estados"])
            print ("É uma AFN? " + str(check))
            if (check):
                conversao(maquina)
            else:
                print("\nO automato '" + file + "' já é uma AFD, portanto, não precisa de conversão :D.\n")
        elif o in ("-u", "--uniao"):
            geraMaquina1(file)
            file2 = comandLine[2]
            geraMaquina2(file2)
            uniao(maquina, maquina2)
        elif o in ("-i", "--intersecao"):
            geraMaquina1(file)
            file2 = comandLine[2]
            geraMaquina2(file2)
            intersecao(maquina, maquina2)
        elif o in ("-e", "--estrela"):
            geraMaquina1(file)
            estrela(maquina)
        elif o in ("-l", "--complemento"):
            geraMaquina1(file)
            #gerar AFD antes se for AFN
            complemento(maquina)
        else:
            assert False,"Unhandled Option"

    # print ("File = " + file)
    # print (maquina)
    # saidaAuto(maquina["estados"], maquina["inicial"], maquina["aceita"], maquina["transicao"])
    # saidaAuto(maquina2["estados"], maquina2["inicial"], maquina2["aceita"], maquina2["transicao"])

main()