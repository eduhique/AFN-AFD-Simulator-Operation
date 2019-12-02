# coding: utf-8

def conversao(maquina_1):
    result = {}
    new_estados = geraEstados(maquina_1["estados"])
    inicial = geraIncial(maquina_1, new_estados)
    new_aceitacao = geraAceita(maquina_1["aceita"], new_estados)
    transicoes = geraTransicao(maquina_1["transicao"], new_estados)
    estados_final = organizaEstados(new_estados)
    inicial_final = "".join(inicial)
    lista_aceita_final = organizaEstados(new_aceitacao)
    transicoes_final = organizaTransicoes(transicoes)
    result["estados"] = organizaEstados(new_estados)
    result["inicial"] = "".join(inicial)
    result["aceita"] = organizaEstados(new_aceitacao)
    result["transicao"] = organizaTransicoes(transicoes)
    return result

######### Precisa ser revisto ##########

def organizaEstados(new_estados):
    result = []
    for elemento in new_estados:
        result.append("".join(elemento))
    return result

def organizaTransicoes(transicoes):
    result = []
    for elemento in transicoes:
        result.append(["".join(elemento[0]), "".join(elemento[1]), elemento[2]])
    return result

def geraAceita(list_aceita, new_estados):
    result = []
    for estado in new_estados:
        for e in estado:
            if (e in list_aceita):
                result.append(estado)
                break
    return result

def geraTransicao(list_transicao, new_estados):
    result = []
    alfabeto = []
    casos_epson = []
    for transicao in list_transicao:
        if transicao[2] != "e" and transicao[2] not in alfabeto:
            alfabeto.append(transicao[2])
        if transicao[2] == "e":
            casos_epson.append(transicao)
    alfabeto.sort()
    for estado in new_estados:
        for entrada in alfabeto:
            aux = []
            for elemento in list_transicao:
                if (elemento[0] in estado and (elemento[2] == entrada) and elemento[1] not in aux):
                    aux.append(elemento[1])
                    # Gambiarra para resolver probema no caso entrada7.txt
                    if([elemento[1], elemento[0], "e"] in casos_epson and elemento[0] not in aux):
                        aux.append(elemento[0])
            aux.sort()
            if aux in new_estados:
                result.append([estado,aux,entrada])
            elif len(aux) == 0:
                result.append([estado,["ø"],entrada])
    return result

def geraIncial(maquina_1, lista_estados):
    result = []
    inicial_ant = maquina_1["inicial"]
    result.append(inicial_ant)
    for e in maquina_1["transicao"]:
        if e[0] == inicial_ant and e[2] == "e" and (e[1] not in result):
            result.append(e[1])
        # Verificar com o prof se a volta tambem conta...
        # if e[1] == inicial_ant and e[2] == "e" and (e[0] not in result):
        #     result.append(e[0])
    if result in lista_estados:
        return result
    else:
        # Forçar um erro aqui
        pass


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