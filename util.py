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