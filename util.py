# coding: utf-8

def saidaAuto(lista_estados, inicial, lista_aceita, lista_transicao):
    result = "\nAutomato: \n\nestados "
    inicial_saida = "inicial " + inicial
    aceita = "aceita "
    for elemento in lista_estados:
        result += (elemento + ",")
    result = result[:-1]
    result += "\n" + inicial_saida
    for elemento in lista_aceita:
        aceita += (elemento + ",")
    result += "\n" +  aceita[:-1]
    for elemento in lista_transicao:
        result += "\n" +  elemento[0] + " " + elemento[1] + " " + elemento[2]
    return result

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