def conversao(maquina_1):
    new_estados = geraEstados(maquina_1["estados"])
    inicial = geraIncial(maquina_1, new_estados)
    print (new_estados)
    print (inicial)
    

######### Precisa ser revisto ##########
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
    # for e in aux:
    #     result.append("".join(e))
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