# Projeto TC 2019.2

Este projeto é parte da nota da disciplina de Teoria da Computação(TC) de 2019.2

## Problema

### Resumo

O projeto consistirá da implementação de um simulador para autômatos finitos e dos principais algoritmos existente sobre autômatos. O projeto deverá ser feito para ser usado através da linha de comando, e poderá ser desenvolvido em Java ou em Python.

### Formato do arquivo de entrada

O o arquivo de entrada contendo a descrição do autômato deverá obedecer ao seguinte formato:

```{text}
estados <lista com os nomes dos estados>
inicial <nome do estado inicial>
aceita <lista com os nomes dos estados de aceitação>
<transições>
````

Note que estados, inicial e aceita são palavras reservadas.

`<transições>` descreve cada transição do autômato (é uma lista) e tem o formato:

```{text}
estado1 estado2 0
````

siginifcando que a transição leva do estado1 para o estado2 lendo o símbolo 0.
Um exemplo de arquivo de entrada seria:

```{text}
estados A, B
inicial A
aceita B
A B 0
B A 0
A A 1
B B 1
```

Todos os autômatos que serão testados terão esse formato. Use o símbolo e para denotar o símbolo vazio.

`Importante`: o autômato será fornecido como um arquivo. Eu não vou ficar digitando na entrada. Seu programa precisa ler esse arquivo com a descrição do autômato.

`Importante`: toda a execução de seu programa deverá ser feita via CLI. Tanto do simulador quando da computação das operações.

## Simulador (obrigatório)

O simulador deverá receber na entrada o nome de um arquivo contendo a descrição do autômato e a entrada que será processada pelo autômato. Por exemplo:

```{text}
$nome_do_executável arquivo_do_automato 101
```

Imprima um traço na tela mostrando em qual estado o autômato se encontra e o que falta ler. Ao final diga se a palavra foi aceita ou não. Por exemplo, para o autômato acima a saída poderia ser:

```{text}
Estado           Palavra
A                101
A                01
B                1
B                e
A palavra foi aceita
````

### Operações

A seguinte operação é obrigatória:

1. Transformar de não-determinístico para determinístico: receba um autômato na entrada e mostre na saída padrão a versão determinística dele.

<p>Além da operação acima, cada grupo deverá escolher pelo menos duas das operações a seguir para serem implementadas.</p>

1. União: receba dois autômatos e gere um terceiro que é a união dos outros dois e mostre na saída padrão.
2. Intersecção: receba dois autômatos e gere um terceiro que é a intersecção dos outros dois e mostre na saída padrão.
3. Complemento: receba um autômato e gere um segundo que é o complemento do outro e mostre na saída padrão.
4. Estrela: receba um autômato e gere um segundo que é o resultado da operação estrela do outro e mostre na saída padrão.

Cada operação adicional valerá pontuação extra.

### Opcional

<p>Minimização de autômatos. Existe um algoritmo para minimizar um autômato reduzindo o número de estados ao mínimo. Esse algoritmo não foi discutido em sala de aula. A implementação desse algoritmo vale pontuação adicional, inclusive podendo transferir para as provas se o projeto tiver atingido a nota máxima.</p>

## Solução

*`Importante`: Muito provavelmente, essas sugestões de solução possem alguns erros ou preceisam ser adptadas para funcionar em uma situação real.*

Nesta seção será discutida a resolução do problema

### Pseudo Código da Função de transição do Simulador

Abaixo segue a ideia de uma função de transição de estado:

```{text}
function transicao(estado_atual, lista_de_transicoes, palavra, estado_de_aceitacao):
    result = "Palavra não aceita"
    if(estado_atual in estado_de_aceitacao and palavra.isvazia()):
        result = "palavra aceita"
    else:
        for elemento in lista_de_transicoes:
            if (elemento[0] == estado_atual and elemento[2] == palavra[0]):
                estado_atual = elemento[1]
                result = transicao(estado_atual, lista_de_transicoes, palavra[1:])
                if (result == "palavra aceita")
                    break
    return result
```

#### Pseudo Código da Função de gerar saida de automato

Código auxiliar para geração de automatos na saida do programa no modelo definido na especificação.

```{text}
function saidaAuto(lista_estados, inicial, lista_aceita, lista_transicao):
    estados = "estados "
    inicial_saida = "inicial " + inicial
    aceita = "aceita "
    for elemento in lista_estados:
        estados += (elemento + ", ")
    print (estados[:-1] + "\n" + inicial_saida + "\n")
    for elemento in lista_aceita:
        estados += (elemento + ", ")
    print (aceita[:-1] + "\n")
    for elemento in lista_transicao:
        print (elemento[1] + " " + elemento[2] + " " + elemento[3] + "\n")
```

### Operações

#### Pseudo Código da Função de Coneversão

```{text}
Ainda falta fazer
```

#### Pseudo Código da Função de União

Para efeitos praticos chamarei o novo estado inicial de estado `N`.segue Abaixo ideia de codigo de união:

```{text}
function uniao(maquina_1, maquina_2):
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
    lista_transicao.append(["N", maquina_2["inicial"] + "2", "e"])
    for elemento in maquina_1["lista_de_transicoes"]:
        lista_transicao.append([(elemento[1] + "1"), (elemento[2] + "1"), (elemento[3] + "1")])
    for elemento in maquina_2["lista_de_transicoes"]:
        lista_transicao.append([(elemento[1] + "2"), (elemento[2] + "2"), (elemento[3] + "2")])
    function saidaAuto(lista_estados, inicial, lista_aceita, lista_transicao)
```

#### Pseudo Código da Função de Intersecção

```{text}
Ainda falta fazer
```

#### Pseudo Código da Função de Complemento

```{text}
function complemento(maquina_1):
    lista_aceita = []
    for elemento in maquina_1["estados"]:
        if (elmento not in maquina_1["aceita"]):
            lista_aceita.append(elemento)
    function saidaAuto(maquina_1["estados"], maquina_1["inicial"], lista_aceita, maquina_2["lista_de_transicoes"])
```

#### Pseudo Código da Função Estrela

Para efeitos praticos chamarei o novo estado inicial de estado `N`.segue Abaixo ideia de codigo de Estrela:

```{text}
function estrela(maquina_1):
    lista_estados = ["N"]
    inicial = "N"
    lista_transicao = maquina_1["lista_de_transicoes"]
    for elemento in maquina_1["estados"]:
        lista_estados.append((elemento))
    for elemento in maquina_1["aceita"]:
        lista_transicao.append([elemento, "N",  "e"])
    function saidaAuto(lista_estados, inicial, maquina_1["aceita"], lista_transicao)
```