from util import saidaAuto, afn_checker

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
