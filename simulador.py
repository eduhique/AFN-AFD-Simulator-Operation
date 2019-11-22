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